class Employee:
  def __init__(self,name=None,age=0,salary=0.0):
    self.name = name 
    self.age = age
    self.salary = salary


class EmployeeManager:
  def __init__(self):
    self.employees = []

  def add(self):
    name = input('Enter the name:').strip()
    age = int(input('Enter the age:'))
    salary = int(input('Enter the salary:'))
    self.employees.append(Employee(name,age,salary))
  
  def list(self):
    for i in self.employees:
      print(f'Name:{i.name},Age:{i.age},Salary:{i.salary}')
  
  def delete_by_age(self):
    f = int(input('Enter the starting range of age(inclusive):'))
    t = int(input('Enter the ending range of age(inclusive):'))
    self.employees = [emp for emp in self.employees if not(f<= emp.age <= t)]

  def update_salary(self):
    name = input('Enter name:').strip()
    salary = int(input('Enter salary to be updated:'))
    
    for i in self.employees:
      if i.name == name:
        i.salary  = salary
        break
    else:
        print(f'Employee not found with name {name}')

class FrontManager:
  def __init__(self):
    self.em = EmployeeManager()

  def run(self):

    while True:

      message = ['0.Exit','1.Add Employee','2.list the employees','3.Delete employees within specific age range','4.Update salary by name']
      print('\n'.join(message))
      user = int(input('\nEnter the option you want to perform'))

      if user == 1:
        self.em.add()
      elif user == 2:
        self.em.list()
      elif user == 0:
        break
      elif user == 3:
        self.em.delete_by_age()
      elif user == 4:
        self.em.update_salary()
      else:
        print('Invalid Input')

a = FrontManager()
a.run()


  
