# If we wanted them to see the actual exception then use raise
raise   

# This is the code block for try except
try:
    file = open("orders.txt")
    
except FileNotFoundError:    
    print("File not found")

# finally will execute regardless of the above conditions
finally:
    print("Thanks!")