from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db:5432/employee_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    department = db.Column(db.String(100))
    salary = db.Column(db.Float)

@app.route('/')
def home():
    return "Employee API Running!"

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    data = [{"id": e.id, "name": e.name, "department": e.department, "salary": e.salary} for e in employees]
    return jsonify(data)

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    emp = Employee(name=data['name'], department=data['department'], salary=data['salary'])
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "Employee added!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
