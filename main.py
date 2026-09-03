#working with numbers
from pyscript import display, document 


def greetings(e): #initializing a function 

    username = document.getElementById('user_input').value #getting the data from the text box

    display(f'Hello {username}', target='result') 

def adding_numbers(e): 

    document.getElementById('results').innerHTML = "" #clear 

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number + second_number

    display(f'The sum of {first_number} and {second_number} is {sum}', target='results')

def subtracting_numbers(e):

    document.getElementById('results').innerHTML = "" #clear 

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    difference = first_number - second_number

    display(f'The difference of {first_number} and {second_number} is {difference}', target='results')

def multiplying_numbers(e):

    document.getElementById('results').innerHTML = "" #clear 

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    product = first_number * second_number

    display(f'The product of {first_number} and {second_number} is {product}', target='results')

def dividing_numbers(e):

    document.getElementById('results').innerHTML = "" #clear 

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    quotient = first_number / second_number

    display(f'The quotient of {first_number} and {second_number} is {quotient}', target='results')

def floor_dividing_numbers(e):

    document.getElementById('results').innerHTML = "" #clear 

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    floordiv = first_number // second_number

    display(f'The floor division of {first_number} and {second_number} is {floordiv}', target='results')

def moduling_numbers(e):
    
    document.getElementById('results').innerHTML = "" #clear 

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    remainder= first_number % second_number

    display(f' When {first_number} is divided by {second_number}, its remainder is {remainder}', target='results')

def exponential_numbers(e):
    
    document.getElementById('results').innerHTML = "" #clear 

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    power= first_number ** second_number

    display(f' When {first_number} is raised to the power of {second_number} it results to {power}', target='results')
  
