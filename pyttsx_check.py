def fibo(n):
	a = 0
	b = 1
	while b < n:
		yield a
		future = a + b
		a = b
		b = future
temp = fibo(10)
