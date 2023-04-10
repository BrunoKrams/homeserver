from abc import ABC, abstractmethod


class DataAdapter(ABC):
    @abstractmethod
    def get_energy_in_mw(self):
        pass


class Display(ABC):
    @abstractmethod
    def update(self, energy_in_mw: int):
        pass


class MainCommand:
    def __init__(self, data_dapter: DataAdapter, display: Display):
        self.data_adapter = data_dapter
        self.display = display

    def execute(self):
        enery_in_mw = self.data_adapter.get_energy_in_mw()
        self.display.update(enery_in_mw)
