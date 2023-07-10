''' formula of BMI cal
weight(kg)/height(m)x height(x) '''

height = float(input("Enter your Height in cm "))
weight = float(input("Enter your Weight in kg"))

height = height/100
BMI = weight/(height*height)

print("Your body mass index is:",BMI)

if BMI>0:
    if BMI<=16:
        print("you are severely under weight")

    elif BMI<18.5:
        print("you are under weight")

    elif BMI<=25:
        print("you are healthy ")

    elif BMI<=30:
        print("you are Overweight")

    else:
        print("you are severely overweight")

else:
    print("you have Entered invalid Details ")


