def solution(A):
    leftSum = A[0]
    rightSum =0
    for a in A[1:]:
        rightSum +=a
    minDifference = abs(leftSum - rightSum)
    for a in A[1:-1]:
        leftSum += a
        rightSum -= a
        minDifference = min(minDifference, abs(leftSum-rightSum))
    return minDifference
