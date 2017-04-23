def solution(A):
    completePermSum = ((len(A)+1)*(len(A)+2))/2 
    ASum = 0
    for el in A:
        ASum += el 
    permMissingElem = completePermSum - ASum
    return permMissingElem


