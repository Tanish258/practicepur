class Employee:
  def __init__(self,name,age,salary):
    self.name = name 
    self.age = age
    self.salary = salary


class EmpolyeeManager:
  def __init__(self):
    self.e = Employee()

  def add(self):
    self.e.name = input('Enter name')
    self.e.age = input('Enter age')
    self.e.salary = input('Enter salary')
    
  

class FrontManager:
  def __init__(self):
    self.em = EmployeeManager()

  message = ['1.Add Employee']
  user = int(input('\n'.join(message),'\nEnter the option you want to perform'))

  if user == 1:
    self.em.add()
  else:
    print('Invalid Input')
