''''arr=[
    [1,2,3,4,3],
    [2,3,4,5,8],
    [3,4,5,6,2],
    [3,4,5,6,1]

]
arr.sort(key=lambda ele:ele[-1])
print(*arr,sep='\n')'''
# --------------------------------------------------------------------------------------------------------------------------------------------------

# sum of elements using lamda


'''from functools import reduce 
def sum_of_ele(a,b):
    return a+b

data=[1,2,3,4,5]

res=reduce(lambda a,b: a+b,data)
# res=reduce(sum_of_ele,data,10) "10+5"
print(res)'''
# --------------------------------------------------------------------------------------------------------------------------------------------------
# factorial
# function tool is a default package
from functools import reduce 
'''def sum_of_ele(a,b):
    return a+b

data=[1,2,3,4,5]
n=5
data=list(range(1,n+1))
res=reduce(lambda a,b: a*b,data)
# res=reduce(sum_of_ele,data,10) "10+5"
print(res)'''
\
# --------------------------------------------------------------------------------------------------------------------------------------------------


ages=[12,45,65,34,2,13,14]
# filter(function,iterable)
# function -> boolean
adults=list(filter( lambda age : age>18 ,ages))
print(adults)

# ---------------------------------------------------------------------------------------------------------------------------------------------------