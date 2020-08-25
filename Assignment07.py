# ------------------------------------------------- #
# Title:
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Rabiya Abdul, 08.24.2020, Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# 1. Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomerName = []
lstCustomerId= []
UnpickledCName= [] #Displays the unpickled list of Customer names
UnpickledCId=[] #Displaying the unpickled list of Customer IDs

# 2. Menu and Processing
# TODO: Get ID and NAME From user, then store it in a list object-- done
# 2.1 Display menu
print("""
    Menu of Options
    1. Add data 
    2. Save to binary file (Pickle)
    3. Read from binary file (Unpickle)
    4. Exit
    """)
while(True):
    Choice=0
    try:
        Choice=int(input("Which option would you like to perform?"))
    except ValueError:
        print("Not a number. Please enter a number") #Exception to handle if the choice is not an integer
    if Choice==1:
        name = str(input("Enter a name for the user: "))
        try:
            id=int(input("Enter the ID: "))
        except ValueError:
            print("Please enter a number \n")
            continue
        lstCustomerName.append(name)
        lstCustomerId.append(id)
        print()
        print("Customer Names : ", lstCustomerName)
        print("Customer IDs : ", lstCustomerId)
        print()
        continue
# 2.2 TODO: store the list object into a binary file---Done
    elif Choice==2:
        print("Pickling lists")
        f=open("AppData.dat", "wb")
        pickle.dump(lstCustomerName, f)
        pickle.dump(lstCustomerId, f)
        f.close()
        continue
    elif Choice==3:
#2.3 TODO: Read the data from the file into a new list object and display the contents
        try:
            f=open("Appdata.dat", "rb")
            UnpickledCName = pickle.load(f)
            UnpickledCId = pickle.load(f)
            print("\nUnpickling lists")
            print("Unpickled Customer Names: ", UnpickledCName)
            print("Unpickled Customer IDs: ", UnpickledCId)
            f.close()
            continue
        except FileNotFoundError: #Exception to handle file not found erro
            print("File not found. Please enter correct filename")
            print()
        except pickle.UnpicklingError: #Exception to handle unpickling error if file is corrupted/modified
            print("There was a problem unpickling the file. Please check file \n")
    elif Choice==4:
        print("Exiting the program")
        break  #Exits the program