import random


div_questions = 0
mult_ques = 0
common_factor = 0
def multiplication():
	for i in range(mult_ques):
		int1 = random.randint(2,15)
		int2 = random.randint(2,15)
		print(int1 , "*", int2, "= ?")
		
		
	

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
