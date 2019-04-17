def URLlength(URL):  #2nd column
    if len(URL)<54:
        return -1
    else:
        return 1

def URLhavingsubdomain(URL): #8thcolumn
    for j in range(len(URL)-1):
        if URL[i]=="." and URL[i+1]==".":
            q=j;
            if q>2:
                return -1
            else:
                return 1
def HTTPStoken(URL): #13cloumn
    if "HTTP" in URL:
        return -1
    else:
        return 1
