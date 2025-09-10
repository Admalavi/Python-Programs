s = ('akshata','pragati','riya','sayali','tejal','preeti')
for i in s:
    print(i) #tuple printing


#positive indexing of tuple

print(type(s)) #type = tuple 
print(s[0])  
print(s[1:4])  #slicing
print(s[2])
print(s[2:4])

#negative indexing of tuple
print(s[-1])
print(s[-3])
print(s[-2])
print(s[-1:-4:2])
print(s[-1:-6:-2])

print(s.count('akshata'))
print(s.index('riya')) 
print(s.index('sayali'))
