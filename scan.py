def expandedFunction(b):
    BNumber = 0
    qOne = None

    for x in b:
        if q is None or x > q:
            bNumber += x
            q = x
        elif x < q:
            bNumber = 0
            q = None

    return bNumber

def otherFunction(c):
    cResult = ""
    
    for y in c:
        if y % 2 == 0:
            cResult += str(y) + " is EVEN "
        else:
            cResult += str(y) + " is ODD "
    
    return cResult

def newFunction(d):
    Dsum = 0
    for z in d:
        dSum += z
    return dSum

def lastFunction(e):
    eResult = ""
    for w in e:
        eResult += str(w) + "myName "
    return eResult

if __name__ == "__main__":
    assert expandedFunction([]) == 0
    assert expandedFunction([0]) == 0
    assert expandedFunction([1]) == 1
    assert expandedFunction([1, 2, 3]) == 6
    assert expandedFunction([-1, 1]) == 0
    assert expandedFunction([1, 2, 3, 4]) == 10
    assert expandedFunction([1, 2, 3, -4]) == 0
    assert expandedFunction([-1]) == -1
    assert expandedFunction([1, 2, 3, 3]) == 6
    assert expandedFunction([3, 3, 3, 3, 3]) == 3
    assert expandedFunction([-1, -2, -3]) == -3
    assert expandedFunction([1000000]) == 1000000
    assert expandedFunction([1, 2, 3, 4, 1]) == 0
    assert expandedFunction([1, 2, 3, 4, 1, 2]) == 2
    assert expandedFunction([1, 3, 5, 42, 1]) == 0
    
    SampleList = [1, 2, 3, 3, 4, 1, 2, 3]
    processed_result = otherFunction(sample_list)
    print(processed_result)
    
    new_list = [10, 20, 30]
    sum_result = newFunction(new_list)
    print(sum_result)
    
    crazy_list = ["hello", "world", "python"]
    crazy_result = crazyFunction(crazy_list)
    print(crazy_result)
