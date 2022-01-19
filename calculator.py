def add(A, Q):    
    return A + Q   
def subtract(A, Q):   
   return A - Q   
def multiply(A, Q):     
   return A * Q   
def divide(A, Q):   
   return A / Q    
 
print ("Please select the operation.")    
print ("Add")    
print ("Subtract")    
print ("Multiply")    
print ("Divide")    
    
choice = input("Please enter operation to be done:-> ")    
    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
    
if choice == 'Add':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif choice == 'Subtract':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
elif choice == 'Multiply':    
   print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))    
elif choice == 'Divide':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))  
else:    
   print ("Error")  