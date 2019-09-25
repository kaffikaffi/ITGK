secret_word = input("Skriv inn det hemmelige ordet: ")

hp = int(input("Hvor forsøk får brukeren? "))


while hp > 0: 
    letter = input("Gjett en bokstav: ")

    if letter in secret_word:
        print("stemmer, bokstaven er i ordet")
    else:
        print ("Bokstaven " + str(letter) + " er ikke en bokstav i ordet" )
        hp -= 1
        if hp == 0:
            print("Spillet er over, du er tom for liv!")
    
