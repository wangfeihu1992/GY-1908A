a = [1,2,3,4,5,6,7,8,9,0]
a.append(12)
print(a)
a.insert(8,12)
print(a)
q=[1,2,3,4]
a.extend(q)
print(a)
print(q)

print(a.pop(-2))
print(a)
print(a.pop(7))
print(a)
a.remove(7)
print(a)
a.remove(12)
print(a)
a.remove(12)
print(a)
a[-5]=12
print(a)
print(a.index(6))
print(a)
a[a.index(1)]=6
print(a)











