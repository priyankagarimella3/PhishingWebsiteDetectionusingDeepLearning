def URLhavingattherate(URL): #4th column
    if '@' in URL:
        return -1
    else:
        return 1
def Redirectusingdoubleslash(URL):#5th column
    for i in range(len(URL)-1):
        if URL[i]=="/" and URL[i+1]=="/":
            p=i
    if p>7:
        return -1
    else:
        return 1
def prefixsuffix(URL): #6th column
    if '-' in URL:
         return -1
    else:
        return 1
url = input()
L=[]
for i in range(30):
    L+=[-1]
p = URLhavingattherate(url)
L[3]=p
k = Redirectusingdoubleslash(url)
L[4]=k
s = prefixsuffix(url)
L[5]=s

print(*L)
