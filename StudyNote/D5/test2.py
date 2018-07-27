class Person:

    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.last_name


class Employee(Person):

    def __init__(self, first, last, age, id):
        Person.__init__(self, first, last, age)
        self.employee_id = id

    def get_employee(self):
        return "FULL NAME: {} EMPLOYEE ID: {}" .format(self.full_name(), self.employee_id)


x = Person("Hanna", "Lee", 26)

y = Employee("Kevin", "Tarvin", 34, 9736549)

print(x.full_name())
print(y.get_employee())