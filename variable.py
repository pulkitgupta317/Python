import sys

print(sys.version)

myNumber = 3
print(type(myNumber))

myNumber = "abcde"
print(type(myNumber))

print("Hi", 'Pulkit','this', 'merlin', 'what are you doing',sep='.', end=',');

print('\nWelcome\nto\npython\nprogramming');

print(2+3)

print('2+3')

x = 1.32132
print('x is %.2f' %x)

boys = 86.44
girls = 13.56
print('Girls = %.2f%%, Boys = %.2f%%' %(girls, boys))

# age = input('Enter your age')
# age = int(age)
# print(age, type(age))

age = eval(input('enter your age'))
print(type(age), age)