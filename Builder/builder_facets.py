

class Person:
    def __init__(self):
        # Address
        self.street_address = None
        self.postcode = None
        self.city = None
        # Employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f"Address: {self.street_address}, {self.postcode}, {self.city}" +\
            f"Employed at {self.company_name} as a {self.position} earning {self.annual_income}"


class PersonBuilder: # Facade
    def __init__(self, person=Person()):
        self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)
