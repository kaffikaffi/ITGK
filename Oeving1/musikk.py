number_of_10melody = input("Antall ulike 10-toners melodilinjer du har hørt?")
max_possible = 8.25e19
result = int(number_of_10melody)/int(max_possible)
print("Du har hørt " + format(result,'.2e') + " prosent av melodier som er mulig")