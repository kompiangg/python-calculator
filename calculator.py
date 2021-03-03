import re

print("Welcome to the python calculator"
    "\nwhere you can type equation continously"
    "\nin python operator syntax and get the result\n"
    "\nType quit or exit to close\n"
    "\nREMINDER : finish the equation before calculate")

result = 0

while (True) :
    if result == 0 :
        equation = str(input("Input the equation : "))
        result = ""
    else :
        print("\nThe result :", result)
        equation = str(input("Input the equation : " + result + " "))

    if (equation == 'quit') | (equation == 'exit'):
        print("Thank you for using this calculator, bruh")
        break
    else :
        equation = re.sub("[^0-9\+\*\/\-\().]", "", equation)
        result = str(eval(result + equation))
