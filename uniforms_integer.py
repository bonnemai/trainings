# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here
  n=4 # TODO: change to 12
  n=len(str(B))+1
  uniforms=[]
  for i in range(1, n): 
    for j in range(10):
      uniform=0
      for k in range(i): 
        uniform+=j*10**k
      uniforms.append(uniform)
  print(uniforms)
  results=0
  for i in range(A,B+1):
    if i in uniforms:
      results+=1
  return results

tests=[
    (75, 300, 5)
]
for (A, B, expected_results) in tests:
    res=getUniformIntegerCountInInterval(A, B)
    print(res==expected_results, A, B)