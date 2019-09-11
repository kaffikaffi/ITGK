wanted_cookies = input("Hvor mange cookies vil du bake?")
recipe_standard = 48 #number of cookies the original recipe makes 
cookie_relation = int(wanted_cookies)/int(recipe_standard)

recipe_list =[
    ["sukker", 400],
    ["smør", 320],
    ["sjokolade",500],
    ["egg", 3],
    ["mel",460]
]
for inner_l in recipe_list:
    for item in inner_l:
        print (item)
##checkout objects and arrays. maybe iterate trough the array and multiply the factor by every element

