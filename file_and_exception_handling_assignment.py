# Exercise 1:
# Write a Python program to read a file and display its contents

file1=open("C:\\Users\\HP\\Desktop\\hello.txt",'r')
print(file1.read())

# Exercise 2:
# Write a Python program to copy the contents of one file to another file

file_to_read="sample.txt"
write_to_file="output.txt"

file2=open(file_to_read,'r')
data=file2.read()
file2.close()

with open(write_to_file,'a')as file2:
    file2.write(data)
print('completed')

# Exercise 3:
# Write a Python program to read the content of a file and count the total number of words in that file.

with open("C:\\Users\\HP\\Desktop\\class.txt",'r') as file3:
 datas = file3.read()
print(datas)

print(datas.split())
print(len(datas.split()))


# Exercise4:
# Write a Python program that prompts the user to input a string and converts it to an integer. Use try-except blocks to handle any
# exceptions that might occur

def convert_to_integer():
    user_input = input("Enter a number: ")
    try:
        # Attempt to convert the input to an integer
        number = int(user_input)
        print(f"Successfully converted to integer: {number}")
    except ValueError:
        print("Error: The input is not a valid integer. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


convert_to_integer()

# Exercise 5:
# Write a Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative.

def check_positive_integers():
    try:
        # Prompt the user to input a list of integers
        user_input = input("Enter a list of integers separated by spaces: ")
        # Convert the input string to a list of integers
        numbers = list(map(int, user_input.split()))
        print(numbers)

        # Check for negative integers
        for num in numbers:
            if num < 0:
                raise ValueError(f"Negative integer found: {num}")

        print("All integers are positive!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

check_positive_integers()

# Exercise 6:
# Write a Python program that prompts the user to input a list of integers and computes the average of those integers. Use try-except blocks to
# handle any exceptions that might occur.use the finally clause to print a message indicating that the program has finished running.

def compute_average():
    try:
        # Prompt the user to input a list of integers
        user_input = input("Enter a list of integers separated by spaces: ")
        # Convert the input string to a list of integers
        numbers = list(map(int, user_input.split()))
        print(numbers)

        if len(numbers) == 0:
            raise ValueError("The list is empty. Cannot compute the average.")

        # Compute the average
        average = sum(numbers) / len(numbers)
        print(f"The average of the entered integers is: {average:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Program has finished running.")

compute_average()

# Exercise 7 :
# Write a Python program that prompts the user to input a filename and writes a string to that file. Use try-except blocks to handle any exceptions
# that might occur and print a welcome message if there is no exception occurred.

def write_to_file():
    try:
        # Prompt the user for a filename
        file_name = input("Enter the filename (with extension): ")

        # Prompt the user for the string to write to the file
        content = input("Enter the string to write to the file: ")

        # Write the string to the file
        with open(file_name, 'w') as file:
            file.write(content)

        # Print a welcome message if no exception occurs
        print("Welcome! The string has been successfully written to the file.")
    except Exception as e:
        # Handle any exceptions that occur
        print(f"An error occurred: {e}")


write_to_file()