import re
# password="Saisasvs@3"
# pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
# result=re.match(pattern,password)
# if result:
#     print("Valid password")     
# else:
#     print("Invalid password")

# #url validation
# url="https://www.example.com"
# url_pattern=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
# result=re.match(url_pattern,url)
# if result:
#     print("Valid URL")
# else:
#     print("Invalid URL")
#exception handling

#ValueError:
# try:
#     num=int(input("enter a number"))
# except ValueError as e:
#     print(f"invalid input:{e}")

#2
#ZeroDivisionError:
try:
    num=100/0
except ZeroDivisionError as e:
    print(f"cannot divide by zero:{e}")

#3
#IndexError:
try:
    l=[1,2,3]
    print(l[3])
except IndexError as e:
    print(f"index out of range:{e}")

#4
#KeyError:
try:
    d={"name":"city"}
    print(d["age"])
except KeyError as e:
    print("key not found:",e)

#5
#AttributeError:
try:
    class Person:
        def __init__(self,name):
            self.name=name
    p=Person("John")
    print(p.age)
except AttributeError as e:
    print("attribute not found:",e)

#6
#TypeError:
try:
    num="10"
    result=num+5    
except TypeError as e:
    print("type error:",e)

#7
#file not found error:
try:
    with open("non_existent_file.txt","r") as f:
        content=f.read()
except FileNotFoundError as e:  
    print("file not found:",e)
#8
#ImportError:
try:
    import non_existent_module
except ImportError as e:
    print("import error:",e)
#9  
# RecursionError:
try:
    def recursive_function():
        return recursive_function()
    recursive_function()
except RecursionError as e: 
    print("recursion error:",e)

#10
#MemoryError:
try:   
    large_list = [1] * (10**10)  # Attempt to allocate a large list
except MemoryError as e:    
    print("memory error:",e)
#11 
#KeyboardInterrupt:
try:
    while True:
        pass  # Infinite loop
except KeyboardInterrupt:
    print("Keyboard interrupt occurred")
#12
#StopIteration: 
try:
    my_list = [1, 2, 3]
    iterator = iter(my_list)
    while True:
        item = next(iterator)   
        print(item)
except StopIteration:
    print("Iteration stopped")
#13
#OverflowError:
try:
    num = 10**1000  # Attempt to create a very large number
except OverflowError as e:
    print("overflow error:",e)

