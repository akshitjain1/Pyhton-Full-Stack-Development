# Write code to print the sum of odd numbers and product of even numbers up to a given number 'a'
a = int(input("Enter the number: "))
sum = 0
mul = 1
for i in range(1, a+1):
    if(i%2 != 0):
        sum += i
        print(i, " + ", end=" ")
    
print("=> ",sum)

for i in range(1, a+1):
    if(i%2 == 0):
        mul *= i
        print(i, " * ", end=" ")
    
print("=> ",mul)