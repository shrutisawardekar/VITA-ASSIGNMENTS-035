1. Swap two variables using 3rd variable.
1.a
a=10
b=5
print(a,b)
a,b=b,a
print(a,b)

1.b
2nd solution
a=10
b=5
print("a is",a, "and b is ",b)
a=a+b
b=a-b
a=a-b
print("a is",a, "and b is ",b)

1.c
3rd solution
a=int(10)
b=int(5)
print("a is",a, "and b is ",b)
a=int(b/a)
b=int(a*b)
print("a is",a, "and b is ",b)

2.Accept the marks from the user and print corresponding grade
a. marks>=75 grade A
b. marks>=55 grade B
c. marks>=35 grade C
d. else fail

print("Enter marks:")
mks =int(input())
if (mks >= 75):
     print("grade A")
elif (mks >= 55):
     print("grade B")
elif (mks >= 35):
     print("grade C")
else:
       print("fail")

3. Accept a number from user -if it is divisible by 3 print "Three", if it is divisible by 7 print "Seven" and if it is divisble by both 3 & 7 print "Three-Seven".
print("Enter a number")
no=int(input())
if (no%3==0 and no%7==0):
     print("Three-seven")
elif(no%3==0):
     print("Three")
elif(no%7==0):
   print("Seven")

4. Accept principal amount, rate of interest and years of investment then find the simple interest.
p=float(input())
n=float(input())
r=float(input())
print("Enter principal amount",p,"rate of interest",r,"no of years",n)
si=(p*n*r)/100
print("simple interest",si)

5.Accept 10 numbers from the user and calculate their sum
1st solution
print("Enter numbers:")
c=0
sum=0
while(c!=10):
  n=int(input())
  sum=sum+n
  c+=1
print("sum is",sum)

2nd solution
print("Enter numbers:")
sum=0
for i in range (1,10):
       n=int(input())
       sum=sum+n
print("sum is",sum)

6.Accept a number from the user and find the factorial of the number.
print("Enter a number to find factorial:")
n=int(input())
sum=1
for i in range (1,n+1):
       sum=sum*i
print("Factorial of",n, "is",sum)

7.Accept 10 numbers from the user and count how many are positive,negative or zero.
print("Enter numbers:")
cp=0
cn=0
cz=0
for i in range (1,11):
       n=int(input())
       if (n>0):
              cp+=1
       elif (n<0):
              cn+=1
       else:
              cz+=1
print("Positive numbers are",cp,"Negative numbers are",cn,"Zeros are",cz)

8.Accept a number from the user and calculate the sum of digits of the number.
1st solution
print("Enter number")
n=int(input())
sum=0
while(n!=0):
       r=n%10
       sum=sum+r
       n=n//10
print("sum of digits is",sum)

2nd solution
sum=0
num=int(input("enter a number"))
while num>0:
    d=num%10
    print(d)
    num=num//10
    sum+=d
print(sum)

9.Accept a number from the user and reverse it. Accept a number from the user and check if it is palindrome or not.
print("Enter number")
n=int(input())
s=n
sum=0
rev=0
while(n!=0):
       r=n%10
       sum+=r
       n=n//10
       rev=rev*10+r
print("rev is",rev)
if rev==s:
       print("Palindrome")
else:
       print("Not palindrome")

10.Accept a number from the user and check if it is armstrong number or not.
sum=0
n=int(input("enter a number"))
s=n
while(n!=0):
       r=n%10
       sum=sum+(r*r*r)
       n=n//10
if sum==s:
       print("ARMSTRONG no")
else:
       print("Not ARMSTRONG")
