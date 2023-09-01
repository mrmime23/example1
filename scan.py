def funca(resA):
    tmpa = 0
    aVal = None

    for elma in resA:
        if aVal is None or elma > aVal:
            tmpa += elma
            aVal = elma
        elif elma < aVal:
            tmpa = 0
            aVal = None

    return tmpa

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
    letz_str_my = ""
    for txt in concatStr:
        letz_str_my += str(txt) + "myName "
    return letz_str_my

if __name__ == "__main__":
    # Tests sind unverändert
    assert funca([]) == 0
    assert funca([0]) == 0
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
