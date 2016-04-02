import time


class Date:
    def __init__(self):
        self.day = int(time.strftime('%d', time.localtime()))
        self.month = int(time.strftime('%m', time.localtime()))
        self.year = int(time.strftime('%y', time.localtime()))
        self.valeur = self.day+self.month*100+self.year*10000
