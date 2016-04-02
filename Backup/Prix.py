import Date


class Prix:
    """
    Le prix lié à la date.
    """

    def __init__(self, prix):
        self.cout = prix
        self.date = Date.Date()

    def DateOfDay(self):
        self.date = Date.Date