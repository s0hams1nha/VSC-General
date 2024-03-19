import sys
def mnm(p, i, j):
  if i==j:
    return 0
  else:
    _min=sys.maxsize
    for k in range(i, j):
      count=(mnm(p, i, k) + mnm(p,  k+1, j) + p[i-1]*p[j]*p[k])
      if count<_min:
        _min=count
  
  return _min

arr=[1,2,3,4,3]
n=len(arr)
print(mnm(arr, 1, n-1))