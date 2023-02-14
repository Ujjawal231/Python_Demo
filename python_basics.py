# lst = [1,2,3,"abc","def"]

#lst.append(5)

#b = [2,3,45,89]
#lst.extend(b)
#print(lst)

# for index in range(0, len(lst)):
#     print(lst[index])
# print(dir(list))
# print(type(lst))

#Tuple
# repesent-->()
#Nature__> Immutable So we can append and delete the element at run time
#Accecable by Index
# print(dir(tuple))

# b = (7,8,9,10,232,232,'fgsdf')
# # print(b[0])
#
# for index in range(0, len(b)):
#     print(b[index], end=',')
#Set =
# Represented by-->{}
#It's contains Unique value

# set_A = {1,2,3,4,1,2,3}
# set_A.add(89)
# print(set_A)
#
#
# print(dir(set))
#
# for index, val in enumerate(set_A):
#     print(index, val)

#Dictonary
# represented by-->{}
#key, value
#key --> immutable in Nature,  Value--> Mutable in nature

# dict ={'a':1, 'Name': "rahul", "Educatio":["B-Tech", "Mtech"]}
#
# for key, value in dict.items():
#     print(key, value)
#
# a = "RAH"
#     # -4 -3 -2 -1
# print(a[::-1])
# a = 'rahulkumar'
# res = ''
# for i in range(len(a)-1, 0, -1):
#     res += a[i]
# print(res)

# while loop
# i = 4
# while i<=9:
#     print(i)
#     i =i+2


#ptyhon  Functions

'''def <Function_name>(<parmaeter>):
    logic---
    ----
    -----'''
def addteonum(a, b):
    sums = a + b
    return sums

# print(addteonum(1,4))

def eddevenlst(lst):
    ood_lst = []
    even_lst = []
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
        else:
            ood_lst.append(lst[i])
    return f"odd list:- {ood_lst}\neven list:- {even_lst}"

lst= [1, 23,45,6,8,9,6,3,254,12]
# print(eddevenlstt(lst))

nums = [1,2,1]
ans = []
ans = nums
for i in range(len(nums)):
    ans.append(nums[i])
print(ans)
