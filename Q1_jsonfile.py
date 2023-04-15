import json
class  Employee:
    def __init__(self,Name,DoB,Height,City,State):
        self.Name=Name
        self.DOB=DoB
        self.Height=Height
        self.City=City
        self.State=State
with open("Employee.json")as f:
 data=json.load(f)

Employeelist=[]
for i in data["emp_details" ]:
    Employeelist.append(Employee(i['Name'],i['DOB'],i['Height'],i['City'],i['State']))
for j in Employeelist:
 print(j.Name,j.DOB, j.Height, j.City, j.State)
