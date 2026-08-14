from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/returned", methods=["POST"])
def returned():
    member_no = request.form["memberNumber"]

    connection = sqlite3.connect('LIBRARY.db')
    connection.row_factory = sqlite3.Row

    sql = """
    SELECT Loan.Returned,Book.Title,Loan.DateLoaned
    FROM Loan,Book
    JOIN Book ON Book.BookID = Loan.BookID
    JOIN Member ON Member.MemberNumber = Loan.MemberNumber
    WHERE Loan.MemberNumber = ? AND Loan.Returned = FALSE
    GROUP BY Book.Title, Loan.DateLoaned;
    """

    cur = connection.execute(sql,(member_no,))
    data = cur.fetchone()
    connection.close()
    return render_template("returned.html",sql_data = data)

if __name__ == "__main__":
    app.run(port = 5000, debug = True)
    
    
    
