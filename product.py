from functools import *
values=[10,20,30,40,50,60,70,80]
ans=reduce(lambda a,b:a*b,values)
print(ans)
