from smartphone import Smartphone



catalog = [
    Smartphone("Apple", "iPhone 14 Pro", "+1234567890"),
    Smartphone("Samsung", "Galaxy S23 Ultra", "+9876543210"),
    Smartphone("Xiaomi", "Redmi Note 12 Pro", "+1112223333"),
    Smartphone("Google", "Pixel 7 Pro", "+4445556666"),
    Smartphone("OnePlus", "11", "+7778889999")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
