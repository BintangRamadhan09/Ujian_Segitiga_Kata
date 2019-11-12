# segitigaKata('Purwadhika')
# segitigaKata('Purwadhika Startup and Coding School @BSD')
# segitigaKata('kode')
# segitigaKata('kode python')
# segitigaKata('lintang')



k = ('kode python').replace (' ', '')
kList = list(k)


Con = []
for a in range(len(kList)):
    X = int((a*(a+1))/2)
    Con.append (X)
print (Con)

n=0
if len(kList) not in Con:
    print ('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
else:
    n= Con.index(len(kList))
def Fwd(n):   
    num = 0
    for i in range(0, n): 
        for j in range(0, i+1): 
            print(k[num], end=" ")  
            num = num + 1
        print("\r") 
def Bckwrd(n):   
    num = 0
    for i in range(n, 0, -1): 
        for j in range(1, i+1): 
            print(kList[num], end=" ")  
            num = num + 1
        print("\r") 
       
Fwd(n)
Bckwrd(n)