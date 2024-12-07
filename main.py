import random
from decimal import Decimal
from datetime import datetime, timedelta

class CurrencyConverter:
    def __init__(self, exchange_rate):
        if not isinstance(exchange_rate, Decimal):
            raise ValueError("Ayirboshlash kursi o'nlik tipda bo'lishi kerak.")
        self.exchange_rate = exchange_rate

    def convert(self, amount):
        if not isinstance(amount, (int, Decimal)):
            raise ValueError("Miqdor butun yoki o'nlik bo'lishi kerak.")

        converted_amount = amount * self.exchange_rate

        day_offset = random.randint(-30, 30)
        conversion_date = datetime.now() + timedelta(days=day_offset)

        return converted_amount, conversion_date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    exchange_rate = Decimal('12000')
    converter = CurrencyConverter(exchange_rate)

    try:
        amount_to_convert = Decimal((input("Miqdorni kiriting: ")))
        result, date = converter.convert(amount_to_convert)
        print(f"{amount_to_convert}$ --> {result} som (Sana: {date})")
    except ValueError as e:
        print(f"Xato: {e}")


#=========================================================================================================
#===========================================2 VAZIFA======================================================
#=========================================================================================================




import random
from decimal import Decimal


class ValueError(Exception):
    def __init__(self,message):
        self.message = message


class Check_Price:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance, value):
        if type(value) == Decimal:
            if value > 0:
                 instance.__dict__[self.name]=value

            else:
                raise ValueError("Qiymat xato kiritildi!!")
        else:
            raise ValueError("Qiymat xato kiritildi!!")

    def __get__(self, instance, owner):
        return  instance.__dict__[self.name]
    def __delete__(self, instance):
         del instance.__dict__[self.name]

class Mahsulot:
    def __init__(self, narx):
        self.narx = narx
    def sana(self):
        c = ["2024.12.21", "2024.12.09", "2024.12.01", "2024.12.05"]
        b = random.choice(c)
        return b
    def cheginma(self):
        a = random.randint(1,50)
        javob =  self.narx - self.narx * a /100
        return (f"Maxsulot narxi: {self.narx}, chegirma: {a}\n"
                f"Chegirmadagi narx: {javob} Sana: {p1.sana()}")


narx = Decimal(input("Maxshlot narxini kiriting: "))
p1 = Mahsulot(narx)
print(p1.cheginma())
#
#
#
#
#
#
#
#
#














