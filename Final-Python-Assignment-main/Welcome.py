#Module: Welcome

from StockAnalysis import main
import os

def choice2():
    stream = os.popen('streamlit run GUI.py')
    output = stream.read()
    output
    
def choice_interface():
    print("\nSelect the option where you want to run the program \n1. Text Interface \n2. User Interface \n3. Quit")
    return input("Enter the choice :")

print("Welcome to the Budiing Analysts Stock Quote Application")
command_choice = choice_interface()

while command_choice != "3":
    if command_choice == "1":
        main()
    elif command_choice == "2":
        choice2()  
    else:
        print("Wrong choice, please try again.")
    command_choice = choice_interface()
    
