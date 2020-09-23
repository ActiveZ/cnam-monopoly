from random import randint 

class De:


    def __init__(self):
        self.is_double = False


    def lancer(self):
        d1 = randint(1,6)
        d2 = randint(1,6)
        self.is_double = d1 == d2
        return d1 + d2
