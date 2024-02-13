import random

#'''
answers = []
div_questions = 20
multiplication_ques = 0
factor_ques = 10
common_factors = 10
int1_iterate = []
int2_iterate = []
def common_factor():
	int1_iterate = []
	int2_iterate = []
	common_factor_answer = []
	for i in range(common_factors):
		int1 = random.randint(6,50)
		if int1%4 == 0:
			int2 = int1/4
		elif int1%3 == 0:
			int2 = int1/3
		elif int1%2 == 0:
			int2 = int1/2
		elif int1%1 == 0:
			int2 = int1*2
		print("common factor of:", min(round(int2), int1), ",",max(int1,int2))
		for i in range(int1):
			i+=1
			if int1 %i == 0:
				int1_iterate.append(round(int1/i))
		for i in range(int(int2)):
			i+=1
			if int2 %i == 0:
				int2_iterate.append(round(int2/i))
		if  int1_iterate> int2_iterate:
			biggest = int1_iterate
		else:
			biggest = int2_iterate

		zambias = max(int2_iterate, int1_iterate)
		zambia = min(int2_iterate, int1_iterate)

		for j in range(len((max(int2_iterate, int1_iterate)))):
			to_check = biggest[j]
			for z in zambia:
				if z == to_check:
					common_factor_answer.append(to_check)
		print(int1_iterate)
		print(int2_iterate)


		boogazagga = "common factor answer for", min(round(int2), int1) ,max(int1,int2), "--->", common_factor_answer
		answers.append(boogazagga)
		common_factor_answer = []
		int1_iterate = []
		int2_iterate = []



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


#'''


'''
output ___________________________________________________________________>





common factor of: 23 , 46
[46, 23, 2, 1]
[23, 1]
common factor of: 9 , 36
[36, 18, 12, 9, 6, 4, 3, 2, 1]
[9, 3, 1]
common factor of: 11 , 33
[33, 11, 3, 1]
[11, 1]
common factor of: 5 , 15
[15, 5, 3, 1]
[5, 1]
common factor of: 9 , 27
[27, 9, 3, 1]
[9, 3, 1]
common factor of: 35 , 70
[35, 7, 5, 1]
[70, 35, 14, 10, 7, 5, 2, 1]
common factor of: 19 , 38
[38, 19, 2, 1]
[19, 1]
common factor of: 11 , 33
[33, 11, 3, 1]
[11, 1]
common factor of: 41 , 82
[41, 1]
[82, 41, 2, 1]
common factor of: 11 , 44
[44, 22, 11, 4, 2, 1]
[11, 1]
36 / 4 = ?
63 / 9 = ?
25 / 5 = ?
72 / 8 = ?
30 / 6 = ?
49 / 7 = ?
56 / 8 = ?
48 / 8 = ?
56 / 8 = ?
24 / 6 = ?
100 / 10 = ?
80 / 10 = ?
16 / 4 = ?
30 / 6 = ?
50 / 10 = ?
20 / 4 = ?
49 / 7 = ?
45 / 5 = ?
90 / 10 = ?
45 / 5 = ?
factor of: 35
factor of: 20
factor of: 30
factor of: 5
factor of: 34
factor of: 18
factor of: 47
factor of: 32
factor of: 6
factor of: 23
ANSWERS



('common factor answer for', 23, 46, '--->', [23, 1])
('common factor answer for', 9, 36, '--->', [9, 3, 1])
('common factor answer for', 11, 33, '--->', [11, 1])
('common factor answer for', 5, 15, '--->', [5, 1])
('common factor answer for', 9, 27, '--->', [9, 3, 1])
('common factor answer for', 35, 70, '--->', [35, 7, 5, 1])
('common factor answer for', 19, 38, '--->', [19, 1])
('common factor answer for', 11, 33, '--->', [11, 1])
('common factor answer for', 41, 82, '--->', [41, 1])
('common factor answer for', 11, 44, '--->', [11, 1])
['ANSWER FOR', 35, ':', 1, 5, 7, 35]


['ANSWER FOR', 20, ':', 1, 2, 4, 5, 10, 20]


['ANSWER FOR', 30, ':', 1, 2, 3, 5, 6, 10, 15, 30]


['ANSWER FOR', 5, ':', 1, 5]


['ANSWER FOR', 34, ':', 1, 2, 17, 34]


['ANSWER FOR', 18, ':', 1, 2, 3, 6, 9, 18]


['ANSWER FOR', 47, ':', 1, 47]


['ANSWER FOR', 32, ':', 1, 2, 4, 8, 16, 32]


['ANSWER FOR', 6, ':', 1, 2, 3, 6]


['ANSWER FOR', 23, ':', 1, 23]


[Finished in 202ms]
'''
