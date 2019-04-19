def nonstandardport(port): #11




def requestUrl(URL): #13 column
    if URL>=22 and URL<=61:
        return 1
    else:
        return 0
def anchor(URL): #14column
    if URL>=31 and URL<=67:
        return 1
    else:
        return 0
def SFH(sfh): #16column
    if sfh='':
        return 1
    else:
        return 0
def email: #17column
    mail=0
    if mail()==1:
        return 1
    else:
        return 0
def abnormal(URL): #18column
    hostname=''
    if URL==hostname:
        return 1
    else:
        return 0
def redirect(URL): #19column
    redirect=1
    if redirect>=2 and redirect<4:
        return 1
    else:
        return 0
def onmouseover(URL): #20colum
    



    
def rightclick(URL): #21column
    if event.button==2:
        return 1
    else:
        return 0
def popup(txt): #22column



def iframe(frame): #23
    frame=0
    if frame==1:
        return 1
    else:
        return 0
def ageofdomain(month): #24
     month = int(input('Enter the number to be converted: '))
    if month<6:
        return 1
    else:
        return 0
def dnsrecord(dns): #25
    if dns='':
        return 1
    else:
        return 0
def websitetraffic(rank): #26
    if rank>=100000:
        return 1
    else:
        return 0
def pagerank(prank): #27
    if prank<0.2:
        return 1
    else :
        return 0
def googleindex(index): #28



def numboflinks(link): #29
    if link>=0 and link<=2:
        return 1
    else:
        return 0
def statisticalreports(host): #30
