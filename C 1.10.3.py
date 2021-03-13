class Client():
    def __init__(self,surname, name, balance):
        self.surname = surname
        self.name = name
        self.balance = balance
    def get_data(self,surname):
        return self.surname

    def get_name(self, name):
        return self.name

    def get_balance(self, balance):
        return self.balance
