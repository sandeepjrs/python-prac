class Saving_account():
    '''this is the saving account PIN and balance'''

    def __init__(self, name, pin, balance = 0.0):
        self._name= name;
        self._pin = pin
        self._balance = balance

    def __lt__(self, other):
        return self._name < other._name

    def __eq__(self, other):
        return self._pin == other._pin



sa1 = Saving_account("sandeep",1234,26.3)
sa2 = Saving_account("sandeep",12234,26.3)
# sa2 = Saving_account("Sandeep",5689,59.6)

print sa2 == sa1


