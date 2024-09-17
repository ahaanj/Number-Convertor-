import time
from colorama import Fore


def bin_den():
    while True:
        try:
            # Inform the user about the purpose of the function and prompt for input
            print(Fore.GREEN)
            print("This function will convert a binary number that is entered and will return it as a decimal number")
            print(Fore.BLUE)
            bina = input("Enter the binary number that you want to convert to a decimal number: ")
            int_bina = int(bina)  # Attempt to convert to integer
            list_bina = list(str(int_bina))
            length = len(list_bina)
            count = 0
            
            # Validate that the input contains only '0's and '1's
            for x in list_bina:
                if x not in ["1", "0"]:
                    print(Fore.RED)
                    print("Please enter a number only consisting of 1s and 0s")
                    print(Fore.CYAN)
                    raise ValueError  # Raise an error to restart the loop
                else:
                    count += 1
            
            # If input is valid, break out of the loop
            if count == length:
                break
        
        except ValueError:
            # Handle the case where the input is not a valid binary number
            print(Fore.RED + "Please enter a valid binary number.")
            continue

    # Convert the binary number to decimal
    binary = 0
    for y in range(len(list_bina)):
        num = int(list_bina[y])
        val = (num * 2 ** (length - y)) / 2
        binary += val
    
    # Extract the integer part of the decimal representation
    binary = str(binary)
    bin_list = binary.split(".")
    pri = bin_list[0]
    
    # Inform the user that the evaluation is in progress
    time.sleep(2)
    print(Fore.MAGENTA)
    print("Evaluating...")
    time.sleep(2)
    
    # Display the result
    print(Fore.GREEN)
    print(f"{int_bina} as a decimal number is {pri}")
    print(Fore.RESET)



def den_bin():
    # Inform the user about the purpose of the function
    print(Fore.GREEN)
    print("This function will convert a decimal number into binary and return the binary number")
    print(Fore.BLUE)
    
    # Prompt the user to enter a decimal number and handle invalid inputs
    while True:
        try:
            den = int(input("Please enter a decimal number that you would like to convert to binary: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Initialize variables for the division loop
    x = den
    y = den
    list_bin = []
    
    # Perform the conversion from decimal to binary
    while True:
        x = y % 2
        y = y // 2  # Use integer division to get integer quotient
        if int(x) >= 1 and int(x) <= 2:
            list_bin.append(1)
        else:
            list_bin.append(int(x))
        if y < 1:
            break
            
    # Reverse the list to get the binary representation in correct order
    list_bin = list_bin[::-1]
    str_bin = ""
    
    # Convert the list of binary digits to a string
    for x in list_bin:
        str_bin = str_bin + str(x)
        
    # Inform the user that evaluation is in progress
    print(Fore.MAGENTA)
    time.sleep(2)
    print("Evaluating...")
    time.sleep(2)
    
    # Display the result
    print(Fore.GREEN)
    print(f"{den} as a binary number is {str_bin}") 
    print(Fore.RESET)
    
    
def den_hex():
    print("This function will convert a decimal number into hexadecimal")
    
    while True:
        try:
            # Taking user input for the decimal number
            dena = int(input("Enter a decimal number that you want to convert into hexadecimal: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    div = dena  # Initializing div with the input decimal number
    rval = dena  # Initializing rval with the input decimal number
    con = 0  # Initializing con to control loop
    list_hexa = []  # List to store hexadecimal digits
    str_hexa = ""  # String to store hexadecimal representation
    list_hex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}  # Dictionary for hexadecimal representation

    # Loop to convert decimal to hexadecimal
    while True:
        div = rval % 16  # Getting remainder
        rval = int(rval / 16)  # Getting quotient
        if div > 9:
            div = list_hex[div]  # Replacing digits > 9 with corresponding hexadecimal letters
        list_hexa.append(div)  # Appending remainder to the list
        if con == 1:  # Checking condition to break the loop
            break
        if rval < 16:  # Checking if quotient is less than 16
            con = 1  # Setting con to 1 to break the loop
    
    list_hexa = list_hexa[::-1]  # Reversing the list to get correct hexadecimal representation
    if list_hexa[0] == 0:  # Removing leading zeros if present
        del list_hexa[0]
        
    time.sleep(2)  # Adding delay for effect
    print("Evaluating...")
    time.sleep(2)  # Adding delay for effect
    print(Fore.GREEN)  # Changing text color to green
    print(f"{dena} as a hexadecimal number is {''.join(map(str, list_hexa))}")  # Printing hexadecimal representation
    print(Fore.RESET)  # Resetting text color
    
def hex_den():
    # Dictionary to map hexadecimal characters to their decimal equivalents
    hex_diction = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
    
    # Printing instructions and hexadecimal to decimal equivalents
    print(Fore.GREEN)
    print("This function will convert a hex number into a decimal number")
    print("These are the hex characters from A-F and their decimal equivalents")
    for k, v in hex_diction.items():
        print(f"{k} = {v}")
    print(Fore.BLUE)
    
    # Taking user input for the hexadecimal number
    hexa = input("Enter a hexadecimal number that you want to convert to decimal: ")
    hexa = hexa.upper()  # Converting input to uppercase for consistency
    list_hex = list(str(hexa))  # Converting the hexadecimal input to a list of characters
    
    count = 0  # Counter to check if all characters are valid hexadecimal digits
    while True:
        for x in range(len(hexa)):
            # Checking if each character is a valid hexadecimal digit
            if list_hex[x] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "0"]:
                print(Fore.RED)
                print("Please ensure that you have entered a hex number")
                hexa = input("Enter a hexadecimal number that you want to convert to decimal: ")
                list_hex = list(str(hexa))
                count = 0  # Resetting the counter
                hexa = hexa.upper()  # Converting input to uppercase for consistency
        if count == len(list_hex):
            break
        else:
            count = count + 1
    
    total = 0  # Variable to store the total decimal value
    list_hex = []  # List to store converted hexadecimal characters
    for y in range(len(hexa)):        
        if hexa[y] in hex_diction.keys():          
            list_hex.append(hex_diction[hexa[y]])  # Converting hexadecimal characters to their decimal equivalents
        else:
            list_hex.append(hexa[y])   
    
    # Calculating the decimal value
    for z in range(len(hexa)):
        a = len(hexa) - (z + 1)   
        b = 16 ** a  # Getting the power of 16 for each position
        c = int(list_hex[z])  # Converting the character to integer if it's not already
        total = total + (b * c)  # Adding the contribution of each position to the total
    
    time.sleep(2)  # Adding delay for effect
    print(Fore.MAGENTA)
    print("Evaluating...")
    time.sleep(2)  # Adding delay for effect
    print(Fore.GREEN)
    print(f"{hexa} as a decimal number is {total}")  # Printing the decimal equivalent
    print(Fore.RESET)  # Resetting text color
    
def hex_bin():
    # Dictionary to map hexadecimal characters to their decimal equivalents
    hex_diction = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
    
    # Printing instructions and hexadecimal to decimal equivalents
    print(Fore.GREEN)
    print("This function will convert a hex number into a binary number") 
    print("These are the hex characters from A-F and their decimal equivalents")
    for k, v in hex_diction.items():
        print(f"{k} = {v}")
    print(Fore.BLUE)
    
    # Taking user input for the hexadecimal number
    hexa = input("Enter a hexadecimal number that you want to convert to binary: ")
    hexa = hexa.upper()  # Converting input to uppercase for consistency
    list_hex = list(str(hexa))  # Converting the hexadecimal input to a list of characters
    
    count = 0  # Counter to check if all characters are valid hexadecimal digits
    while True:
        for i in range(len(hexa)):
            # Checking if each character is a valid hexadecimal digit
            if list_hex[i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "0"]:
                print(Fore.RED)
                print("Please ensure that you have entered a hex number")
                hexa = input("Enter a hexadecimal number that you want to convert to binary: ")
                list_hex = list(str(hexa))
                count = 0  # Resetting the counter
                hexa = hexa.upper()  # Converting input to uppercase for consistency
        if count == len(list_hex):
            break
        else:
            count = count + 1        
    
    # Creating an empty list to store the converted binary digits
    list_bin = []
    
    # Converting hexadecimal characters to their decimal equivalents
    for j in range(len(hexa)):       
        if hexa[j] in hex_diction.keys():       
            list_bin.append(hex_diction[hexa[j]])  # Appending decimal equivalents to the list
        else:
            list_bin.append(hexa[j])  # If not in the dictionary, appending the character itself
    
    total = ""  # Variable to store the total binary value
    # Looping through the list of decimal equivalents
    for z in list_bin:       
        den = int(z)  # Converting the character to integer
        x = den
        y = den
        list_bin = []  # List to store binary digits
        
        # Converting decimal to binary
        while True:
            x = y % 2
            y = y / 2         
            if int(x) >= 1 and int(x) <= 2:
                list_bin.append(1)
            else:
                list_bin.append(int(x))
            if y <= 1:
                break
        
        list_bin = list_bin[::-1]  # Reversing the list to get correct binary representation
        
        # Adding leading zeros if necessary to make each group 4 digits
        if len(list_bin) != 4:
            list_bin.insert(0, "0")
        
        str_bin = ""  # String to store binary representation
        for l in list_bin:
            str_bin = str_bin + str(l)
        
        # Adding leading zeros to make the binary number divisible by 4
        while True:
            if len(str_bin) % 4 == 0:
                break
            else:
                str_bin = "0" + str_bin           
        
        total = total + str_bin  # Concatenating binary representations
    
    time.sleep(2)  # Adding delay for effect
    print(Fore.MAGENTA)
    print("Evaluating")
    time.sleep(2)  # Adding delay for effect
    print(Fore.GREEN)
    print(f"{hexa} in binary is {total}")  # Printing the binary equivalent
    print(Fore.RESET)  # Resetting text color
    
def bin_hex():
    # Printing instructions
    print(Fore.GREEN)
    print("This function will convert a binary number that is entered into a hexadecimal number")
    print(Fore.BLUE)
    
    while True:
        try:
            # Taking user input for the binary number
            bina = input("Enter the binary number that you want to convert to a hexadecimal number: ")
            # Checking if the input consists only of 0s and 1s
            if all(c in "01" for c in bina):
                break  # If the input is valid, exit the loop
            else:
                print(Fore.RED)
                print("Please enter a number consisting only of 1s and 0s.")
                print(Fore.RESET)
        except ValueError:
            print(Fore.RED)
            print("Please enter a valid binary number.")
            print(Fore.RESET)

    list_bina = list(bina)  # Converting the binary input to a list of characters
    length = len(list_bina)  # Getting the length of the binary number

    binary = 0  # Variable to store the decimal value of the binary number
    # Converting binary to decimal
    for y in range(len(list_bina)):
        num = int(list_bina[y])  # Converting the character to integer
        val = (num * 2**(length - y)) / 2  # Calculating the decimal value of each digit
        binary = binary + val  # Accumulating the decimal value

    binary = str(binary)  # Converting the decimal value to string
    bin_list = binary.split(".")  # Splitting the decimal value by the decimal point
    pri = bin_list[0]  # Extracting the integer part of the decimal value
    dena = pri  # Assigning the integer part to dena for further processing   
    div = int(dena)  # Initializing div with the integer part
    rval = int(dena)  # Initializing rval with the integer part  
    con = 0  # Initializing con to control loop
    list_hexa = []  # List to store hexadecimal digits
    str_hexa = ""  # String to store hexadecimal representation
    list_hex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}  # Dictionary for hexadecimal representation

    # Loop to convert decimal to hexadecimal
    while True:
        div = rval % 16  # Getting remainder
        rval = int(rval / 16)  # Getting quotient  
        if div > 9:
           div = list_hex[div]  # Replacing digits > 9 with corresponding hexadecimal letters
        list_hexa.append(str(div))  # Appending remainder to the list
        if con == 1:  # Checking condition to break the loop
            break        
        if rval < 16:  # Checking if quotient is less than 16
            con = 1  # Setting con to 1 to break the loop

    list_hexa = list_hexa[::-1]  # Reversing the list to get correct hexadecimal representation
    if list_hexa[0] == '0':  # Removing leading zeros if present
        del list_hexa[0]
    
    print(Fore.MAGENTA)
    time.sleep(2)
    print("Evaluating...")
    time.sleep(2)
    
    print(Fore.GREEN)
    print(f"{bina} as a hexadecimal number is {''.join(list_hexa)}")  # Printing the hexadecimal representation
    print(Fore.RESET)

    
def den_bin2(den):
    # Initialize variables
    x = den
    y = den
    list_bin = []

    # Loop to convert decimal to binary
    while True:
        # Get the remainder of division by 2
        x = y % 2
        # Get the quotient after division by 2
        y = y / 2

        # Append the remainder to the binary list
        if int(x) >= 1 and int(x) <= 2:
            list_bin.append(1)
        else:
            list_bin.append(int(x))

        # Check if the quotient is less than 1 to break the loop
        if y < 1:
            break

    # Reverse the list to get the correct binary representation
    list_bin = list_bin[::-1]

    # Convert the binary list to a string
    str_bin = ""
    for x in list_bin:
        str_bin = str_bin + str(x)

    # Return the binary representation as a string
    return str_bin


def bin_den2(bina):    
    # Convert the binary input to a list of characters
    list_bina = list(str(bina))
    # Get the length of the binary number
    length = len(list_bina)        
    binary = 0
    
    # Loop through each digit of the binary number
    for y in range(len(list_bina)):
        # Convert the character to an integer
        num = int(list_bina[y])
        # Calculate the decimal value of each digit
        val = (num * 2**(length - y)) / 2
        # Accumulate the decimal value
        binary = binary + val
    
    # Convert the total decimal value to string
    binary = str(binary)
    # Split the decimal value by the decimal point
    bin_list = binary.split(".")
    # Extract the integer part of the decimal value
    pri = bin_list[0]
    
    # Return the integer part of the decimal value
    return pri



def bitwise_AND():
    while True:
        try:
            # Print instructions
            print(Fore.GREEN)
            print("This function will perform a bitwise AND on 2 decimal numbers")
            print(Fore.BLUE)
            
            # Input the first decimal number
            den = int(input("Please enter a decimal number that you would like to perform a bitwise AND on: "))
            # Convert the first decimal number to binary
            a = den_bin2(den)
            time.sleep(2)
            
            # Inform processing
            print(Fore.MAGENTA)
            print("Processing...")
            time.sleep(2)
            print(Fore.BLUE)
            
            # Input the second decimal number
            den2 = int(input("Please enter the other decimal number that you would like to perform a bitwise AND on: "))
            # Convert the second decimal number to binary
            b = den_bin2(den2)
            
            # Validate if binary strings are of equal length
            while len(a) != len(b):
                if len(a) < len(b):
                    a = '0' + a
                else:
                    b = '0' + b
            
            # Ensure binary strings are multiples of 4
            a = a.zfill((len(a) + 3) // 4 * 4)
            b = b.zfill((len(b) + 3) // 4 * 4)
            
            # Perform bitwise AND operation
            list_total = [int(a[i]) * int(b[i]) for i in range(len(a))]
            str_total = ''.join(map(str, list_total))
            # Convert the result back to decimal
            pri2 = bin_den2(int(str_total))
            
            # Inform evaluation
            print(Fore.MAGENTA)
            print("Evaluating...")
            time.sleep(2)
            print(Fore.GREEN)
            # Print the result
            print(f"A bitwise AND on {den} and {den2} results in {pri2}")
            print(Fore.RESET)
            break
        except ValueError:
            # Catch invalid input errors
            print(Fore.RED)
            print("Invalid input. Please enter a valid decimal number.")
            print(Fore.RESET)
            
            
def bitwise_OR():
    while True:
        try:
            # Print instructions
            print(Fore.GREEN)
            print("This function will perform a bitwise OR on 2 decimal numbers")
            print(Fore.BLUE)
            
            # Input the first decimal number
            den = int(input("Please enter a decimal number that you would like to perform a bitwise OR on: "))
            time.sleep(2)
            
            # Inform processing
            print(Fore.MAGENTA)
            print("Processing...")
            time.sleep(2)
            print(Fore.BLUE)
            
            # Input the second decimal number
            den2 = int(input("Please enter the other decimal number that you would like to perform a bitwise OR on: "))
            
            # Convert decimal numbers to binary
            a = den_bin2(den)
            b = den_bin2(den2)
            
            # Validate if binary strings are of equal length
            while len(a) != len(b):
                if len(a) < len(b):
                    a = '0' + a
                else:
                    b = '0' + b
            
            # Ensure binary strings are multiples of 4
            a = a.zfill((len(a) + 3) // 4 * 4)
            b = b.zfill((len(b) + 3) // 4 * 4)
            
            # Perform bitwise OR operation
            list_total = [int(a[i]) + int(b[i]) - int(a[i]) * int(b[i]) for i in range(len(a))]
            str_total = ''.join(map(str, list_total))
            st2 = bin_den2(int(str_total))
            
            # Inform evaluation
            print(Fore.MAGENTA)
            print("Evaluating...")
            time.sleep(2)
            print(Fore.GREEN)
            # Print the result
            print(f"A bitwise OR on {den} and {den2} results in {st2}")
            print(Fore.RESET)
            break
        except ValueError:
            # Catch invalid input errors
            print(Fore.RED)
            print("Invalid input. Please enter a valid decimal number.")
            print(Fore.RESET)

    
    
def bitwise_XOR():
    while True:
        try:
            # Print instructions
            print(Fore.GREEN)
            print("This function will perform a bitwise XOR on two decimal numbers")
            print(Fore.BLUE)
            
            # Input the first decimal number
            den = int(input("Please enter a decimal number that you would like to perform a bitwise XOR on: "))   
            # Convert the first decimal number to binary
            a = den_bin2(den)
            time.sleep(2)
            
            # Inform processing
            print(Fore.MAGENTA)
            print("Processing...")
            time.sleep(2)
            print(Fore.BLUE)
            
            # Input the second decimal number
            den2 = int(input("Please enter another decimal number that you would like to perform a bitwise XOR on: "))
            # Convert the second decimal number to binary
            b = den_bin2(den2)
            
            # Ensure binary strings are multiples of 4
            a = a.zfill((len(a) + 3) // 4 * 4)
            b = b.zfill((len(b) + 3) // 4 * 4)
            
            # Validate if binary strings are of equal length
            while len(a) != len(b):
                if len(a) < len(b):
                    a = '0' + a
                else:
                    b = '0' + b
            
            # Perform bitwise XOR operation
            list_total = [int(a[i]) + int(b[i]) - int(a[i]) * int(b[i]) for i in range(len(a))]
            str_total = ''.join(map(str, list_total))
            # Convert the result back to decimal
            st2 = bin_den2(str_total)
            
            # Inform evaluation
            print(Fore.MAGENTA)
            print("Evaluating...")
            time.sleep(2)
            print(Fore.GREEN)
            # Print the result
            print(f"A bitwise XOR on {den} and {den2} results in {st2}")
            print(Fore.RESET)
            break
        except ValueError:
            # Catch invalid input errors
            print(Fore.RED)
            print("Invalid input. Please enter a valid decimal number.")
            print(Fore.RESET)
            
def bitwise_NOT():
    while True:
        # Print instructions
        print(Fore.GREEN)
        print("This function will perform a bitwise NOT on a decimal number")
        print(Fore.BLUE)
        
        # Input the decimal number
        den = input("Please enter a decimal number that you would like to perform a bitwise NOT on: ")
        
        # Validate input: Ensure that the input is a valid decimal number
        if not den.isdigit():
            print(Fore.RED)
            print("Error: Please enter a valid decimal number.")
            print(Fore.RESET)
            continue

        try:
            # Convert the input to an integer
            int_den = int(den)
            # Convert the decimal number to its binary representation
            a = den_bin2(int_den)

            # Validate input: Ensure that the binary representation is a valid binary number
            for bit in a:
                if bit not in '01':
                    raise ValueError("Invalid binary representation")

            # Perform bitwise NOT operation
            list_total = [1 - int(bit) for bit in a]

            # Convert the result back to decimal
            st = ''.join(map(str, list_total))
            st2 = bin_den2(st)

            # Inform evaluation
            print(Fore.MAGENTA)
            print("Evaluating...")
            time.sleep(2)
            print(Fore.GREEN)
            # Print the result
            print(f"A bitwise NOT on {int_den} results in {st2}")
            print(Fore.RESET)
            break
        except ValueError as e:
            # Catch invalid input errors
            print(Fore.RED)
            print(f"Error: {e}")
            print(Fore.RESET)
    
def den_bin3(bina):
    # Convert the input binary number to an integer
    x = int(bina)
    y = int(bina)
    list_bin = []

    # Loop to convert binary to decimal
    while True:
        # Get the remainder of division by 2
        x = y % 2
        # Get the quotient after division by 2
        y = y / 2 

        # Append the remainder to the binary list
        if int(x) >= 1 and int(x) <= 2:
            list_bin.append(1)
        else:
            list_bin.append(int(x))
        
        # Check if the quotient is less than 1 to break the loop
        if y < 1:
            break

    # Reverse the list to get the correct binary representation
    list_bin = list_bin[::-1]

    # Convert the binary list to a string
    str_bin = ""
    for x in list_bin:
        str_bin = str_bin + str(x)
    
    # Return the binary representation as a string
    return str_bin

def bin_den3(bina):
    # Convert the input binary number to a list of characters
    list_bina = list(str(bina))
    length = len(list_bina)       
    count = 0
    
    # Loop to validate binary input
    while True:
        for x in list_bina:
            # Check if each character is either '0' or '1'
            if x not in ["1", "0"]:
                print(Fore.RED)
                print("Please enter a number only consisting of 1s and 0s")
                print(Fore.BLUE)
                # Request new binary input if there's an invalid character
                bina = int(input("Enter the binary number that you want to add to another binary number: "))
                list_bina = list(str(bina))
                length = len(list_bina)
                break
            else:
                count += 1
        if count == length:
            break
    
    # Convert binary to decimal
    binary = 0
    for y in range(len(list_bina)):
        num = int(list_bina[y])
        val = (num * 2**(length - y)) / 2
        binary = binary + val
    
    # Convert the total decimal value to a string
    binary = str(binary)
    bin_list = binary.split(".")
    pri = bin_list[0]
    
    # Return the integer part of the decimal value
    return pri

def bin_addition():
    while True:
        # Print instructions
        print(Fore.GREEN)
        print("This is a program that will add two binary numbers of your choice")
        print(Fore.BLUE)
        
        # Input the first binary number
        bina = input("Enter a binary number that you want to add: ")
        # Input the second binary number
        bina2 = input("Enter another binary number that you want to add: ")
        
        # Validate input: Ensure that both inputs are valid binary numbers
        if not all(bit in '01' for bit in bina) or not all(bit in '01' for bit in bina2):
            print(Fore.RED)
            print("Error: Please enter valid binary numbers (containing only 0s and 1s).")
            print(Fore.RESET)
            continue

        try:
            # Convert binary numbers to decimal
            a = int(bin_den3(bina))
            b = int(bin_den3(bina2))
            
            # Perform addition
            su = a + b
            # Convert the sum back to binary
            total = den_bin3(su)

            # Inform evaluation
            print(Fore.BLUE)
            print("Evaluating...")
            time.sleep(2)
            print(Fore.GREEN)
            # Print the result
            print(f"The sum of {bina} and {bina2} is {total}")
            print(Fore.RESET)
            break
        except ValueError as e:
            # Catch invalid input errors
            print(Fore.RED)
            print(f"Error: {e}")
            print(Fore.RESET)
            


# Function to choose and execute the desired function
def choose_func():
    # Prompt the user to enter the letter corresponding to the function they want to use
    print(Fore.BLUE)
    ch = input("Enter the letter of the function that you would like to use: ")
    ch = ch.lower()  # Convert input to lowercase for uniformity
    
    # Dictionary mapping function letters to their respective functions
    func = {
        "a": den_bin,
        "b": bin_den,
        "c": den_hex,
        "d": hex_den,
        "e": hex_bin,
        "f": bin_hex,
        "g": bitwise_AND,
        "h": bitwise_OR,
        "i": bitwise_XOR,
        "j": bitwise_NOT,
        "k": bin_addition
    }
    
    # Loop until a valid function letter is entered
    while True:
        if ch not in func.keys():
            print(Fore.RED)
            print("Ensure that you have entered one of the letters of the functions i.e a-h")
            print(Fore.BLUE)
            ch = input("Enter the letter of the function that you would like to use: ")
            ch = ch.lower()  # Convert input to lowercase for uniformity
        else:
            break
    
    # Execute the chosen function
    func[ch]()

# Main program logic
f = 0
while True:    
    if f == 0:  
        # Display the available functions if it's the first iteration
        print(Fore.GREEN)         
        print("---This is a calculator with the functions listed below---")
        print()
        print("a) Decimal Number to Binary Number.")              
        print("b) Binary Number to Decimal Number.")
        print("c) Decimal Number to Hexadecimal Number.")
        print("d) Hexadecimal Number to Decimal Number.")
        print("e) Hexadecimal Number to Binary Number.")
        print("f) Binary Number to Hexadecimal Number.")
        print("g) Bitwise AND Operation.")
        print("h) Bitwise OR Operation.")
        print("i) Bitwise XOR Operation.")
        print("j) Bitwise Not Operation.")
        print("k) Addition of two Binary Numbers")
        # Call the function to choose and execute the desired function
        choose_func()
    
    print(Fore.BLUE)
    # Prompt the user to continue or exit
    contin = input("Do you want to continue? ")
    contin = contin.lower()
    
    if contin in ["n", "no"]:
        # If user chooses to exit, print a thank you message and break the loop
        print(Fore.GREEN)
        print("Thank you for using the Number Converter, brought to you by Ahaan!")
        break
    elif contin not in ["y", "yes", "n", "no", "NO", "YES"]:
        # If invalid input is provided, prompt the user again
        print(Fore.RED)
        print("Ensure that you enter y/n")
        print(Fore.BLUE)
        contin = input("Do you want to continue? ")
        contin = contin.lower()
    else:
        # Increment f to indicate that it's not the first iteration and call choose_func() again
        f = f + 1
        choose_func()
