def solution(N):
  """ Returns length of longest subarray of zeros between ones in binary representation of integer N"""
  longest_binary_gap = 0
  bin_N = bin(N)[2:] # without 0b at the beginning
  tmp = 0
  for i in bin_N:
    if i is '0':
      tmp = tmp + 1
    else: # i is 1 
      longest_binary_gap = max(longest_binary_gap, tmp)
      tmp = 0
  return longest_binary_gap

