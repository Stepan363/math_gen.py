import random


div_questions = 0
multiplication_ques = 0
common_factor = 10



def division():
	for i in range(div_questions):
		int1 = random.randint(2,10)
		int2 = random.randint(2,10)
		print(int1 * int2, "/", int2, "= ?")
division()

def common_factors():
	for i in range(common_factor):
		int3 = random.randint(1,50)
		print("common factor of:", int3
			)


common_factors()
