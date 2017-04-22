def solution(A):
  result = 0
  for number in A:
    result = result ^ number #xor 
  return result
