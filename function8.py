def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_kwargs(movie="Jawaan", actor="Shah Rukh")
