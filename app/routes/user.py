class User:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age
        
    def get_username(self)->str:
        return self._name
    
#inhert class from User    
class Admin(User):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self._employees: list[User] = []
    
    def print_Employees(self):
        for e in self._employees:
            print(e._name)