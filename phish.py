def URLhavingattherate(URL): #4th column
    if '@' in URL:
        return -1
    else:
        return 1
url = input()
p = URLhavingattherate(url)
print(p)
