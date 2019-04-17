def URLhavingattherate(URL): #4th column
    if '@' in URL:
        return -1
    else:
        return 1
p=URLhavingattherate(URL)
print(p)
