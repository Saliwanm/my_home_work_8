from app import app
from flask import render_template


@app.route('/')
def home():
    return 'Hello vonuchka'


@app.route('/<string:calc>')
def calc_user(calc):
    return render_template('calc.html', calc=calc)


@app.route('/<string:calc>/<int:num1>')
def half_user(calc, num1):
    return render_template('halfsuma.html', calc=calc, num1=num1)


@app.route('/<string:calc>/<int:num1>/<int:num2>')
def suma_user(calc, num1, num2):
    return render_template('suma.html', calc=calc, num1=num1, num2=num2)

# @app_route('/calc')
# def calc(calc):
#     return render_template('calc.html', calc=calc)