from abc import ABC, abstractmethod


class DataAdapter(ABC):
    @abstractmethod
    def get_energy_in_mw(self):
        pass


class Display(ABC):
    @abstractmethod
    def update(self, energy_in_mw: int):
        pass

    @abstractmethod
    def clear(self):
        pass




