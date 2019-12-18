print("Enter a Number:  ")
value = int(input())
first = 0
second = 1
flag = 0
temp = 0
while temp <= value:
	temp = first + second
	first = second
	second = temp		
	if value == second or value == 0:
		flag = 1
		break
if flag == 1:
	print("Fibonacci")
else:
	print("Not Fibonacci")