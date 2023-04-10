import hashlib
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

from main.business.energymonitor.logic import DataAdapter


class LoginState:
    def __init__(self, challenge: str, blocktime: int):
        self.challenge = challenge
        self.blocktime = blocktime
        self.is_pbkdf2 = challenge.startswith("2$")


class FritzboxAdapter(DataAdapter):
    BASE_URL = 'http://fritz.box'
    LOGIN_SID_ROUTE = '/login_sid.lua?version=2'
    HOME_AUTO_SWITCH_ROUTE = '/webservices/homeautoswitch.lua'

    def get_energy_in_mw(self):
        session_id = self.__get_sid(self.BASE_URL, 'energymonitor', 'start123!')
        url = self.BASE_URL + self.HOME_AUTO_SWITCH_ROUTE
        params = '?ain=116570612483&switchcmd=getswitchpower&sid=' + session_id
        url = url + format(params)
        return int(urllib.request.urlopen(url).read().decode('utf-8').strip())

    def __get_sid(self, box_url: str, username: str, password: str) -> str:
        try:
            state = self.__get_login_state(box_url)
        except Exception as ex:
            raise Exception("failed to get challenge") from ex
        if state.is_pbkdf2:
            challenge_response = self.__calculate_pbkdf2_response(state.challenge, password)
        else:
            challenge_response = self.__calculate_md5_response(state.challenge, password)
        if state.blocktime > 0:
            time.sleep(state.blocktime)
        try:
            sid = self.__send_response(box_url, username, challenge_response)
        except Exception as ex:
            raise Exception("failed to login") from ex
        if sid == "0000000000000000":
            raise Exception("wrong username or password")
        return sid

    def __get_login_state(self, box_url: str) -> LoginState:
        url = box_url + self.LOGIN_SID_ROUTE
        http_response = urllib.request.urlopen(url)
        xml = ET.fromstring(http_response.read())
        challenge = xml.find("Challenge").text
        blocktime = int(xml.find("BlockTime").text)
        return LoginState(challenge, blocktime)

    @staticmethod
    def __calculate_pbkdf2_response(challenge: str, password: str) -> str:
        challenge_parts = challenge.split("$")
        iter1 = int(challenge_parts[1])
        salt1 = bytes.fromhex(challenge_parts[2])
        iter2 = int(challenge_parts[3])
        salt2 = bytes.fromhex(challenge_parts[4])
        hash1 = hashlib.pbkdf2_hmac("sha256", password.encode(), salt1, iter1)
        hash2 = hashlib.pbkdf2_hmac("sha256", hash1, salt2, iter2)
        return f"{challenge_parts[4]}${hash2.hex()}"

    @staticmethod
    def __calculate_md5_response(challenge: str, password: str) -> str:
        response = challenge + "-" + password
        response = response.encode("utf_16_le")
        md5_sum = hashlib.md5()
        md5_sum.update(response)
        response = challenge + "-" + md5_sum.hexdigest()
        return response

    def __send_response(self, box_url: str, username: str, challenge_response: str) -> str:
        post_data_dict = {"username": username, "response": challenge_response}
        post_data = urllib.parse.urlencode(post_data_dict).encode()
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = box_url + self.LOGIN_SID_ROUTE
        http_request = urllib.request.Request(url, post_data, headers)
        http_response = urllib.request.urlopen(http_request)
        xml = ET.fromstring(http_response.read())
        return xml.find("SID").text
