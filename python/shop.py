from dataclasses import dataclass


@dataclass
class Address:
    line1: str
    line2: str
    city: str
    zip_code: str
    country: str


@dataclass
class User:
    name: str
    email: str
    age: int
    address: Address
    verified: bool
    
    class Builder:
        def __init__(self):
            self.name = None
            self.email = None
            self.age = None
            self.address = None
            self.verified = None

        def with_name(self, name):
            self.name = name
            return self

        def with_email(self, email):
            self.email = email
            return self

        def with_age(self, age):
            self.age = age
            return self

        def with_address(self, address):
            self.address = address
            return self

        def with_verified(self, verified):
            self.verified = verified
            return self

        def build(self):
            return User(self.name, self.email, self.age, self.address, self.verified)


class Shop:
    @classmethod
    def can_order(cls, user):
        if user.age <= 18:
            return False
        if not user.verified:
            return False #FIXME: c'était kc
        else:
            return True

    @classmethod
    def must_pay_foreign_fee(cls, user):
        return user.address.country != "USA"

        