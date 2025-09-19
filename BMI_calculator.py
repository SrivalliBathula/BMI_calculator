# BMI calculator
print("Welcome to BMI calculator")
while True:
    weight=float(input("Enter your weight in kg: "))
    Height=float(input("Enter your height in cm: "))
    
    #converting height in cm to meters
    height=Height/100
    
    #calculating BMI
    bmi = round(weight / (height**2),2)
    print(f'Your Body Mass Index is: {bmi}')
    
    # person is under weight if bmi is lessthan 18.5
    if bmi < 18.5:
        print("You're under_weight (not healthy)")
        
    #person is normal weight and healthy if bmi is in between 18.5 to 24.9
    elif 18.5 <= bmi < 25:
        print("You're normal_weight (Healthy)")
        
    #person in over weight and not healthy if bmi is in between 25 to 30 
    elif 25 <= bmi <= 30:
        print("You're over_weight (not healthy)")
        
    ##person is obese and high risk if bmi is greater than 30
    else:
        print("You're obese (High risk)")
        
    extra= input("Do you want to continue? (yes/no): ")
    if extra == 'no':
        print("Game Over")
        break
    


