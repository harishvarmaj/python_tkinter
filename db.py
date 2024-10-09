
import sqlite3

class Database:
    def __init__(self , db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, name, age, doj, email, gender, contact, address):

        self.cur.execute("Insert into employees values (NULL,?,?,?,?,?,?,?)" , (name, age, doj, email, gender, contact, address))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows

    def remove(self, id):
        self.cur.execute("delete from employees where id=?",(id))
        self.con.commit()

    def update(self,id, name, age, doj, email, gender, contact, address):
        self.cur.execute("update  employees set  name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=? ",
                         (name, age, doj, email, gender, contact, address,id))
        self.con.commit()


