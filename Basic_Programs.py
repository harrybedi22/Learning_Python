"""Max of Two Number"""

from re import L


def max_of_two_numbers(n1,n2):
    """Max of Two Numbers"""
    return max(n1,n2)

# call=max_of_two_numbers(2,4)
# print(call)

def fictorial_of_number(num):
    """Fictorial of number :Iterative Approch"""
    fic=1
    while num>0:
        fic=num*fic
        num-=1
    print(fic)

def fictorial(num):
    """Fictorial of number:Recursive approch"""
    return 1 if (num==0 or num==1) else num * fictorial(num-1);

def armstrong_numberr(num):
    org_num=num
    num_list=[]
    sum=0
    while num!=0:
        r=num%10
        num_list.append(r)
        num=num//10
    print(num_list)
    for number in num_list:
        sum=number**3+sum
    print(sum)
    print(num)
    if sum==org_num:
        print("Armstrong")
    else:
        print("Not armstrong")

def all_prime(num):
    flag=False
    
    for i in range(2,num):
        if num%i==0:
           flag=True
           break

    if flag==False:
        print("Prime")
    else:
        print("Not Prime")
    
def fibonacci(seq):
    num1=0
    num2=1
    for i in range(seq):
        fb=num1 + num2
        num1=num2
        num2=fb
        print(fb)

def ascivalue(char):
    print(ord(char))
call=ascivalue("5")