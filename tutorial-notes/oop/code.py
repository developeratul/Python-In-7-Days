class Person:
    def __init__(self, name: str, year_of_birth: int, height: int = None) -> None:
        # private property only accessible in this class
        self.__name = name
        self.year_of_birth = year_of_birth
        self.height = height

    def get_person_info(self):
        return f"name: {self.__name}, year_of_birth: {self.year_of_birth}, height: {self.height if self.height is not None else 'Not Provided'}"

    def set_name(self, name):
        if self.__has_any_number(name):
            print("Sorry name can't contain 0 cause we think you are a hero")
            return
        else:
            self.__name = name

    # private method only accessible through this class
    def __has_any_number(self, string):
        return "0" in string


devr = Person("Ratul", 2006)

person_list: list = [
    Person("Ratul", 2006),
    Person("devR", 1980, 158),
    Person("Kyle", 2001, 298),
    Person("Bob", 1977),
    Person("Mary", 2003, 163),
]

person_above_2000_list: list = []

for person in person_list:
    if person.year_of_birth >= 2000:
        person_above_2000_list.append(person.get_person_info())

# creating subclass and inheriting another class
class Student(Person):
    def __init__(
        self, name: str, year_of_birth: int, email: str, password: int
    ) -> None:
        super().__init__(name, year_of_birth)
        self.email = email
        self.__password = password

    def get_person_info(self):
        return f"email: {self.email}, password: {self.__password}"


ratul = Student("Ratul", 2006, "azammmgol@gmail.com", 12345678)

print(ratul.get_person_info())