order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " Coffee with Extra Shot"
else:
    coffee = order_size + " Coffee"
    
print("Order : ", coffee)