#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calculator!\n")
total_bil = float(input("what was the total bill? $"))
tip_pecentage = int(input("how much tip would you like to give? ,10 ,12 ,or 15 ? "))
number_of_people = int(input("how many people to split the bill? "))
amount_to_pay = (total_bil/number_of_people)*(tip_pecentage/100)
normal_bill = total_bil/number_of_people
print(f"each person should pay: ${round(amount_to_pay + normal_bill, 2)}")