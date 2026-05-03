# # import random
# # a=[]
# # for i in range(5):
# #     b=random.randint(1,6)
# #     a.append(b)
# #     print(b)

# # f=["apple", "bananana", "cherry"]
# # p=["$2", "$4", "$1"]

# # for i in range (len(f)):
# #     print(f[i]+ " costs " + p[i])


# itms=["bread", "poultry", "plutonium", "snacks"]
# stk=["8", "0", "237", "8"]
# stat=""
# for i in range (len(itms)):
#     if stk[i]==0:
#         stat="no stock"
#     elif int(stk[i])<9 and int(stk[i])>0:
#         stat="low stock"
#     else:
#         stat="well stock"

#     askd=input("check stock of item: ")
#     if askd in itms:
#         print("item" + str(itms[i]) +"// stock"+ str(stk[i])+"status" +str(stat[i]))

s=["pens","pencils", "erasers"]
c=input("how many more shld i buy")
for i in range (len(c)):
    item=input("what items should i buy")

print(s)