from abc import ABC, abstractmethod

class PrintAdapter(ABC):

    @abstractmethod
    def print(self, file_path):
        pass
