
def countA(w):
    letterA=0
    for i in range(0,len(w)):
        if w[i] =="a":
           letterA=letterA+1
    return(letterA)

countA("rat")
