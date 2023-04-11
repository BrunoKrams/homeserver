from main.business.energymonitor.logic import Display


class CommandLineDisplay(Display):

    def update(self, energy_in_mw:int):
        print(energy_in_mw)

    def clear(self):
        print('Cleared')
