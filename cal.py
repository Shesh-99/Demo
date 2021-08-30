# dic ={1:"shesh",2:"giri",[a,b,c]:[1,2,3,4]}
# for x in dic:
#      print(dic[x])
#
# # dic ={1:"shesh",2:"giri"}
# # pop_e=dic.pop(1)
# # print(dic)

#Table_program
def table(n):
     return lambda a:a * n
n=int(input("enter the number"))
b=table(n)
for i in range(1,11):
     print(n,"X",i,"=",b(i))
