name1= 'Alex'
height_m1 = 1.83
weight_kg1= 91

name2='Bob'
height_m2=1.70
weight_kg2= 70

name3='Charlie'
height_m3= 1.50
weight_kg3= 50

name4='David'
height_m4=  1.45	
weight_kg4= 50



def BMI_Calculator(name,height_m,weight_kg):
			bmi=weight_kg / (height_m ** 2)
			print("BMI:  ")
			print(bmi)
			if bmi < 25:
				return name + " is not overweight"
			else:
				return name+" is overweight"

result1 = BMI_Calculator(name1,height_m1,weight_kg1)
print(result1) 

result2 = BMI_Calculator(name2,height_m2,weight_kg2)
print (result2) 

result3 = BMI_Calculator(name3,height_m3,weight_kg3)
print (result3) 

result4	= BMI_Calculator(name4,height_m4,weight_kg4)
print (result4) 

