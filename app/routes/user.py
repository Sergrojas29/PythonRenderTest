from dataclasses import dataclass
#import dataclasses
@dataclass
class Project:
    project_name: str
    start_date: str
    end_date: str
    #ect



class User:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age
    
    @property
    def name(self)->str:
        return self._name
    
    @staticmethod
    def valid_name(name: str)->bool:
        if(isinstance(name, str)):
            return True
        return False
    
#inhert class from User    
class Admin(User):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self._employees: list[User] = []
    
    def print_Employees(self):
        for e in self._employees:
            print(e._name)