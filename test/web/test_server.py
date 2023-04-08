import unittest
from unittest.mock import MagicMock

from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.lightswitch.lightswitch_service import LightswitchService
from main.web.server import Server


class ServerTest(unittest.TestCase):

    def test_index(self):
        # given
        server = Server(LightswitchService(), EnergymonitorService())

        # when
        response = server.app.test_client().get('/')

        # then
        assert response.status_code == 200
        assert "html" in response.data.decode('utf-8')
        response.close()

    def test_lightswitch_status(self):
        # given
        lightswitch_service = LightswitchService()
        lightswitch_service.status = MagicMock()
        server = Server(lightswitch_service, EnergymonitorService())

        # when
        response = server.app.test_client().get('/lightswitch')

        # then
        assert response.status_code == 200
        lightswitch_service.status.assert_called()

    def test_lightswitch_on(self):
        # given
        lightswitch_service = LightswitchService()
        lightswitch_service.on = MagicMock()
        server = Server(lightswitch_service, EnergymonitorService())

        # when
        response = server.app.test_client().post('/lightswitch/on')

        # then
        assert response.status_code == 200
        lightswitch_service.on.assert_called()

    def test_lightswitch_off(self):
        # given
        lightswitch_service = LightswitchService()
        lightswitch_service.off = MagicMock()
        server = Server(lightswitch_service, EnergymonitorService())

        # when
        response = server.app.test_client().post('/lightswitch/off')

        # then
        assert response.status_code == 200
        lightswitch_service.off.assert_called()

    def test_energy_monitor_start(self):
        # given
        energy_monitor_service = EnergymonitorService()
        energy_monitor_service.start = MagicMock()
        server = Server(LightswitchService(), energy_monitor_service)

        # when
        response = server.app.test_client().post('/energymonitor/start')

        # then
        assert response.status_code == 200
        energy_monitor_service.start.assert_called()

    def test_energy_monitor_stop(self):
        # given
        energy_monitor_service = EnergymonitorService()
        energy_monitor_service.stop = MagicMock()
        server = Server(LightswitchService(), energy_monitor_service)

        # when
        response = server.app.test_client().post('/energymonitor/stop')

        # then
        assert response.status_code == 200
        energy_monitor_service.stop.assert_called()

if __name__ == '__main__':
    unittest.main()
