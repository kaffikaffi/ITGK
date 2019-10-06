import math

GRAVITY = 9.81

def get_fall_time(d,g = GRAVITY):
    
    time = math.sqrt((2*d)/g)
    return time

print(get_fall_time(20))
print(get_fall_time(20,1.4))
