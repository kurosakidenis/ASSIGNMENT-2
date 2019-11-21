"""
Write a Python program to get the Fibonacci series between 0 to 50.
Note: The Fibonacci sequence is the series of numbers:
0, 1, 1, 2, 3, 5, 8, 13, 21,
Every next number is found by adding up the two numbers before it.
Expected Output: 1 1 2 3 5 8 13 21 34
"""

numbers = int (11)
# first two terms
q1, q2 = 0, 1
count = 0

# check if the number of terms is valid
if numbers <= 0:
   print("Please enter a positive integer")
elif numbers == 1:
   print("Fibonacci sequence upto",numbers,":")
   print(q1)
else:
   print("Fibonacci sequence:")
   while count < numbers:
       print(q1)
       qth = q1 + q2
       # updating values
       q1 = q2
       q2 = qth
       count += 1