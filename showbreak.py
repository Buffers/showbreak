### showbreak.py
### COMSC 175, Skyler King
### January 22, 2025
### Time Spent = mins


from math import factorial

while __name__:
   N = int(input('Enter a nonnegative integer: '))
   try:
      fact = factorial(int(N))
      if int(N)>=0:
         break
   except:
      print('ValueError')
      print('N must be non-negative.')
   continue

M = factorial(N)
print('The factorial of user input %d! equals %d' %(N,M))

