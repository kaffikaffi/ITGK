import random

lowerRange = int(input("Bestem nedre grense for det tilfeldige tallet: "))
maxRange = int(input("Besten øvre grense for det tilfeldige tallet: "))
randomNumber = int(random.randint(lowerRange,maxRange))

guess = int(input ("Gjett tallet: "))

while guess !=randomNumber:

    if guess < randomNumber:
        print("Det riktige tallet er større")
    elif guess > randomNumber:
        print("Det riktige tallet er mindre")
    
    guess = int(input ("Gjett tallet: "))

print("Du gjettet riktig tall! " + str(randomNumber) )