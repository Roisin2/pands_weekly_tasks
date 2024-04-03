# counting e from text file. The program should take the filename from arg on the command line.
# Author: Roisin Stanley

#cd "C:\Users\Roisin\OneDrive\Desktop\my-weekly-tasks\" # change directory to folder

# import module to work with command line
import sys

filename = "moby_dick.text"

def count_letter_e(filename):
    try:
        with open(filename, 'rt') as file:                      # open file if exists in read text mode
            data = file.read()                                  # Read entire file into a string
            e_count = data.lower().count('e')                   # Count occurrences of 'e' in the entire file
            print(f"Number of 'e's in the file: {e_count}")     # print total amount of e's using f string
    except FileNotFoundError:
        print(f"ERR_01 - File '{filename}' not found! Please check the filename.") # if file not found print message


if __name__ == "__main__":    # checking script run directly not imported
    if len(sys.argv) != 2:    # if the command line is provided then it calls the function count_letter_e
        print("ERR_02 - Use: python count_es.py <filename>")
    else:
        filename = sys.argv[1] # retrieves file name from command line arguement
        count_letter_e(filename)


# then run this from terminal --- python es.py moby_dick.text   

'''
sys.argv is a list in Python that contains the command-line arguments passed to a script when it is run.
The expression len(sys.argv) calculates the length of this list,which corresponds to the number of arguments.
The condition len(sys.argv) != 2 checks if the number of arguments is not equal to 2 
If the condition is true, it shows that the user didnt give the expected number of arguments,
 and the script can then handle this condition.

 reference: https://stackoverflow.com/questions/4765085/using-command-line-arguments-in-python-understanding-sys-argv
 '''