from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    return n1+n2

def minus(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get('first')
    number_2 = request.form.get('second')
    operation = request.form.get('operation')

    result = 0

    if operation == 'add':
        if((number_1=="" or number_2=="")):
            flash(f'Please enter the numbers properly...')
            
        elif(number_1.isdigit()!=True or number_2.isdigit()!=True):
            flash(f'Please enter the numbers properly...')

        else:
            result = add(int(number_1), int(number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')



    elif operation == 'minus':
        if((number_1==None or number_2==None)):
            flash(f'Please enter the numbers properly...')
            
        elif(number_1.isdigit()!=True or number_2.isdigit()!=True):
            flash(f'Please enter the numbers properly...')

        else:
            result =  minus(int(number_1), int(number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')


    elif operation == 'multiply':
        if((number_1==None or number_2==None)):
            flash(f'Please enter the numbers properly...')
            
        elif(number_1.isdigit()!=True or number_2.isdigit()!=True):
            flash(f'Please enter the numbers properly...')

        else:
            result = multiply(int(number_1), int(number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
  
    
    elif operation == 'divide':
        if((number_1==None or number_2==None)):
            flash(f'Please enter the numbers properly...')
            
        elif(number_1.isdigit()!=True or number_2.isdigit()!=True):
            flash(f'Please enter the numbers properly...')
        
        elif(number_2=="0"):
            flash(f'Denominator cannot be zero...')

        else:
            result = divide(int(number_1), int(number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5051,
        host="0.0.0.0"
    )
