pet = "dog"
age = 4

if pet == "dog":
    if age < 2:
        food = "Puppy Food"
    else:
        food = "Adult Dog Food"
elif pet == "cat":
    if age > 5:
        food = "Senior Cat food"
    else:
        food = "Adult Cat Food"
    
print("Recommended food : ", food)