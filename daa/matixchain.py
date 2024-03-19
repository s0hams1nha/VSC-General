import sys
def mnm(p, i, j):
  if i==j:
    return 0
  _min=sys.maxsize
  for k in range(i, j):
    count=(mnm(p, i, k) + mnm(p, k+1, j) + p[i-1]*p[j]*p[k])
    if _min>count:
      _min=count
  return _min


n=int(input("Enter number of inputs: "))
arr=[]
for i in range(n):
  arr.append(int(input("Enter array element: ")))
print(mnm(arr, 1, n-1))