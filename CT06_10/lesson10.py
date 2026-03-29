print("Hello from lesson 10")

# import random
# num = random.randint(1,15)
# chance = 3
# ans=input("guess the random number!")
# for i in range(3):
#     if chance!=0:
#         if ans==num:
#             print("Thats it!")
#         else:
#             print("try again")
#             chance-=1
#     else:
#         print("you lost")




# ans=int(input("what is ur age"))
# if (ans>18):
#     print("you are an adult")
# elif (ans<12):
#     print("you are a kid")
# else:
#     print("you are a teen")


# temp=int(input("what is the temperature"))
# if temp<=20:
#     print("read a book")
# elif temp>25 and temp<31:
#     print("go play basketball")
# elif temp>20 and temp<24:
#     print("go cycling")
# else:
#     print("go swimming")






# ans=int(input("what is ur age"))
# if (ans<0):
#     print("age can't be negative")
# elif (ans>=18):
#     print("you can vote")
# else:
#     print("you can't vote")


# # Task 7: Random Number Guesser IV (nested if..else)
# Using nested 'if..else' conditions, code a Random Number Guesser
# Program that tells the user if their guess is higher or lower,
# and checks if they have guessed correctly. If not, the program
# will assume invalid input.

# Hint: You will need 3 separate 'if..else' conditions for this.

# 1. Generate a random integer betweeen 1 to 10
# 2. Ask the user to guess the number
# 3. If the correct number is greater than the guessed number:
#         If true, print "Higher!"
# 4. Within the 'else' statement of the 1st 'if' statement, use
#    another 'if' statement to check if the correct number is lower
#    than the guessed number:
#         If true, print "Lower!"
# 5. Within the 'else' statement of the 2nd 'if' statement, use
#    another 'if' statement to check if the correct number is the
#    same as the guessed number:
#         If true, print "You got it!"
# 6. Else:
#         Print "Invalid input!"


# import random
# num = random.randint(1,10)
# ans = int(input("whats ur guess? the random number is from 1 to 10!:"))
# for i in range(10):
#     if ans<num:
#         print("wrong,higher")
#     elif ans>num:
#         print("wrong,lower")
#     elif ans>10:
#         print("its from 1 to 10 try again")
#     else:
#         print("yup")


money=int(input("whats the amount of money you have?"))
if money>=150:
    print("you can buy a gaming keyboard")
elif money>=100 and money<150:
    print("you can buy GTA 6 which has surprisingly been released although for an absurd cost")
elif money>=50 and money<100:
    print("you can buy gaming mice")
elif money>=20 and money<50:
    print("you can buy gaming mouse pads")
else:
    print("you can only buy snacks broke boy")
