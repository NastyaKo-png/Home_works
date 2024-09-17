from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address # Тип данных Address
        self.from_address = from_address # Тип данных Address
        self.cost = cost # Тип данных число
        self.track = track # Тип данных строка
    
    def __str__(self):
        return f"{ self.to_address}, {self.from_address}, {self.cost}, {self.track}"

