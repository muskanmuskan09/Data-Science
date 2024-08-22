from abc import ABC, abstractmethod

# Task 1: Creating an Abstract Class with Abstraction
class Person(ABC):
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"
    
    def greet(self, other_person):
        return f"Hello {other_person.name}! My name is {self.name}."
    
    @abstractmethod
    def introduce(self):
        pass
    
    @staticmethod
    def is_adult(age):
        return age > 18

# Task 2: Single Inheritance, Encapsulation
class Employee(Person):
    _counter = 0  # Private class attribute for counting instances
    
    def __init__(self, name, age, gender, address, salary):
        super().__init__(name, age, gender, address)
        Employee._counter += 1
        self._employee_id = f"EMP{Employee._counter:02d}"
        self._salary = salary
    
    @property
    def employee_id(self):
        return self._employee_id
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
    
    def increase_salary(self, amount):
        if amount > 0:
            self._salary += amount
    
    def decrease_salary(self, amount):
        if amount > 0:
            self._salary -= amount
    
    @property
    def counter(self):
        return Employee._counter
    
    def introduce(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}"

# Task 3: Multiple Inheritance, Polymorphism
class Teacher(Employee):
    _counter = 0  # Private class attribute for counting instances
    
    def __init__(self, name, age, gender, address, salary, subjects):
        super().__init__(name, age, gender, address, salary)
        Teacher._counter += 1
        self._teacher_id = f"TEC{Teacher._counter:02d}"
        self.subjects = subjects
    
    @property
    def teacher_id(self):
        return self._teacher_id
    
    @property
    def counter(self):
        return Teacher._counter
    
    @property
    def employee_id(self):
        raise AttributeError("Teacher object has no attribute 'employee_id'")
    
    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
    
    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
    
    def introduce(self):
        return f"{self.teacher_id} teaches {', '.join(self.subjects)}."

# Example Testing

if __name__ == "__main__":
    # Instantiate Employee and Teacher objects
    employee1 = Employee("Muskan", 20, "Female", "892 Hello Street", 50000)
    print(employee1.introduce())

    teacher1 = Teacher("Anurag", 25, "Male", "202 Thakur ji Street", 60000, ["Math", "Physics"])
    print(teacher1.introduce())    
    teacher1.add_subject("Chemistry")
    print(teacher1.introduce())    
    teacher1.remove_subject("Math")
    print(teacher1.introduce())   