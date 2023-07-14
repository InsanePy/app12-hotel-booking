import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "The Real Estate Company"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        print(availability)
        if availability == "yes":
            return True
        else:
            return False
    @classmethod
    def hotel_count(cls, data):
        return len(data)

    def __eq__(self, other):
        if self.hotel_id ==other.hotel_id:
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel Name: {self.hotel.name}"""

        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2


hotel1 = Hotel(hotel_id="134")
hotel2 = Hotel(hotel_id="188")
hotel3 = Hotel(hotel_id="188")

# instance variables
print(hotel1.name)
print(hotel2.name)

# Class variables
print(Hotel.watermark)

# Accessing Class variables with instance variables
print(hotel1.watermark)
print(hotel2.watermark)

# calling a class method
print(Hotel.hotel_count(df))

print(hotel1.hotel_count(df))
print(hotel2.hotel_count(df))

# properties
ticket = ReservationTicket(customer_name="john smith ",hotel_object=hotel1)
print(ticket.the_customer_name)
print(ticket.generate())

# static method
converted = ReservationTicket.convert(10)
print(converted)

# magic methods
print(hotel1 == hotel2)
print(hotel2 == hotel3)
