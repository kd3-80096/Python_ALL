samplearray=([2,5,0,4,2,2,5,6,8,90,110,1456,1,43,2])

def findbiggestnumber(samplearray):
    biggestnumber = samplearray[0]
    for i in range (1,len(samplearray)):
        if samplearray[i]>biggestnumber:
            biggestnumber = samplearray[i]
    print(biggestnumber)

findbiggestnumber(samplearray)

