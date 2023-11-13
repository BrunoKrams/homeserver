import unittest
from unittest.mock import MagicMock, Mock

from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.lightswitch.lightswitch_service import LightSwitchService
from main.business.print.print_service import PrintService
from main.web.server import Server


class ServerTest(unittest.TestCase):

    def test_index(self):
        # given
        server = Server(self.__create_kitchen_light_service(), self.__create_energymonitor_service(),
                        self.__create_print_service())

        # when
        response = server.app.test_client().get('/')

        # then
        assert response.status_code == 200
        assert "html" in response.data.decode('utf-8')
        response.close()

    def test_kitchen_light_status(self):
        # given
        kitchen_light_service = self.__create_kitchen_light_service()
        kitchen_light_service.status = MagicMock()
        server = Server(kitchen_light_service, self.__create_energymonitor_service(), self.__create_print_service())

        # when
        response = server.app.test_client().get('/kitchenlight')

        # then
        assert response.status_code == 200
        kitchen_light_service.status.assert_called()

    def test_kitchen_light_on(self):
        # given
        kitchen_light_service = self.__create_kitchen_light_service()
        kitchen_light_service.on = MagicMock()
        server = Server(kitchen_light_service, self.__create_energymonitor_service(), self.__create_print_service())

        # when
        response = server.app.test_client().post('/kitchenlight/on')

        # then
        assert response.status_code == 200
        kitchen_light_service.on.assert_called()

    def test_kitchen_light_off(self):
        # given
        kitchen_light_service = self.__create_kitchen_light_service()
        kitchen_light_service.off = MagicMock()
        server = Server(kitchen_light_service, self.__create_energymonitor_service(), self.__create_print_service())

        # when
        response = server.app.test_client().post('/kitchenlight/off')

        # then
        assert response.status_code == 200
        kitchen_light_service.off.assert_called()

    def test_energymonitor_status(self):
        # given
        energymonitor_service = self.__create_energymonitor_service()
        energymonitor_service.status = MagicMock()
        server = Server(self.__create_kitchen_light_service(), energymonitor_service, self.__create_print_service())

        # when
        response = server.app.test_client().get('/energymonitor')

        # then
        assert response.status_code == 200
        energymonitor_service.status.assert_called()

    def test_energy_monitor_start(self):
        # given
        energy_monitor_service = self.__create_energymonitor_service()
        energy_monitor_service.start = MagicMock()
        server = Server(self.__create_kitchen_light_service(), energy_monitor_service, self.__create_print_service())

        # when
        response = server.app.test_client().post('/energymonitor/start')

        # then
        assert response.status_code == 200
        energy_monitor_service.start.assert_called()

    def test_energy_monitor_stop(self):
        # given
        energy_monitor_service = self.__create_energymonitor_service()
        energy_monitor_service.stop = MagicMock()
        server = Server(self.__create_kitchen_light_service(), energy_monitor_service, self.__create_print_service())

        # when
        response = server.app.test_client().post('/energymonitor/stop')

        # then
        assert response.status_code == 200
        energy_monitor_service.stop.assert_called()

    def test_print(self):
        # given
        print_service = self.__create_print_service()
        print_service.print = MagicMock()
        server = Server(self.__create_kitchen_light_service(), self.__create_energymonitor_service(), print_service)

        pdf_file_name = "test.pdf"
        pdf_file = open(pdf_file_name, "rb")
        data = {"file": pdf_file}

        # when
        response = server.app.test_client().post('/print', data=data, content_type="multipart/form-data")

        # then
        assert response.status_code == 200
        print_service.print.assert_called()

    def test_print_no_file(self):
        # given
        print_service = self.__create_print_service()
        print_service.print = MagicMock()
        server = Server(self.__create_kitchen_light_service(), self.__create_energymonitor_service(), print_service)

        # when
        response = server.app.test_client().post('/print')

        # then
        assert response.status_code == 400
        assert response.text == 'Please provide exactly one file'
        print_service.print.assert_not_called()

    def test_print_wrong_extension(self):
        # given
        print_service = self.__create_print_service()
        print_service.print = MagicMock()
        server = Server(self.__create_kitchen_light_service(), self.__create_energymonitor_service(), print_service)

        txt_file_name = "test.txt"
        txt_file = open(txt_file_name, "rb")
        data = {"file": txt_file}

        # when
        response = server.app.test_client().post('/print', data=data, content_type="multipart/form-data")

        # then
        assert response.status_code == 400
        assert response.text == 'Please provide a valid pdf file'
        print_service.print.assert_not_called()

    def __create_kitchen_light_service(self):
        return LightSwitchService(Mock())

    def __create_energymonitor_service(self):
        return EnergymonitorService(Mock(), Mock(), Mock(), Mock())

    def __create_print_service(self):  #
        return PrintService(Mock())


if __name__ == '__main__':
    unittest.main()
