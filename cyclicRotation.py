# [3 8 9 7 6] k=2
# [7 6 3 8 9]


def solution(A,k):
  left = A[0:-k]
  right = A[-k:]
  return right + left

print solution([3, 8, 9, 7, 6], 2)
