# order=""

# for i in range (10):
#     a=input("what are you ordering")
#     while a !="end":
#         print(a)
#     break



# n1=int(input("what is the number?: "))

# if n1%3==0 and n1%5==0:
#   print("yes it is divisable by 3 and 5")
# else:
#   print("is isnt divisable by 3 and/or 5")


# v=int(input("how many visitors are there"))
# mv=int(input("max visitor?"))

# while True:
#     if v<mv:
#         v+=1
#         print(v)
#     elif v>=mv:
#         break




# order = ""

# while True:
#     user_input = input("Enter your order (type 'end' to finish): ")
    
#     if user_input == "end":
#         break
    
#     order += user_input + " "


# print("Customer's order:", order)



# count = 10

# while count >= 1:
#     print(count)
#     count -= 1
#     if count==5:
#         break
# else:
#     print("Happy New Year!")



import random
while True:
    a=random.randint(1,10)
    b=random.randint(1,10)
    quesans=int(input("what is"+str(a)+"+"+str(b)))
    if quesans!=(a+b):
        print("wrong")
    else:
        print("correct")