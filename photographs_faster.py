
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Prefix 
  prefixPSum = [0]
  prefixBSum = [0]
  
  for c in C:
    if c == "P":
      prefixPSum.append(prefixPSum[-1] + 1)
    else:
      prefixPSum.append(prefixPSum[-1])
  for c in C:
    if c == "B":
      prefixBSum.append(prefixBSum[-1] + 1)
    else:
      prefixBSum.append(prefixBSum[-1])

  result = 0
  
  def bounded(x):
    return max(0, min(x, N))
  
  for i, c in enumerate(C):
    if c == "A":
      rightWindow = (bounded(i+X), bounded(i+Y+1))
      leftWindow = (bounded(i-Y), bounded(i-X+1))
      
      leftPs = prefixPSum[leftWindow[1]] - prefixPSum[leftWindow[0]]
      rightBs = prefixBSum[rightWindow[1]] - prefixBSum[rightWindow[0]]
      result += leftPs * rightBs
      
      rightPs = prefixPSum[rightWindow[1]] - prefixPSum[rightWindow[0]]
      leftBs = prefixBSum[leftWindow[1]] - prefixBSum[leftWindow[0]]
      result += leftBs * rightPs
        
  return result