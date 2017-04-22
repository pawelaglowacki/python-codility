# [3 8 9 7 6] k=2
# [7 6 3 8 9]


def solution(A,k):
  try:
    k = k%len(A)
  except ZeroDivisionError: # to handle empty A array
    k = 0
  return A[-k:] + A[0:-k] #interchange left and right subarrays in A

