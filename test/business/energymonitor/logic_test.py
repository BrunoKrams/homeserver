import unittest
from unittest.mock import MagicMock, patch

from main.business.energymonitor.logic import Display, DataAdapter, MainCommand


class LogicTest(unittest.TestCase):

    @patch("src.logic.Display.__abstractmethods__", set())
    @patch("src.logic.DataAdapter.__abstractmethods__", set())
    def test_execute(self):
        # given
        mock_display = Display()
        mock_display.update = MagicMock()

        mock_data_adapter = DataAdapter()
        mock_data_adapter.get_energy_in_mw = MagicMock(return_value=100)

        main_command = MainCommand(mock_data_adapter, mock_display)

        # when
        main_command.execute()

        # then
        mock_display.update.assert_called_with(100)

if __name__ == '__main__':
    unittest.main()