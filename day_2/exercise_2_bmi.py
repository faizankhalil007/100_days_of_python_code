# in this example we will create a BMI(Body Mass Index) Calculator
# BMI formula BMI = weight(kg) / height(power 2)(m)
# lets start
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = float(weight) / float(height) ** 2
print(BMI)
# to round the result use round
print(round(BMI))
# to round a specific number of length
print(round(BMI,2))
# to convert to integer
print(int(BMI))