#task 1.1
import sqlite3
connection = sqlite3.connect("TESTDATABASE.db")

#functions and procedures
def createTables():
  #creates class table:
  connection.execute("CREATE TABLE 'Class' ("+
	"'ClassName'	TEXT," +
	"'YearGroup'	INTEGER NOT NULL," +
	"PRIMARY KEY('ClassName')" +
");")
  connection.commit()
  
  #create student table
  connection.execute("CREATE TABLE 'Student' (" +
	"'StudentID'	INTEGER," +
	"'GivenName'	TEXT NOT NULL," +
	"'FamilyName'	TEXT NOT NULL," +
	"'ClassName'	TEXT NOT NULL," +
	"PRIMARY KEY('StudentID')," +
	"FOREIGN KEY('ClassName') REFERENCES 'Class'('ClassName')"+
");")
  connection.commit()


  #create test table
  connection.execute("CREATE TABLE 'Test' ("+
	"'TestID'	TEXT,"+
	"'MaxMarks'	INTEGER NOT NULL,"+
	"PRIMARY KEY('TestID')"+
");")
  connection.commit()

  #creates student_test table
  connection.execute("CREATE TABLE `Student_Test` ("+
	"`StudentTestID`	INTEGER UNIQUE,"+
	"`StudentID`	INTEGER NOT NULL,"+
	"`TestID`	TEXT NOT NULL,"+
	"`Mark`	INTEGER NOT NULL,"+
	"`DateTest`	TEXT NOT NULL,"+
	"FOREIGN KEY(`StudentID`) REFERENCES `Student`(`StudentID`),"+
	"PRIMARY KEY(`StudentTestID`),"+
	"FOREIGN KEY(`TestID`) REFERENCES `Test`(`TestID`)"+
");")
  connection.commit()

def insertTable():
#insert class record
connection.execute("INSERT INTO Class (ClassName, YearGroup) VALUES (?, ?);",
                    ("CS3", 12))
connection.commit()

#insert student record
connection.execute("INSERT INTO Student (StudentID, GivenName, FamilyName, ClassName) VALUES (?, ?, ?, ?);",
                    (102, "Mary", "Lim", "CS3"))
connection.commit()

#insert test record
connection.execute("INSERT INTO Test (TestID, MaxMarks) VALUES (?, ?);",
                    ("PG1", 100))
connection.commit()

#insert student_test record
connection.execute("INSERT INTO Student_Test (StudentTestID, StudentID, TestID, Mark, DateTest) VALUES (?, ?, ?, ?, ?);",
                    (123, 102, "PG1", 85, "01-02-2023"))
connection.commit()

#main program
createTables()
insertTable()
