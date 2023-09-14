"""300 children's code lessons"""

# Exercise 1
# Check type value is number or string or float.

def check_type():
    user_input = input('ex1. Enter your value: ')
    print('\n')

    try:
        val = int(user_input)
        print('Type your value is number, val = ', val)
    except ValueError:
        try:
            val = float(user_input)
            print('Type your value is float, val = ', val)
        except ValueError:
            print('Type your value is string')

        '''Use function isdigit()
        user_input = input('ex1. Enter your value: ')
        print('\n')

        if user_input.isdigit():
            print('Type your value is number')
        else:
            print('Type your value is string')
        '''



# Exercise 2
# Cal sum S(n) = 1 + 2 + 3 + .. + n

def sum():
    n = int(input('ex2. Enter value of n = '))
    S = 0

    ''' Loop 'for' '''
    for i in range(0, n + 1):
        S += i
        i -= 1

    ''' Loop 'while'
    while n >= 0:
        S += n
        n -= 1
    '''
    print('Sum S = ', S)


# Exercise 3
# Cal sum S(n) = 1^2 + 2^2 + 3^2 + .. + n^2

def sum_iSQuare():
    n = int(input('ex3. Enter value of n = '))
    S = 0

    for i in range(0, n+1):
        S += i**2
        n -= 1

    print('Sum S = ', S)

# Exercise 4
# Cal sum S(n) = 1 + 1/2 + 1/3 + .. + 1/n

def sum_divI():
    n = int(input('ex4. Enter value of n = '))
    S = 0

    for i in range(1, n+1):
        S += 1/i
        n -= 1

    print('Sum S = ', S)


# Exercise 5
# Cal sum S(n) = 1/2 + 1/4 + .. + 1/2n

def sum_div2I():
    n = int(input('ex5. Enter value of n = '))
    S = 0

    for i in range(1, n+1):
        S += 1/(2*i)
        n -= 1

    print('Sum S = ', S)

# Exercise 6
# Cal sum S(n) = 1/3 + 1/5  +.. + 1/(2n+1)
def sum_div2Ip1():
    n = int(input('ex6. Enter value of n = '))
    S = 0

    for i in range(1, n+1):
        S += 1/(2*i+1)
        n -= 1

    print('Sum S = ', S)

# Ex 7. List all divisors of positive integer n in Python

def list_div0():
    n = int(input('ex.7 Enter value of n, n = '))
    l = []

    for i in range(1, n+1):
        if n%i == 0:
            l.append(i)
    print('List all divisors of positive integer', n, ':', l)

# Ex 8. Sum all divisors of positive integer n in Python

def sum_div0():
    n = int(input('ex.8 Enter value of n, n = '))
    S = 0

    for i in range(1, n+1):
        if n%i == 0:
            S += i

    print('Sum all divisors of positive integer', n, ':', S)

# Ex 9. Find the largest odd divisor of a number in Python

def find_oddN():
    n = int(input('ex.9 Enter value of n, n = '))
    l = []

    for i in range(1, n+1):
        if n%i == 0:
            if i%2 != 0:
                l.append(i)

    print('The largest odd divisor of a number', n, ':', l[len(l)-1])

# Ex 10. Check if a number is a perfect number in Python

def check_perfectN():
    n = int(input('ex10. Enter your value: '))
    S = 0

    for i in range(1, n):
        if n%i == 0:
            S += i

    if S == n:
        print('n is perfect number')
    else:
        print('n is not perfect number')

# Ex 11. Check square numbers in Python

def check_squareN():
    n = int(input('ex11. Enter your value: '))
    c = 0

    for i in range(0, n+1):
        if i**2 == n:
            c = 1

    if c == 1:
        print(n, 'is square number')
    else:
        print(n, 'is not square number')

# Ex12. Check prime numbers in Python

def check_primeN():
    n = int(input('ex12. Enter your value: '))
    c = 0

    for i in range(1, n+1):
        if n%i == 0:
            c += 1
    if c == 2:
        print(n, 'is prime number')
    else:
        print(n, 'is not prime number')

# Ex13. Reverse a number in Python

def reserveN():
    n = int(input('ex13. Enter your value: '))
    li = []

    while(n!=0):
        print(n%10, end='')
        n = n // 10


def reserveNotherW():
    n = int(input('ex14. Enter your value: '))
    c = 0
    den = 1
    li = []

    # Count the number of digits
    n1 = n
    while(n1>10):
        n1 /= 10
        c += 1

    for i in range(1, c+1):
        den *= 10

    # update origin value
    den1 = den
    n1 = n

    while(c>=0):
        res = n//den
        li.append(res)
        n = n%den
        den /= 10
        c -= 1

    re = 0
    for i in reversed(li):
        re += i*den1
        den1 /= 10

    print('Print')
    while(re!=0):
        print('\t', int(re%10), end='\t')
        re = re // 10



# Ex 15. Solving one-unknown first-order equations in Python (ax + b = 0)

def firstOrder_x():
    a = int(input('ex15. Enter: a = '))
    b = int(input('Enter: b = '))
    if (a == 0):
        a = int(input('Re-enter: a = '))
    print('Hiden value of equation: x = ', (-b/a))

# Ex 16. Solve quadratic equations with one unknown in Python (ax^2 + bx + c = 0)
import math
def quadraticE_x():
    a = int(input('ex16.\nEnter: a = '))
    b = int(input('Enter: b = '))
    c = int(input('Enter: c = '))

    # Cal delta
    delta = b**2-(4*a*c)
    print('delta = ', delta)

    if delta<0:
        print('The equation has no solution')
    if delta==0:
        print('The equation has a double solution: x1 = x2 = ', -(b/2*a))
    else:
        print('The equation has two distinct solutions: x1 =', (-b+math.sqrt(delta))/(2*a), '& x2 = ', (-b-math.sqrt(delta))/(2*a))




#check_type()
#sum()
#sum_iSQuare()
#sum_div2I()
#sum_div2Ip1()
#list_div0()
#sum_div0()
#find_oddN()
#check_perfectN()
#check_squareN()
#check_primeN()
#reserveN()
#reserveNotherW()
#firstOrder_x()
#quadraticE_x()
