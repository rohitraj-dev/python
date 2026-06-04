password = "secure@123"

if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "medium"
elif len(password) > 10:
    strength = "strong"
    
print("password strength : ", strength)