# import random
# n=0
# while n!=4:
#     n=random.randint(1,6)
#     print(n)

# bal=1000

# while True:
#     ans=input("Would you like to withdraw, deposit, check your balance? Type end to exit")
#     if ans=="withdraw":
#         withmon=int(input("how much would you like to withdraw?"))
#         if withmon>bal:
#             print("you cannot withdraw more than u have.")
#         elif bal>withmon:
#             bal=bal-withmon
#             print("your balance is now "+ str(bal))
#     if ans=="deposit":
#         inmon=int(input("how much would u like to deposit?"))
#         bal=bal+inmon
#         print("your balance is now "+ str(bal))
#     if ans=="check my balance":
#         print (bal)
#     if ans=="end":
#         break
g=["apples", "carrots", "grape"]

# for i in range(4):
#     if g=="apples":
#             print("Apple: i need 5 of these")
#     if g=="carrots":
#             print("Apple: i need 3 of these")
#     if g=="grapes":
#             print("grapes:get the farmfresh brand")
# s=[]   
# while True:
#     t=input("what have u bought")
#     if u =="end":
#         break
#     t.append(u)

# g=""
# while True:
#     g=input("what is selling")
#     if g=="end":
#         break

# g=["apples" ,"bananas" ,"germany"]

# while True:
#     a=input("what are u looking for")
#     if a in g:
#         print("we have that")
#     else:
# #         print("we dont have that")


# import random
# for i in range (10):
#     a=(random.randint(1,9999))
#     print("the winner is #" + str(a) )

pzt=["pepperoni" ," mushrooms" ," pineapple", "uranium", " garlic", " More cheese", " tomatoes", " plutonium", " olives", " onion"]
print(pzt)
for i in range(len(pzt)):
    print(str(i+1) + pzt[i] )
while True:
    ys=input("what do you want")
    if ys=="end":
        print(ys)
        break


# for i in range(len(pzt)):
#     print(str(i+1) + pzt[i] )