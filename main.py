import random


div_questions = 20
multiplication_ques = 0
common_factor = 10



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
	
	for i in range(common_factor):
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
print("ANSWERS")
print("")
print("")
print("")
#print(answers, "answers")
for i in answers:
	print(i)


