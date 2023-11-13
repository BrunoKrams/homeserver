import subprocess

import cups

from main.business.print.logic import PrintAdapter

class CupsPrintAdapter(PrintAdapter):

    def print(self, file_path):
        subprocess.run("lp", file_path)



