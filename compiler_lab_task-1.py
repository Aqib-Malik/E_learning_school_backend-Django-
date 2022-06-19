print("***********Q1************")
from collections import Counter
x = Counter({'a':5, 'b':3, 'c':7})
   sorted(x)
['a', 'b', 'c']
 sorted(x.items())
[('a', 5), ('b', 3), ('c', 7)]
 [(l,k) for k,l in sorted([(j,i) for i,j in x.items()])]
[('b', 3), ('a', 5), ('c', 7)]
[(l,k) for k,l in sorted([(j,i) for i,j in x.items()], reverse=True)]
[('c', 7), ('a', 5), ('b', 3)

print("***********Q2************")
w="w3resource"
dic={}
for x in w:
    if (x=='r' or x=='e'):
        dic[x]='2'
    else:
        dic[x]='1'
    

for v in dic:
    print(v,dic[v])

print("***************Q3***********")
dict1 = {1: ["ali", 21, 'CS'],
         2: ["aslam", 20, 'EE'],
         3: ["qasim", 21, 'Civil'],
         }
print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

for key, value in dict1.items():
    name, age, course = value
    print("{:<10} {:<10} {:<10}".format(name, age, course))

print("***************Q4***********")
vehicles = ("car","bike","truck","motorcycle","train")
x = sorted(vehicles)
print(x)


print("***********Q5*************")
dat={
    'item1':45.50,
    'item2':35,
    'item3':41.3,
    }
temp={}
for x in dat:
    if (dat[x]>dat['item2'] and dat[x]>dat['item3'] ):
      temp["item1"]=dat[x]
    if (dat[x]>dat['item2'] and dat[x]<dat['item1'] ):
      temp["item3"]=dat[x]
    if (dat[x]<dat['item1'] and dat[x]<dat['item3'] ):
      temp["item2"]=dat[x]

print(temp)

print("************Q6************")
my_dict = {'Math':81, 'Physics':83, 'Chemistry':87}
my_list = list(my_dict.items())
my_list.sort(key=lambda x: x[1], reverse= True)
print(my_list)

print("************Q7************")
print("************Q8************")
a=[1,4,6,8]
y=0
for x in a:
    y=y+x
print("sum=",y)


print("************Q9************")
a=[1,4,6,8]
y=1
for x in a:
    y=y*x
print("multily=",y)

print("************Q10************")
def compare(a):
    ctr = 0
    for i in a:
        if len(i) > 2 and i[0] == i[-1]:
            ctr+= 1
    return ctr

a = ['abc', 'xyz', 'aba', '1221', 'aaa', 'asdasdsada']
for i in a:
    z = compare(a)

print(z)

print("************Q11************")
def last(n): return n[-1]  
  
def sort_list_last(tuples):  
  return sorted(tuples, key=last)  
  
print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])) 

print("***********Q12************")
dataa=['red','green','white','black','pink','yellow']
temp=[]
p=0
for x in dataa:
    if (x!='red' and x!='pink' and x!='yellow'):
        temp.append(x)
    print(x)

print('Result',temp)

print("***************Q13***********")
def toString(List):
    return ''.join(List)
 
def permute(a, l, r):
    if l == r:
        print (toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)

            a[l], a[i] = a[i], a[l]
 
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

print("***************Q14***********")
a = [1, 2, 4]
b = [4, 5, 6]

temp = []
for item in a:
  if item not in b:
    temp.append(item)

print('Result:',temp)
    
print("**********Q15************")
a = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
b = {}

for item in a:
   if item in b:
      b[item] += 1
   else:
      b[item] = 1

print(b)

