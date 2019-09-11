Pizza_prize = 750
Student_discount = 0.2
tip = 1.08

total_prize = (int(Pizza_prize) * float(1-Student_discount)) * float(tip)
print("prisen ble " + str(total_prize))
number_people = input("Hvor mange deltok på middagen?: ")
divided_prize = total_prize/ int(number_people)
print("Ettersom dere er " + str(number_people) + "personer, så må dere betale " + str(divided_prize) + " kroner hver.")