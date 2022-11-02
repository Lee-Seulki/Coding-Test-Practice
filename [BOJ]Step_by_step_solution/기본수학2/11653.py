N = int(input())
m = 2
while N != 1:  # N과 m을 나눴을 때 몫이 1이 되면 멈춤.
  if N % m == 0: 
    print(m) 
    N = N // m
  else:
    m += 1