forever = "yes"
while forever == "yes":
    answer = input("Would you like to continue?")
    if answer.lower() == "yes": 
        continue
    else:
        forever = "No"
    
