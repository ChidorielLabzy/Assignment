print ("PERSONAL TIME TABLE\nWelcom to your Division and Multiplication time table creating program")
num=int(input(f"Enter the number for the time table you want  to produce:"))

for i in range(0, 13):
    product = i * num
    print(f"{i}x{num}= {product}")
    
print(f"\nCongratulations you now have the {num} times table.\n")
    
for i in range(0, 13):
    division =i/num
    print(f"{i}/{num}= {division:,.2f}")
    
print(f"\nCongratulations you now have the {num} division table.\nGoodbye 👋")
          
          
