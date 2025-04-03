# str="hii,Hope you  ARE mgg doing great"
# print(len(str))
# print(str.upper())
# print(str.lower())
# print(str.strip())#used to remove the blank space front and back
# print(str.format())
# print(str.count("g"))
# print(str.replace("h","u"))
# #print(str.index("e"))
# print(str.find("e"))
# print(str.split())#used to split the string into list of words
# print(str.isascii())#used to check whether the string is ascii or not
# print(str.isalpha())#used to check whether the string is alphabetic or not
# print(str.isalnum())#used to check whether the string is alphanumeric or not


# #list methods
# fruits=["banana","orange","apple","kiwi"]
# print(fruits.append("mango"))
# print(fruits.sort())


# num=int(input("emter num:"))
# if num>89 and num<=100:
#     print("grad a")
# elif num>=70 and num<=80:
#     print("grade b")
# elif num>=60 and num<70:
#     print("grad c")
# else:
#     print("fail")
    

#rev a string
# str="hello how are you"
# print(str[::-1])
#rev a string using for loop
# str="haaah"
# rev_str=""
# for i in str:
#    r=i+rev_str
# if(str==rev_str):
#     print("string is palindrome")
# else:
#     print("string is not palindrome")


# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# number=int(input("enter a number:"))
# if is_prime(number):
#     print("isprime")
# else:
#     print("not prime")


# def fibinacci(n):
#     a,b=0,1
#     print(a,end=" ")
#     print(b,end=" ")
#     for i in range(2,n):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
#     print()
# num=int(input("enter a number:"))
# fibinacci(num)


# n=int(input("enter num"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")

# n=int(input("enter num"))
# for i in range(1,n):
#     if n%i==0:
#         print("not prime")
#         break
        
#     else:
#         print("prime")

# n=int(input("enter num:"))
# for i in range(1,n):
#     if(i%2==0):
#         print("@")
#     else:
#         print(i)


# c=[1,2,3,4,5]
# for i in range(0,len(c)):
#     c[i]=c[i]*c[i]
# print(c)


dict1={"name":"jexson","age":55,"place":"kerala"}
def ret_val(key):
    if key in dict1:
        return dict1[key]
    else:
        return "not present"
user_key=input("enter key:")
ret_val(user_key)
print(ret_val(user_key))



