import random


div_questions = 20
multiplication_ques = 0
factor_ques = 10
common_factors = 10
def common_factor():
	for i in range(common_factors):
		int1 = random.randint(6,50)
		print("common factor of:", int1, ",",int1*2)
common_factor()

def mult_ques():


	for z in range(multiplication_ques):
		int1 = random.randint(4,11)
		int2 = random.randint(4,11)
		print(int1, "*", int2, "= ?")

def division():

	if div_questions > 0:
		for i in range(div_questions):
			int1 = random.randint(4,10)
			int2 = random.randint(4,10)
			
			#print(div_questions)
			print(int1 * int2, "/", int2, "= ?")
			if div_questions <= 0:
				break;
if div_questions > 0:
	division()


answers = []
def factors():
	answer_add = []
	
	for i in range(factor_ques):
		num = 0
		int3 = random.randint(1,50)
		print("factor of:", int3
			)
		answer_add.append("ANSWER FOR")
		answer_add.append(int3)
		answer_add.append(":")
		while num <= int3:
			num += 1
			#print((int3/num).is_integer())
			#print(int3/num)
			if (int3/num).is_integer() == True:
				answer_add.append(num)

		if answer_add != []:
			answers.append(answer_add)
			answers.append("")
			answers.append("")
		answer_add = []
factors()
mult_ques()
print("ANSWERS")
print("")
print("")
print("")
#print(answers, "answers")
for i in answers:
	print(i)


for i in answers:
	print(i)


