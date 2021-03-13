class Guest:

    def __init__(self, name, surname, city, status):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status


    def get_name(self):
        return (self.name)

    def get_surname(self):
        return (self.surnameame)

    def get_city(self):
        return (self.city)

    def get_status(self):
        return (self.status)

class Client(Guest):
    def set_balance(self, balance):

        if balance >= 1000000:
            print("VIP")
        elif balance < 1000000 >= 500000:
            print("Premium")
        elif 0 < balance < 500000:
            print("Standart")
        else:
            return False
        self.balance = balance
        return self.balance

ivan = Guest (name = "Иван", surname = "Петров", city = "г.Москва", status = "'Наставник'")
silvestor = Client(name = "Сильвестор", surname = "Зиберштейн", city = "г.Лондон", status = "'Клиент'")


print('"', ivan.name, ivan.surname,",", ivan.city,", статус", ivan.status,'"')
print("__________________________________________")
print('"', silvestor.name, silvestor.surname,",", silvestor.city,",", 'статус', silvestor.status,'"')
print("Баланс:", silvestor.set_balance(10000000))
print("__________________________________________")



    



