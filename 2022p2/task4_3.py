#task4.1
import sqlite3
connection = sqlite3.connect('LIBRARY.db')
cur = connection.cursor()

def deleteTable():
  connection.execute("DROP TABLE IF EXISTS Book")
  connection.execute("DROP TABLE IF EXISTS Member")
  connection.execute("DROP TABLE IF EXISTS Loan")
  connection.commit()


def createTable():
  connection.execute("CREATE TABLE `Book` ("+
	"`BookID`	INTEGER,"+
	"`Title`	TEXT NOT NULL,"+
	"`Genre`	TEXT NOT NULL,"+
	"PRIMARY KEY(`BookID`)"+
");")
  connection.execute("CREATE TABLE `Member` ("+
	"`MemberNumber`	INTEGER UNIQUE,"+
	"`FamilyName`	TEXT NOT NULL,"+
	"`GivenName`	TEXT NOT NULL,"+
	"PRIMARY KEY(`MemberNumber`)"+
");")
  connection.execute("CREATE TABLE `Loan` ("+
	"`LoanID`	INTEGER UNIQUE,"+
	"`MemberNumber`	INTEGER,"+
	"`BookID`	INTEGER,"+
	"`DateLoaned`	TEXT NOT NULL,"+
	"`Returned`	TEXT NOT NULL,"+
	"FOREIGN KEY(`MemberNumber`) REFERENCES `Member`(`MemberNumber`),"+
	"FOREIGN KEY(`BookID`) REFERENCES `Book`(`BookID`),"+
	"PRIMARY KEY(`LoanID`)"+
");")
  connection.commit()
#task4.2
def insertTable():
  with open('BOOK.txt','r') as file:
    for line in file:
      data = line.strip()
      data = data.split(',')

      connection.execute("INSERT INTO Book(BookID,Title,Genre) VALUES (?,?,?)",(data[0],data[1],data[2]))
  connection.commit()
  
  with open('LOAN.txt','r') as file:
    for line in file:
      data = line.strip()
      data = data.split(',')

      connection.execute("INSERT INTO Loan(LoanID,MemberNumber,BookID,DateLoaned,Returned) VALUES (?,?,?,?,?)",(data[0],data[1],data[2],data[3],data[4]))
  connection.commit()
  
  with open('MEMBER.txt','r') as file:
    for line in file:
      data = line.strip()
      data = data.split(',')

      connection.execute("INSERT INTO Member(MemberNumber,FamilyName,GivenName) VALUES (?,?,?)",(data[0],data[1],data[2]))
  connection.commit()
#task4.3
def searchTable():
  key = int(input("Enter Member No. :"))
  cur.execute("SELECT Loan.MemberNumber,Book.Title,Loan.Returned,Loan.DateLoaned FROM LOAN,BOOK "+
                     "WHERE Loan.MemberNumber = ? AND Loan.BookID = Book.BookID "+
                     "ORDER BY Loan.DateLoaned ASC", (key,))
  records = cur.fetchall()
  print()
  print(f'{"Date Loaned":<10}{"Book":^10}{"Returned":>10}')
  for record in records:
    title,returned,dateloaned = record[1],record[2],record[3]
    if returned == "True":
      returned = 'Yes'
    else:
      returned = 'No'
    print(f'{dateloaned:<10}{title:^10}{returned:>10}')


#main program
deleteTable()
createTable()
insertTable()
searchTable()
