#task4.2
import sqlite3
#Classes
class Person:
  def __init__(self,full_name,date_of_birth):
    self.name = full_name
    self.dob = date_of_birth

  #Class methods
  def getName(self):
    return self.name

  def setName(self,newName):
    self.name = newName

  def getDOB(self):
    return self.dob

  def setDOB(self,newDOB):
    self.dob = newDOB

  def is_adult(self):
    year = int(self.dob[:4])
    return (2026 - year) >= 18


  def screen_name(self):
    month = self.dob[5:7]
    day = self.dob[-2:]

    screen_name = self.name.replace(" ","") + month + day
    return screen_name


class Staff(Person):
  def screen_name(self):
    return Person.screen_name(self) + "Staff"

  def is_adult(self):
    return True


class Student(Person):
  def is_adult(self):
    return False




#Procedures and functions
def ReadandInsertTable(filename):
  with open(filename,'r') as file:
    temp_people = []
    for line in file:
      line = line.strip()
      data = line.split(',')
      temp_people.append(data)
  
  
  people = []
  for person in temp_people:
    name,dob,role = person[0],person[1],person[2]

    if role == "Staff":
      person = Staff(name,dob)

    if role == "Student":
      person = Student(name,dob)

    if role == "Person":
      person = Person(name,dob)
    
    people.append(person)
  
  for person in people:
    connection.execute("INSERT INTO People(FullName,DateOfBirth,ScreenName,IsAdult) VALUES" +
    "(?,?,?,?)",(person.name,person.dob,person.screen_name(),person.is_adult())) 
    connection.commit()

def deleteTable():
  connection.execute("DROP TABLE IF EXISTS People")
  connection.commit()

def createTable():
  connection.execute("CREATE TABLE 'People'(" +
	"'PersonID'	INTEGER PRIMARY KEY AUTOINCREMENT,"+
	"'FullName'	TEXT NOT NULL," +
	"'DateofBirth'	TEXT NOT NULL," +
	"'ScreenName'	TEXT NOT NULL," +
	"'IsAdult'	INTEGER NOT NULL"+
";")
  connection.commit()

#main program
connection = sqlite3.connect('school.db')
deleteTable()
createTable()
ReadandInsertTable('people.txt')
