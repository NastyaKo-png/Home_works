
from mailing import Mailing
from address import Address

# Создаем адреса
to_address = Address(123456, "Москва", "Ленина", 10, 15)
from_address = Address(789012, "Санкт-Петербург", "Невского", 20, 25)

# Создаем почтовое отправление
mailing = Mailing(to_address, from_address, 150, "TR123456789")

# Выводим информацию о отправлении
print (
    f' Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, ',
    f' {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} ',
    f' в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, ',
    f' {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.'
    )

