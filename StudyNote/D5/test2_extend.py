class Person:

    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def __str__(self):
        return self.first_name + " " + self.last_name 


class Employee(Person):

    def __init__(self, first, last, age, id):
        super().__init__(first, last, age)
        self.employee_id = id

    def __str__(self):
        return "FULL NAME: {} EMPLOYEE ID: {}" .format(super().__str__(), self.employee_id)


x = Person("Hanna", "Lee", 33)

y = Employee("Kevin", "Tarvin", 54, 9736549)

print(x)
print(y)