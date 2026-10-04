from employeemanagementsystem import employee

print("Company:",employee.display())
print("Employee Count:",employee.get_total_employees())

e1=employee("Rahul","IT",50000,"ABCDE1234F")
e2=employee("Anjali","HR",40000,"XYZAB5678P")

print(e1)
print(e2)

print("Employee Count:",employee.get_total_employees())

print("PF:",e1.calculate_pf())

print(e1)
e1.applyhike(10)
print(e1)

e1.transfer_department("Finance")

try:
    e1.salary=10000
except Exception as e:
    print(e)

try:
    e1.emp_id=100
except Exception as e:
    print(e)

print(e1._department)
e1._department="Testing"
print(e1._department)

try:
    print(e1.__pannumber)
except Exception as e:
    print(type(e),e)

print(e1._employee__pannumber)
