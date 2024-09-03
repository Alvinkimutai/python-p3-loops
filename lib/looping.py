#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    n = 11
    while n > 1:
        n-= 1
        print(n)
    if n==1 :
        print("Happy New Year!")
    pass

happy_new_year()

def square_integers(int_list):
    # code goes here!


    # squared_integers= list()
    # for elements in int_list:
    #     integers_squared = elements**2
    #     squared_integers.append(integers_squared)

    # return squared_integers
    sqr = [element**2 for element in int_list]
    return sqr
    pass
print(square_integers([1,3,5,7,9]))
def fizzbuzz():
    # code goes here!
    for num in range(1,101,1):
        if num%3 ==0 and num%5 !=0:
            print("Fizz")
        elif num%3 != 0 and num%5 == 0:
            print("Buzz")
        elif num%3 == 0 and num%5 == 0:
            print("FizzBuzz")
        else:
            print(num)

    pass
print(fizzbuzz())

