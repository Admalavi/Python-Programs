r = "hello akshata"
for i in r:
    print(i)

# Positive indexing of string
print(type(r))
print(r[1])
print(r[1:4])
print(r[2])

# Negative indexing of string
print(r[-1])
print(r[-3])
print(r[-1:-4:-2])
print(r[-1:-6:-2])

print(r.count('hello'))
print(r.index('akshata'))
print(r.lower())
print(r.upper())
print(r.replace('akshata','ankita'))
print(r.split(' ')) 
print(r.find('akshata'))