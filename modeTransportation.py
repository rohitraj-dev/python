distance = 12

if distance <3:
    mode = "Walk"
elif distance <= 15:
    mode = "Bike"
elif distance > 15:
    mode = "Car"
    
print("mode of transportation : ", mode)