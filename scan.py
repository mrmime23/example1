def funcA(resA):
    tmpA = 0
    highVal = None

    for elmA in resA:
        if highVal is None or elmA > highVal:
            tmpA += elmA
            highVal = elmA
        elif elmA < highVal:
            tmpA = 0
            highVal = None

    return tmpA

def funcB(strOut):
    output = ""
    
    for valB in strOut:
        if valB % 2 == 0:
            output += str(valB) + " is EVEN "
        else:
            output += str(valB) + " is ODD "
    
    return output

def sumFunc(totalSum):
    sumVal = 0
    for num in totalSum:
        sumVal += num
    return sumVal

def funcC(concatStr):
    finalStr = ""
    for txt in concatStr:
        finalStr += str(txt) + "myName "
    return finalStr

if __name__ == "__main__":
    # Tests sind unverändert
    assert funcA([]) == 0
    assert funcA([0]) == 0
    # ... weitere Tests
    
    lstA = [1, 2, 3, 3, 4, 1, 2, 3]
    resB = funcB(lstA)
    print(resB)
    
    lstB = [10, 20, 30]
    calcTotal = sumFunc(lstB)
    print(calcTotal)
    
    lstTxt = ["hello", "world", "python"]
    resC = funcC(lstTxt)
    print(resC)
