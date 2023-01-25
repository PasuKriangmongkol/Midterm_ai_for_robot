class AIChatBot:
	def showSubjectName(x):
		print(x)
	def showStudentYear(y):
		print(y)
	def calculator(z):
		print(z)
	def main(x,y,z):
		showSubjectName(x)
		showStudentYear(y)
		calculator(z)
print("subject")
subject = str(input())
print("year")
year = int(input())
print("cal")
op = str(input())
num = []

while True:
	x = str(input())
	if x != "":
		num.append(int(x))
	else:
		break
	
if op =="+":
	calc = sum(num)
elif op == "-":
	calc = sum(((-1)*num))
x,y,z = main(subject,year,calc)
