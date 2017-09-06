
#1)Create a function to identify the teperature when value of Fahrenheit and Celsius scale is equal

def TempCalculation(): # defile function
	for CelTemp in range(-250,250) : # provide a range of values to calculate the temprature 
		FrhTemp=1.8*CelTemp+32    # formula to convert Celsius to Fahrenheit
		if (FrhTemp==CelTemp):
			print( FrhTemp, "is the temperature where Fahrenheit and Celsius Scales meet.")

			




#2)Create a function to convert between Fahrenheit and Celsius with user input
 
 def TempConverter() : #function definition
	temp = int(input(' Please enter the temperature you would like to convert and the unit you want to convert it into : ')) 
	unit = input(' Please enter the unit you want to convert it into (F or C) : ')
	if (unit=='C'):
		Cel= (temp-32)*(5/9)   # formula to convert Celsius to Fahrenheit
		if (Cel==temp):
			print('The temperature in Celsius is same as Fahrenheit :', Cel)
		else:
			print(temp,'Fahrenheit is equal to',Cel, 'Celsius')
	else:
		Frh=(9/5)*temp+32   # formula to convert Fahrenheit to Celsius
		if (Frh==temp):
			print('The temperature in Fahrenheit is same as Celsius : ',Frh)
		else:
			print(temp,'Celsius is equal to',Frh, 'Fahrenheit')
