import unittest
from unittest.mock import MagicMock, Mock

from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.lightswitch.lightswitch_service import LightswitchService
from main.web.server import Server


class ServerTest(unittest.TestCase):

    def test_index(self):
        # given
        server = Server(self.__create_lightswitch_service(), self.__create_energymonitor_service())

        # when
        response = server.app.test_client().get('/')

        # then
        assert response.status_code == 200
        assert "html" in response.data.decode('utf-8')
        response.close()

    def test_lightswitch_status(self):
        # given
        lightswitch_service = self.__create_lightswitch_service()
        lightswitch_service.status = MagicMock()
        server = Server(lightswitch_service, self.__create_energymonitor_service())

        # when
        response = server.app.test_client().get('/lightswitch')

        # then
        assert response.status_code == 200
        lightswitch_service.status.assert_called()

    def test_lightswitch_on(self):
        # given
        lightswitch_service = self.__create_lightswitch_service()
        lightswitch_service.on = MagicMock()
        server = Server(lightswitch_service, self.__create_energymonitor_service())

        # when
        response = server.app.test_client().post('/lightswitch/on')

        # then
        assert response.status_code == 200
        lightswitch_service.on.assert_called()

    def test_lightswitch_off(self):
        # given
        lightswitch_service = self.__create_lightswitch_service()
        lightswitch_service.off = MagicMock()
        server = Server(lightswitch_service, self.__create_energymonitor_service())

        # when
        response = server.app.test_client().post('/lightswitch/off')

        # then
        assert response.status_code == 200
        lightswitch_service.off.assert_called()

    def test_energymonitor_status(self):
        # given
        energymonitor_service = self.__create_energymonitor_service()
        energymonitor_service.status = MagicMock()
        server = Server(self.__create_lightswitch_service(), energymonitor_service)

        # when
        response = server.app.test_client().get('/energymonitor')

        # then
        assert response.status_code == 200
        energymonitor_service.status.assert_called()

    def test_energy_monitor_start(self):
        # given
        energy_monitor_service = self.__create_energymonitor_service()
        energy_monitor_service.start = MagicMock()
        server = Server(self.__create_lightswitch_service(), energy_monitor_service)

        # when
        response = server.app.test_client().post('/energymonitor/start')

        # then
        assert response.status_code == 200
        energy_monitor_service.start.assert_called()

    def test_energy_monitor_stop(self):
        # given
        energy_monitor_service = self.__create_energymonitor_service()
        energy_monitor_service.stop = MagicMock()
        server = Server(self.__create_lightswitch_service(), energy_monitor_service)

        # when
        response = server.app.test_client().post('/energymonitor/stop')

        # then
        assert response.status_code == 200
        energy_monitor_service.stop.assert_called()

    def __create_lightswitch_service(self):
        return LightswitchService(Mock())

    def __create_energymonitor_service(self):
        return EnergymonitorService(Mock(), Mock(), Mock(), Mock())


if __name__ == '__main__':
    unittest.main()
