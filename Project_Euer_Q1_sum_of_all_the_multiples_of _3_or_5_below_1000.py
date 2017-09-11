"""
Project Euler problem solutions using Python

by

Charanraj Thimmisetty
charanrajt@gmail.com

Q1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
def sum_of_int(n):
    """
    Returns the sum of 1+2+3+...+n
    """
    return n*(n+1)/2

max_multiple_of_3=int(999/3)*3; #3, 6, .... 999
sum_multiples_of_3=3*sum_of_int(max_multiple_of_3/3)#3(1+2+.....+333)

max_multiple_of_5=int(999/5)*5;
sum_multiples_of_5=5*sum_of_int(max_multiple_of_5/5)

max_multiple_of_15=int(999/15)*15;
sum_multiples_of_15=15*sum_of_int(max_multiple_of_15/15)

Ans=sum_multiples_of_3+sum_multiples_of_5-sum_multiples_of_15

print Ans


