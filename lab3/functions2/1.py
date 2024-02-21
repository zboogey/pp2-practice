n = int(input())
for i in range(n):
  a = int(input())
  b = int(input())
  c = int(input())
  if a+b == c or a+c == b or b+c==a:
    print("YES")
  else:
    print("NO")
