class employee():
    company="TechCorpSolutions"
    total_employes=0
    mini=15000
    maxi=500000
    pf_percentage=12

    @classmethod
    def display(cls):
        return cls.company
    def __init__(self,name,department,salary,pannumber,empid=None):
        employee.total_employes+=1

        if empid is None:
            self._emp_id=employee.total_employes
        else:
            raise ArithmeticError("cannot assign empid")

        self.name=name
        self._department=department
        self.salary=salary
        self.__pannumber=pannumber

    @property
    def emp_id(self):
        return self._emp_id


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if self.is_valid_salary(amount):
            self._salary = amount
        else:
            raise ValueError("Invalid salary")

    def applyhike(self, percent):
        if 0 <= percent <= 50:
            self.salary += self.salary * percent / 100
            return self.salary
        raise ValueError("Hike percentage should be between 0 and 50")

    def calculate_pf(self):
        return self._salary*employee.pf_percentage/100
    
    def transfer_department(self,new_dept):
        print("old dept:",self._department)
        self._department=new_dept
        print("new dept:",self._department)

    @classmethod
    def get_total_employees(cls):
        return cls.total_employes

    @staticmethod
    def is_valid_salary(amount):
        return isinstance(amount,(int,float)) and employee.mini<=amount<=employee.maxi

    def __str__(self):
        return (
            f"ID:{self.emp_id}, "
            f"Name:{self.name}, "
            f"Department:{self._department}, "
            f"Salary:{self.salary}"
        )
    




    


        
    

    
