from main.business.print.logic import PrintAdapter

class PrintService:

    def __init__(self, print_adapter:PrintAdapter):
        self.print_adapter = print_adapter

    def print(self, file):
        self.print_adapter.print(file)