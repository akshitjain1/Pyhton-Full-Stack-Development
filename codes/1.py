# Write a simple code to print the sum of prime numbers up to a given number 'a'
a = int(input("Enter the number: "))
sum = 0
for i in range(2, a+1):
    is_prime = True
    for j in range(2, int(i**0.5)+1):
        if(i%j ==0):
            is_primec = False
            break
    if is_prime:
        sum += i;
        print(i, " + ", end=" ")
print("=> ",sum)

