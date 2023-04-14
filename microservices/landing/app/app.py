from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    url = "http://addition-service:5052/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1+n2

def minus(n1, n2):
    url = "http://subtraction-service:5053/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1-n2

def multiply(n1, n2):
    url = "http://multiplication-service:5054/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1*n2

def divide(n1, n2):
    url = "http://division-service:5055/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1/n2
    
def exponent(n1, n2):
    url = "http://exponent-service:5056/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1**n2
    
def modulus(n1, n2):
    url = "http://modulus-service:5057/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1%n2

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
            flash(f'Zero Division Errorrrr...')

        else:
            result = divide(int(number_1), int(number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
       
    
    elif operation == 'exponent':
        if((number_1==None or number_2==None)):
            flash(f'Please enter the numbers properly1...')
            
        elif(number_1.isdigit()!=True or number_2.isdigit()!=True):
            flash(f'Please enter the numbers properly2...')

        else:
            result = exponent(int(number_1), int(number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
        
        
    elif operation == 'modulus':
        if((number_1==None or number_2==None)):
            flash(f'Please enter the numbers properly...')
            
        elif(number_1.isdigit()!=True or number_2.isdigit()!=True):
            flash(f'Please enter the numbers properly...')
        
        elif(number_2=="0"):
            flash(f'Modulus by Zero is undefined..')
        
        else:
            result = modulus(int(number_1), int(number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5051,
        host="0.0.0.0"
    )
