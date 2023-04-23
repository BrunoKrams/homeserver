import unittest
from unittest.mock import MagicMock, patch

from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.energymonitor.logic import Display, DataAdapter


class EnergymonitorTest(unittest.TestCase):

    @patch("main.business.energymonitor.logic.Display.__abstractmethods__", set())
    @patch("main.business.energymonitor.logic.DataAdapter.__abstractmethods__", set())
    @patch("sched.scheduler")
    def test_start(self, mock_scheduler):
        # given
        mock_scheduler.run = MagicMock()
        mock_scheduler.cancel = MagicMock()
        mock_scheduler.enter = MagicMock()

        energymonitor_service = EnergymonitorService(DataAdapter(), Display(), mock_scheduler, 5)

        # when
        energymonitor_service.start()
        energymonitor_service.start()

        # then
        mock_scheduler.run.assert_called_once()

if __name__ == '__main__':
    unittest.main()