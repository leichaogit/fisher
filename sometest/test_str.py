a = ["10",'2']
sorted(a,key=lambda o:(o[0],len(o)))
print(a)
print(''.join(a))