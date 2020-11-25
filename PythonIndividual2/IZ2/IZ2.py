def inputDict(SonParentDict):
    uniq = {}
    data = input("Введите данные в формате: отец сын (0 - окончание ввода)\n")
    while data != '0':
        dataList = data.split()
        if not dataList[0] in SonParentDict.keys():    
            SonParentDict[dataList[0]] = []
            SonParentDict[dataList[0]].append(dataList[1])
        else:
            SonParentDict[dataList[0]].append(dataList[1])
        if not dataList[0] in uniq.keys(): uniq[dataList[0]] = -1
        if not dataList[1] in uniq.keys(): uniq[dataList[1]] = -1
        data=input()
    return SonParentDict,uniq

def SearchBeg(SonParentDict, uniq):
    for i in uniq.keys():
        SearchRec(SonParentDict,uniq,i)
        print( uniq[i], ":", i)

def SearchRec(SonParentDict, uniq, elem):
    if uniq[elem] == -1:
        if not elem in SonParentDict.keys():
            uniq[elem] = 0
        else:
            sum = 0
            for j in SonParentDict[elem]:
                if uniq[j] == 0: sum+=1
                elif uniq[j] != -1: sum+=uniq[j] 
                else: 
                    SearchRec(SonParentDict,uniq,j)
                    sum+=uniq[j]+1
            uniq[elem]=sum

SonParentDict = {}
uniq = {}
SonParentDict,uniq = inputDict(SonParentDict)
SearchBeg(SonParentDict,uniq)