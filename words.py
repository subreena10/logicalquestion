# user1=int(input("number: "))
# user2=int(input("number: "))
# user3=int(input("number: "))
# if user1>user2:
#     print(user1,"greater")
# elif user2>user3:
#     print(user2,"greater")
# else:
#     print(user3,"graeter")


# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# i=4
# j=0
# while i<len(a):
#     if j==0:
#         a[i]=15
#         j=1
#     else:
#         a[i]=20
#         j=0
#     i+=5
# print(a)


# a=[[1,2,3,4],[5,6,7,8],[8,9,10]]
# list=[]
# i=0
# sum=0
# sum1=0
# sum2=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if j==0:
#             sum=sum+a[i][j]
#         elif j==1:
#             sum1=sum1+a[i][j]
#         elif j==2:
#             sum2=sum2+a[i][j]
#         elif j==3:
#             list.append(a[i][j])
#         j+=1
#     i+=1
# list.append(sum)
# list.append(sum1)
# list.append(sum2)
# print(list)


# i=100
# sum=0
# while i>0:
#     sum=sum+i
#     i-=1
# print(sum)


# list=["a","b","c","d","a","c","d","e","f","a","b"]
# i=0
# o=0
# while i<len(list):
#     if list[0]==list[i]:
#         k=(i)
#     elif list[1]==list[i]:
#         l=(i)
#     elif list[2]==list[i]:
#         m=(i)
#     elif list[3]==list[i]:
#         n=(i)
#     elif list[7]==list[i]:
#         o=(i)
#     elif list[8]==list[i]:
#         p=(i)
#     i+=1
# print(list[0],":",k,list[1],":",l,list[2],":",m,list[3],":",n,list[7],":",o,list[8],":",p)

# a=[1,2,3,4,5,6,7,8,9,10]
# c={}
# for i in a:
#     b={}
#     for j in range(0,i):
#         s=i*5
#         b.update({i:s})
#     c.update(b)
# print(c)

# a=["MIPCO"]
# c={}
# i=0
# while i <len(a):
#     j=0
#     b=a[i][j]
#     while j<len(a[i]):
#         # print(a[i][j])
#         c.update({b:j})
#         print(c)
#         j+=1
#     i+=1
#     # print(c)
#     # for j in range(6,11):
#         # b.update({i:j})
#         # print(b)




# a=12
# b=20.0
# c=4+2j
# a=float(a)
# print(type(a))
# b=int(b)
# print(type(b))
# a=float(a)
# print(a)
# c=str(c)
# print(c)
# a=complex(a)
# print(a)

# x = 10
# print("x is of type:",type(x))
# y = 10.6
# print("y is of type:",type(y))
# x = x + y
# print(x)
# print("x is of type:",type(x))

# d="20.0"
# c="3+4j"
# e=20
# b="29"
# e=complex(e)
# d=complex(d)
# b=complex(b)
# c=complex(c)
# f=b+c+d+e
# a="kavi"
# f=str(f)
# print(b+c+d+e)
# print(a+f)
