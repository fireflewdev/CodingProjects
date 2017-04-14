import math

side_input
if (decision_1 == "A" and decision_2 == "B") or (decision_1 == "B" and decision_2 == "A"):
	A_and_B
elif (decision_1 == "A" and decision_2 == "C") or (decision_1 == "C" and decision_2 == "A"):
	A_and_C
elif  (decision_1 == "B" and decision_2 == "C") or (decision_1 == "C" and decision_2 == "B"):
	B_and_C
else:
	print("Error. Please restart the program. If problem persists, please contact the developer")










#EVERYTHING BELOW ARE FUNCTIONS
def side_input():
	decision_1 = input("What is one side/angle you are utilizing (A, B, C): ")
	decision_1 = input("What is the other side/angle you are utilizing (A, B, C): ")
#***These Functions are the initial functions that are going to be called***
def A_and_B():
	side_angle = input("What are we looking for:'Side' or 'Angle('Case Sensitive)?: ")
	if side_angle == "Side":
		A_B_Side
	else:
		A_B_Angle
def A_and_C():
	side_angle = input("What are we looking for:'Side' or 'Angle('Case Sensitive)?: ")
	if side_angle == "Side":
		A_C_Side
	else:
		A_C_Angle
def B_and_C():
	side_angle = input("What are we looking for:'Side' or 'Angle('Case Sensitive)?: ")
	if side_angle == "Side":
		B_C_Side
	else:
		B_C_Angle

#***These functions will be furthering the initial functions***

def A_B_Side():
	what_side = input("What side are you solving for(A or B): ")
	if what_side == "A":
		#Run Function
	else:
		#Run function
def A_C_Side():
	what_side = input("What side are you solving for(A or C): ")
	if what_side == "A":
		#Run Function
	else:
		#Run function
def B_C_Side():
	what_side = input("What side are you solving for(B or C): ")
	if what_side == "B":
		#Run Function
	else:
		#Run function

#ANGLES

def A_B_Angle():
	what_angle = input("What angle are you solving for(A or B): ")
	if what_angle == "A":
		#Run Function
	else:
		#Run function
def A_C_Angle():
	what_angle = input("What angle are you solving for(A or C): ")
	if what_angle == "A":
		#Run Function
	else:
		#Run function
def B_C_Angle():
	what_angle = input("What angle are you solving for(B or C): ")
	if what_angle == "B":
		#Run Function
	else:
		#Run function

#Side Calculations
def A_B_SideA():
	side_B = int(input("Please enter the value of side B: "))
	angle_A_input = int(input("Please enter the value of angle A: "))
	angle_B_input = int(input("Please enter the value of angle B: "))
	sin_A = math.sin(math.radians(angle_A_input))
	sin_B = math.sin(math.radians(angle_B_input))
	side_A = (side_B*sin_A)/sin_B
	statement = "The value of side A is: %s" %(side_A)
	print(statement)

def A_B_SideB():
	side_A = int(input("Please enter the value of side A: "))
	angle_A_input = int(input("Please enter the value of angle A: "))
	angle_B_input = int(input("Please enter the value of angle B: "))
	sin_A = math.sin(math.radians(angle_A_input))
	sin_B = math.sin(math.radians(angle_B_input))
	side_B = (side_A*sin_B)/sin_A
	statement = "The value of side A is: %s" %(side_B)
	print(statement)

def A_C_SideA():
	side_C = int(input("Please enter the value of side C: "))
	angle_A_input = int(input("Please enter the value of angle A: "))
	angle_C_input = int(input("Please enter the value of angle C: "))
	sin_A = math.sin(math.radians(angle_A_input))
	sin_C = math.sin(math.radians(angle_C_input))
	side_A = (side_C*sin_A)/sin_C
	statement = "The value of side A is: %s" %(side_A)
	print(statement)

def A_C_SideC():
	side_A = int(input("Please enter the value of side A: "))
	angle_A_input = int(input("Please enter the value of angle A: "))
	angle_C_input = int(input("Please enter the value of angle C: "))
	sin_A = math.sin(math.radians(angle_A_input))
	sin_C = math.sin(math.radians(angle_C_input))
	side_C = (side_A*sin_C)/sin_A
	statement = "The value of side A is: %s" %(side_C)
	print(statement)

def B_C_SideB():
	side_C = int(input("Please enter the value of side C: "))
	angle_C_input = int(input("Please enter the value of angle C: "))
	angle_B_input = int(input("Please enter the value of angle B: "))
	sin_C = math.sin(math.radians(angle_C_input))
	sin_B = math.sin(math.radians(angle_B_input))
	side_B = (side_C*sin_B)/sin_C
	statement = "The value of side A is: %s" %(side_B)
	print(statement)

def B_C_SideC():
	side_B = int(input("Please enter the value of side B: "))
	angle_C_input = int(input("Please enter the value of angle C: "))
	angle_B_input = int(input("Please enter the value of angle B: "))
	sin_C = math.sin(math.radians(angle_C_input))
	sin_B = math.sin(math.radians(angle_B_input))
	side_C = (side_B*sin_C)/sin_C
	statement = "The value of side A is: %s" %(side_C)
	print(statement)

#Angle Calculations
def A_B_AngleA():#Not Done

def A_B_AngleB():#Not Done

def A_C_AngleA():#Not Done

def A_C_AngleC():#Not Done

def B_C_AngleB():#Not Done

def B_C_AngleC():#Not Done


