element = input("Si et stoff du er i besittelse av: ")
molarMass = input("Hva er molmassen til " + element + "?: ")
mass = input("Hvor mange gram " +  element +  " har du?: ")

avogadroConstant = 6.022e23

result = ((int(mass)/int(molarMass))) * (avogadroConstant)
result = round(result,2)


print("Du har " + format(result,'.2e') + " molekyler " + element)