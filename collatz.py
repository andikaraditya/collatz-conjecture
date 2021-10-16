n = int(input("Enter initial number: "))
i = 1;
n;
nmax = n;

while n > 2:
	i = i+1;
	if n%2 == 1:
		n = 3*n +1;
	else:
		n = n / 2;
	if n > nmax:
		nmax = n;

print("The number of iteration is: ", i)
print("The highest number is: ", nmax)