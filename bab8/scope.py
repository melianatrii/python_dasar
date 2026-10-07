x = "global"
def tes():
    x = "lokal"     #hanya didalam tes()
    print(x)        #lokal
tes()
print(x)            #global