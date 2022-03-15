import math

def run(bp, pp, pmax):
  k = 0
  min_total = 0
  while min_total <= pmax:
    min_total = math.inf
    for right in range(0, len(bp)-k):
      boostingPower = max(bp[right:right+k+1])
      processingPower = (k+1)*sum(pp[right:right+k+1])
      total = boostingPower + processingPower
      min_total = min(min_total, boostingPower + processingPower)
    # print(k, min_total, pmax)
    k += 1

  print("answer is " + str(k-2))
  return k-2

def runbs(bp, pp, pmax):
  k = 0
  min_total = 0
  left = 0
  right = len(bp) - 1

  while left < right:
    # set k to mid
    k = (right - left) // 2
    print(left, right, k)

    # calculate powers
    min_total = math.inf
    for right in range(0, len(bp)-k):
      boostingPower = max(bp[right:right+k+1])
      processingPower = (k+1)*sum(pp[right:right+k+1])
      total = boostingPower + processingPower
      min_total = min(min_total, boostingPower + processingPower)
    print(k, min_total, pmax)

    # update k
    if min_total < pmax:
      left = k + 1
    else:
      right = k - 1

  print("answer is " + str(k))
  return k

if __name__ == '__main__':
  boostingPower =   [3,6,1,3,4,3,4,6,6,3,7,3,6,4,1,3]
  processingPower = [2,1,3,4,5,5,6,5,1,4,2,3,5,1,2,3]
  powerMax = 500

  print(run(boostingPower, processingPower, powerMax))
  print(runbs(boostingPower, processingPower, powerMax))
"""
  k = 3 -> 0,1,2
  max(bp[0],bp[1],bp[2]) + ( pp[0]+pp[1]+pp[2] ) * k
  max(3,6,1) + 2+1+3 = 6 + 6*3 = 24

  find minimum k
"""