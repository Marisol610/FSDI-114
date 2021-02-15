#Memoized Dynamic Programming Algorithm
#can be applied to any recursive algorithm
memo ={}
fib (n):
if n in memo:return memo[n]
if n <= 2: f=1
else : 
    f=fib(n-1) + fib(n-2)
    memo[n]=f
return f 


def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))