def Calculator():
    num1 = float(input('Enter your Number 1 :'))
    print('''This Calcultor can Calc 4 main operator 
    for Sum Enter +
    For Division Enter / 
    For Submission Enter -
    For Submission Enter *
    please Enter in down line:''')
    Operator = input('Enter your math opertor :')
    num2 = float(input('Enter your Number 2 :'))
    if Operator == '+':
        print('Result :', num1 + num2)
    if Operator == '-':
        print( 'Result :', num1 - num2)
    if Operator == '/':
        print('Result :', num1 / num2)
    if Operator == '*':
        print('Result : ','''
        ************''',num1 * num2)
    Again()        
def Again() :
    Num_again = input('''aya mikay ke dobare barname rub eshe 
    Y for Yes
    N for No | :''')
    if Num_again.upper() == 'Y' : 
        Calculator()
    elif Num_again.upper() == 'N' :
        print('Bye Bye')
    else : 
        Calculator()
Calculator()