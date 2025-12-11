class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(f"{self.name}: работает")
    
    def get_info(self):
        print(f"Сотрудник: {self.name}, Зарплата: {self.salary} руб.")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def work(self):
        print(f"{self.name}: Управляет отделом '{self.department}'")
    
    def hold_meeting(self):
        print(f"{self.name}: Проводит совещание в отделе '{self.department}'")
    
    def get_info(self):
        base_info = super().get_info()
        print(f"{base_info}, Должность: Менеджер, Отдел: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def work(self):
        print(f"{self.name}: Пишет код на {self.programming_language}")
    
    def debug_code(self):
        print(f"{self.name}: Отлаживает код на {self.programming_language}")
    
    def get_info(self):
        base_info = super().get_info()
        print(f"{base_info}, Должность: Разработчик, Язык: {self.programming_language}")
