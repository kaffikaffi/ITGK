def komparativ(adj):
    # GROVT FORENKLET FOR Å KUNNE FOKUSERE PÅ HOVEDPOENGET
    if len(adj) >= 8: # unøyaktig
        svar = "mer " + adj
    else:
        svar = adj + "ere"
    return svar
  
### TILLEGG 1, ny funksjon, kommer her:
def superlativ(adj):
    # GROVT FORENKLET FOR Å KUNNE FOKUSERE PÅ HOVEDPOENGET
    if len(adj) >= 8: # unøyaktig
        svar = "mest " + adj
    else:
        svar = adj + "est"
    return svar
  
 


# DEL AV KODEN HVOR BRUKEREN TRENER PÅ Å GRADBØYE
def checkFasit(x,e):
    if x == e:
        print("Korrekt!")
    else:
        print("Feil, det var", e)


def main():
    adj = input("Beskriv deg selv med et adjektiv: ")
    print("Hah! Jeg er mye", komparativ(adj), "!")  

    adj
    print(f"Jeg er faktisk {superlativ(adj)} i hele verden")

    adj
    x = input("Hva er komparativ for" + adj + " ? ")
    fasit = komparativ(adj)
    checkFasit(x, fasit)

    adj
    svar = input("Hva er superlativ for" + adj + " ? ")
    fasit = superlativ(adj)
    checkFasit(svar,fasit)


main()

