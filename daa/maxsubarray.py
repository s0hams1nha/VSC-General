x=[-2, -5, 6, -2, -3, 1, 5, -6]
continuossum=x[0]
maxsum=x[0]
for i in range(1,7):
  continuossum=max(x[i], continuossum+x[i])
  maxsum=max(continuossum, maxsum)
print(maxsum)