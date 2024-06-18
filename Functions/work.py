# functions are of four types
#  prositional arg, default arg, keyword arg, variablelength arg


'''def square(num):
    return num*num
data=[1,2,3,4,5,6,7]
res=[]
# syntax : map(function_object,iterable)
# iterable : list,tuple,etc
res=list(map(square,data))
print(res)
print(type(res))'''

# use of filter function

'''def Verify(age):
   return age>18
ages=[12,45,65,34,2,13,14]
# filter(function,iterable)
# function -> boolean
adults=list(filter( Verify,ages))
print(adults)'''

# use of reduce function
# function tool is a default package
from functools import reduce 
def sum_of_ele(a,b):
    return a+b

data=[1,2,3,4,5]
# reduce(function,data,initialValue)
res=reduce(sum_of_ele,data)
# res=reduce(sum_of_ele,data,10) "10+5"
print(res)


