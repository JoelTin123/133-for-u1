import math #coz yea q7
# Q1
def q1():
    farenheight = float(input('Enter temperature in fahrenheit: '))
    centigrade = 5/9 * (farenheight-32)
    print('Temperature in centigrade: ', centigrade)
def q1heranswer():
    f = float(input('Enter temperature in fahrenheit: '))
    c = 5 / 9 * (f - 32)
    print(c)
    print('temperature: ', c)
    print(f'Temperature in celsius = {round(c)}, {round(c, 3)}, {c:.2f}') 
    # the above line is to round the result to nearest integer, 3dp, and 2dp respectively

#q2 
def q2():
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    n3 = int(input('Enter third number: '))
    sum = n1+n2+n3
    average = sum/3
    print('The sum of the 3 numbers is : ', sum)
    print('The average of the 3 numbers is : ', average)
def q2heranswer():
    a, b, c = 1, 2, 3 # assigning 1 to A, 2 to B, 3 to C
    sum0 = a + b + c
    ave = sum0/3
    print(sum0, ave)

#q3
def q3():
    threedigit = input('Enter a 3 digit integer: ')
    sum = 0
    product = 1
    for i in range(len(threedigit)):
        sum += int(threedigit[i])
        product *= int(threedigit[i])
    print(f'The sum of the digits is {sum}')
    print(f'The product of the digits is {product}')
# ------------------------------------------------------
def q3heranswer():
    threedigit = int(input('Enter a 3 digit integer: '))
    hunrdreds = threedigit // 100 # divide by 100 and remove the decimal
    tens = (threedigit-hunrdreds*100) // 10 # minus the hundred then same thing as the above
    ones = threedigit - (hunrdreds * 100) - (tens*10) # minus everything
    sum = hunrdreds + tens + ones
    product = hunrdreds * tens * ones
    print(f'Sum of digits = {sum}')
    print(f'Product of digits = {product}')
    print('Sum of digits = ', sum)
    print('Product of digits = ', product)
#-----------------------------------------------------------

#q4 (similiar to q3)
def q4():
    seconds = int(input('Enter time in seconds: '))
    hours = seconds // 3600
    minutes = (seconds-(hours * 3600)) // 60
    remainseconds = seconds - (hours * 3600) - (minutes * 60)
    print(f'The output in hours, minutes and seconds is: {hours} hour, {minutes} minute, {remainseconds} seconds')

def q4heranswer():
    n = int(input('Enter one integer number refers to seconds: '))
    hour = n // 3600
    minute = (n - (hour * 3600)) // 60
    second = n - (minute * 60) - (hour * 3600)
    print(hour, ' hr, ', minute, ' min and ', second, ' sec.')
    print(f'{hour} hr, {minute} min and {second} sec.')

#q5 (same as the above)
def q5():
    change = int(input('Enter change: '))
    change_50 = change // 50 
    change_10 = (change - change_50 * 50) // 10
    change_5 = (change - (change_50 * 50) - (change_10* 10)) // 5
    change_1 = (change - (change_50 * 50) - (change_10* 10) - (change_5* 5)) 
    print(f'50 cent: {change_50}')
    print(f'10 cent: {change_10}')
    print(f'5 cent: {change_5}')
    print(f'1 cent: {change_1}')
def q5heranswer():
    n = int(input('Enter change (<1 dollar): '))
    n_50 = n // 50
    n_10 = (n - n_50 * 50) // 10
    n_5 = (n - n_50 * 50 - n_10 * 10) // 5
    n_1 = n - n_50 * 50 - n_10 * 10 - n_5 * 5
    print('50 cent: ', n_50)
    print('10 cent: ', n_10)
    print('5 cent: ', n_5)
    print('1 cent: ', n_1)


#q6 (her answer is weird but yea use)
'''
Idk how service charge and gst works but yea is just math and 
step by step
'''
def q6():
    cost = float(input('Enter mean amount ($): '))
    discount = cost * 0.5 
    servicecharge = 0.1 * (cost -discount) 
    totalaftersc = cost - discount + servicecharge 
    gst = 0.07 * totalaftersc
    finaltotal = cost -discount+ servicecharge+ gst
    print('Receipt')
    print(f'Cost of meal: ${cost:.2f}')
    print(f'50% discount: ${discount:.2f}')
    print(f'Service charge: ${servicecharge:.2f}')
    print(f'GST: ${gst:.2f}')
    print(f'Total amount: ${finaltotal:.2f}')
def q6heranswer():
    n = float(input('Enter meal amount ($): '))
    discount = n * 0.5
    service = discount * 0.1
    gst = (discount + service) * 0.07
    total = discount + service + gst
    print('Receipt')
    print(f'Cost of meal: {n}')
    print(f'50% discount: {discount:.2f}')
    print(f'Service charge: {service:.2f}')

#q7 (she got no answer)
def q7():
    # Quite simple follow formula in qn, only part is the math module
    side1 = float(input('Enter first side: '))
    side2 = float(input('Enter second side: '))
    side3 = float(input('Enter third side: '))
    semiperi = 0.5 * (side1 + side2 + side3) 
    area = math.sqrt(semiperi*(semiperi - side1)*(semiperi-side2)*(semiperi-side3))
    print(f'Area is {area}')

#q8 (she got no answer)
def q8():
    loan_amount = float(input('Enter loan amount: ')) #ig loan can be float
    duration_in_years = int(input('Enter num years: ')) # number of years definitely is integer
    interest_rate = int(input('Enter interest rate: ')) # this i not sure maybe can be float
    compound_int = loan_amount * math.pow((1 + (interest_rate / 100)), duration_in_years)
    print(compound_int)

#q9 (i use her answer HAHA)
def q9():
    h = int(input('Enter current hr: '))
    m = int(input('Enter current min: '))
    s = int(input('Enter current sec: '))
    print(f'Clock time is {h:0=2d}:{m:0=2d}:{s:0=2d}') # making hour, min, second to 2 digits
    new_s = (s + 1) % 60 # getting remainer since if is 59 seconds, add 1 will be 60, so answer is 0
    new_m = (m + ((s + 1) // 60)) % 60
    new_h = (h + ((m + ((s + 1) // 60)) // 60)) % 24
    print(f'After 1 second, the time is {new_h:0=2d}:{new_m:0=2d}:{new_s:0=2d}')
q9()
'''
Basically the part where after 1 second is added:
The complicated formula is only for when is 59 seconds, 59 mins,
idk how explain in words
'''
