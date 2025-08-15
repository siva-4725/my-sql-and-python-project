#1. Check if a number is prime or not
n=int(input("Enter a number:"))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

output_1:
Enter a number:10
Not Prime
output_2:
Enter a number:5
Prime


#2. Find the factorial of a given number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(n,"Factorial =", fact)

output:
Enter a number: 5
5 Factorial = 120


#3. print the fibanocci series upto n terms
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

output:
Enter number of terms: 10
0 1 1 2 3 5 8 13 21 34 


#4. Find the sum of digits of given numbers
n = int(input("Enter a number: "))
sum_digits = 0
while n > 0:
    sum_digits += n % 10   
    n //= 10
print("Sum of digits:", sum_digits)

output:
Enter a number: 123
Sum of digits: 6


#5. Reverse the digits of a given number
n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10      
    rev = rev * 10 + digit
    n //= 10            
print("Reversed number:", rev)

output:
Enter a number: 1234
Reversed number: 4321




