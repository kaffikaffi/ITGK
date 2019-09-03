height  = input("hva er høyden til tetraederet?: ")
import math
a = 3/(math.sqrt(6)) * int(height)
surface_area = math.sqrt(3) * math.pow(a, 2)
volume = (math.sqrt(2) * math.pow(a, 3) ) / 12
print("I et tetraeder der høyden er " + height + " blir overflatearealet " + str(surface_area) + " og volumet blir " + str(volume))