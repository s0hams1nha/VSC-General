def maxprofit(n, w, p, c):
  pw=[]
  for i in range(n):
    pw.append(p[i] / w[i])

  for i in range(n-1):
    for j in range(n-i-1):
      if(pw[j]<pw[j+1]):
        pw[j], pw[j + 1] = pw[j + 1], pw[j]
        w[j], w[j + 1] = w[j + 1], w[j]
        p[j], p[j + 1] = p[j + 1], p[j]

  profit=0
  capcount=0
  for i in range(n):
    if capcount+w[i]<=c:
      profit+=p[i]
      capcount+=w[i]
    else:
      profit+=(c-capcount)*pw[i]
      break
  return round(profit, 2)
      
n = int(input())
w=[]
p=[]

for _ in range(n):
  w.append(int(input()))
for _ in range(n):
  p.append(int(input()))
c=int(input())

print(maxprofit(n, w, p, c))