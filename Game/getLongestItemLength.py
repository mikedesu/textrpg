def getLongestItemLength(items):
    assert(items!=None)
    assert(len(items)>0)

    longestLen = 0
    for item in items:
        if len(item) > longestLen:
            longestLen = len(item)
    return longestLen 


