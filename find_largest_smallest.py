#Find Largest and Smallest number
print 'Excercise 2'
max_num=-5
min_num=None

def largest_num(number, max_ret):
	if number > max_ret:
		max_ret=number
	return max_ret

def smallest_num(number2, min_ret):
	if min_ret is None:
		min_ret=number2
	elif number2 < min_ret:
		min_ret=number2
	return mi

while True:
	key=raw_input("Enter a number:")
	if key == 'done':
		print 'Largest number:', max_num
		print 'Smallest number:', min_num
		break
	try:
		num2=int(key)
	except:
		print'Invalid input'
		continue

	max_num=largest_num(num2, max_num)
	min_num=smallest_num(num2,min_num)