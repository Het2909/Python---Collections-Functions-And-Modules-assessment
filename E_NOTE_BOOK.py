from datetime import datetime

menu="""
                Welcome to E - Note

            Press 1 for generate note book
            Press 2 for view note
            press 3 for exit

"""
try:
  with open("my_data.txt", "w") as file:
    pass 
  print("File 'my_data.txt' created successfully.")
except FileExistsError:
  print("File 'my_data.txt' already exists.")



status = True

while status:
  print(menu)
  choice=int(input("Enter your choice: "))
  if choice==1:
    name=input("Enter pyton E-Note generator name: ")
    title=input("Enter pyton E-Note title: ")
    content=input("Enter E-Note content: ")
    now = datetime.now()
    with open('my_data.txt','a') as file:
      file.write('-'*30 + '\n')
      file.write(f"{str(now)} \n") # it will print the date and tiem in log file
      file.write(f"E-Note Title : {title}\nE-Note Description : {content} \n{" "*10}Note Generator :{name}\n")
  elif choice==2:
    print("------------------------")
    # Get the current date and time
    
    # Print the date and time
    with open('my_data.txt','r')as file:
      read1=file.read()
    print(read1)
    
      #  title=file.read()
      #  name=file.read()
      #  content = file.read()
      #  print("E-Note title : ",name,"\n")
      #  print("E-Note description : ",content)
      #  print("\t\t\tNote generator : ",title)
    print("------------------------")
  elif choice == 3:
   print("Thankyou for using")
   status=False
  else:
   print("Enter a valide choice")

  choice1=input("Do you want to continue? y for yes and n for no: ")
  if choice1 == 'n':
    status=False

   
