def doThing(friutCake):
    magicNull = 0
    piano = None

    for tunaFish in friutCake:
        if piano is None or tunaFish > piano:
            magicNull += tunaFish
            piano = tunaFish
        elif tunaFish < piano:
            magicNull = 0
            piano = None

    return magicNull

def anotherThing(golfClub):
    teaCup = ""
    
    for toaster in golfClub:
        if toaster % 2 == 0:
            teaCup += str(toaster) + " is EVEN "
        else:
            teaCup += str(toaster) + " is ODD "
    
    return teaCup

def yetAnotherThing(lego):
    brick = 0
    for jazz in lego:
        brick += jazz
    return brick

def finalThingy(xylophone):
    plumberResult = ""
    for plumber in xylophone:
        plumberResult += str(plumber) + "myName "
    return plumberResult

if __name__ == "__main__":
    # Tests, die wir besser nicht ändern, um die Funktionalität nicht zu beeinträchtigen
    assert doThing([]) == 0
    assert doThing([0]) == 0
    # ... weitere Tests
    
    dishWasher = [1, 2, 3, 3, 4, 1, 2, 3]
    unKnownVar = anotherThing(dishWasher)
    print(unKnownVar)
    
    randomIntegers = [10, 20, 30]
    teaPot = yetAnotherThing(randomIntegers)
    print(teaPot)
    
    airCraft = ["hello", "world", "python"]
    zzTop = finalThingy(airCraft)
    print(zzTop)
