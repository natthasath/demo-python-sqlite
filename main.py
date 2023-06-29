from sqlite.sqlite import Database

# Usage example:
db = Database('company.db')
db.create_table()

db.insert_employee('John Doe', 30, 5000.0)
db.insert_employee('Jane Smith', 35, 6000.0)

employees = db.get_employees()
print(employees)

db.update_employee(1, 'John Doe', 31, 5500.0)

db.delete_employee(2)

employees = db.get_employees()
print(employees)
