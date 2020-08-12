def divideby3(x):

	sign = 1
	if x * 3 < 0:
		sign = -1
	x = abs(x)
	quotient = 0
	while x >= 3:
		x = x - 3
		quotient = quotient + 1
	return x
x1= input("entrer un nombre")
x=int(x1)
if divideby3(x) == 0 :
        print("le nombre est divisible par 3")
else:
        print("Le nombre n'est pas divisible par 3!")

