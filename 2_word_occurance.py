#Implement a Python function to count the occurrences of each word in a text.
s=input("enter a sentance\n").split()
d={}
for i in s:
  d[i]=s.count(i)
print(d)