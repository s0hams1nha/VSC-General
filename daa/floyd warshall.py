def floyd(a, n):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        a[i][j]=min(a[i][j], a[i][k] + a[k][j])
  return a

x=float('inf')
a=[[0, 8, x, 1], [x, 0, 1, x], [4, x, 0, x], [x, 2, 9, 0]]

def printfloyd(a, n):
  for i in range(n):
    for j in range(n):
      print(a[i][j], end=" ")
    print()

printfloyd(floyd(a, 4), 4)