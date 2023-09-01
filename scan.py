def funcA(resA):
    tmpA = 0
    aVal = None

    for elmA in resA:
        if aVal is None or elmA > aVal:
            tmpA += elmA
            aVal = elmA
        elif elmA < aVal:
            tmpA = 0
            aVal = None

    return tmpA

def doSomeSTB(strOut):
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

def SnTBV(concatStr):
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
    resB = doSomeSTB(lstA)
    print(resB)
    
    lstB = [10, 20, 30]
    calcTotal = sumFunc(lstB)
    print(calcTotal)
    
    lstTxt = ["hello", "world", "python"]
    resC = SnTBV(lstTxt)
    print(resC)
