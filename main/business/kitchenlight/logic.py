from abc import ABC, abstractmethod

class KitchenLightAdapter(ABC):

    @abstractmethod
    def status(self)->bool:
        pass

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass