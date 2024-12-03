from flask import Flask, request
app = Flask(__name__)

personnel = {
    "rachel": "Executive Vice President of Managerial Functions",
    "wallace": "Senior Vice President of Managerial Functions",
    "rosie": "Staff Vice President of Managerial Functions",
    "james": "Vice Vice President of Managerial Functions",
    "henri": "Junior Vice President of Managerial Functions"
}

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/information')
def info():
    return 'Flask is the micro-framework of choice for building Machine Learning API endpoints'

@app.route('/profile/<name>')
def profile(name):
    return f"This is the profile information for {name.upper()}"

@app.route('/personnel/<name>')
def personel_info(name):
    if name in personnel:
        return personnel[name]
    else: 
        return f"No one by the name of {name} here.", 404

@app.route('/employee-search')
def employee_search():
    name = request.args.get('name')
    age = request.args.get('age')
    return f"I searched for employees named {name} who are {age} years old." 




if __name__ == '__main__':
    app.run()
