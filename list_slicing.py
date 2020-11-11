#Using List Slicing Method

list1=[]
string_even=""
string_odd=""
n=int(input("Enter number of names you want to enter in list:"))

for i in range(n):
    name=input("Enter name:")
    list1.append(name)
print("\nThe given list of names is:"+str(list1))

for i in list1[ : : 2]:
    string_even=string_even+i

for j in list1[1: : 2]:   
    string_odd=string_odd+j

print("\nString formed after joining even indices names:"+string_even)
print("\nString formed after joining even indices names:"+string_odd)
