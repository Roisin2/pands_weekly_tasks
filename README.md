# pands_weekly_tasks
Weekly task hand up.

## About this work.
    Below is a list of the weekly tasks assigned for hands on learning.
    I am a new learner in this enviornment and I did extensive reading and learning through various websites. Such as (https://realpython.com/search)
    (https://stackoverflow.com/) (https://www.geeksforgeeks.org).

    ### List of Tasks.
    bank.py
    accounts.py
    weekday.py
    collatz.py
    squareroot.py
    plottask.py
    es.py
    
## Use of this project.
    In doing these tasks, I was required to cover the course material but also source my own help through the linked websites. The class also has a group chat that helped 
    me a little when I got a bit lost with the technology along the way. There are links to references and sources beside the code within the py's.
    Unfortunatly due to my lack of expierence I encounterd a few issues with my committing of changes and out of worry of losing anymore material I will now add any         
    additional comments or information in this space.
    
    For Bank.py, I needed to change float to an integer and do addition, and print the answer. I read in the amounts in cents eg.amount1 = 65. 
    Then change to Euro (100c in a euro) and change float to integer eg. e1 = int(amount1) / 100.  Then added both - total_money = e1 + e2
    Printed the amounts with decimal point and only two numbers after the point. - print (f"the sum of the amounts is €{total_money:.2f}")
    After progressing my Knowlege I may have done it a little differently by using "floor". But I believe the answer I gave was suffient as a novice.
    "floor" is a function from "math" that can imported.
    
    For accounts.py, a user is prompted to enter a 10 digit code and the program will check if exactly 10 digits, if the entry was valid, it will mask 6 numbers 
    with X and append the last 4 and print it out.

    Weekday.py - I imported datetime module.That gives todays date Returning the day of the week as an integer, eg. Monday is 0. A Loop is used to check what day it is and      prints a message according to the day, depending on if its a weekday or weekend day.
    Another reference I would like to add is https://realpython.com/if-name-main-python/#when-should-you-use-the-name-main-idiom-in-python

    Collatz.py -This was a little tricky, Maths was needed.
    While the number was not 1, %  was used for checking if a number could be divived by 2. (even number). If a number wasnt even, multiplication and addition was required.     The user is asked to enter a positive number, (printing if positive) If user entered a negitive number they were given a promt to please enter a positive integer. If it     was an odd number the program would print eg This is The Collatz Sequence
                                                Enter a positive integer: 5
                                                sucessive values of sequence: [5, 16]

    Squareroot.py 
    The function sqrt(x) calculates the square root of a positive number. It will check if the input is less than 0, if it is, it will give a Value Error and print message      about it ("input must be a positive number"). The function uses the Newton-Raphson method to estimate the square root iteratively.
    The tolerence level for convergence was set at tol = 1e-6 , and an initial estimate of the  square root.
    Inside the While loop an new estimate is calculated using new estimate. The loop continues until the absolute difference between the two is less than the specified     
    tolerance.
    Then there is a convergence check, if estimate has converged (inside tolerance) the function will return final estimate, otherwise the loop will continue after updating 
    the estimate.    
    # example
    number = 14.5
    result = sqrt(number)
    print(f"The square root of { 14.5} is aprox {result:.6f}")

    
    
    
    plottask.py - Even though I liked this task, a simple over sight of () puzzled me for a long time. I could not get my plot to show even though a lot of this was
    covered in another subject with another lecturer. I relied on Ian Mc Loughlin - a lecturer at [ATU] (https://www.atu.ie/) sample code to complete this task. Numpy and 
    Matplotlib.pyplot were imported.
    Matplotlib.pyplot is assigned as plt in the script. It is used to create the Histogram.
    Numpy, was required to generate the random numbers, as it creates efficient data structures for dealing with numerical data. It was also called on for linspace: that 
    returns evenly spaced numbers over a specified interval.
    Another simple puzzle for me was colour was "color" in code when I wished to have yellow and purple for something different. A little bit of research allowed me to see 
    my errors. The Real Python website was a good help here. As was W3schools where i saw how to enter a grid. (https://www.w3schools.com/python/matplotlib_grid.asp)
    
    es.py - So in this task "sys" was used. 
        According to stackoverflow (https://stackoverflow.com/questions/4765085/using-command-line-arguments-in-python-understanding-sys-argv)
        sys.argv is a list in Python that contains the command-line arguments passed to a script when it is run.
        The expression len(sys.argv) calculates the length of this list,which corresponds to the number of arguments.
        The condition len(sys.argv) != 2 checks if the number of arguments is not equal to 2 
        If the condition is true, it shows that the user didnt give the expected number of arguments,
        and the script can then handle this condition.
    The Task itself was looking for the amount of letter "e's" that were contained in a text file. The program will take the filename from argument on the command line.
    My program opened the text file, read it, and counted e. I allowed for Error handling. eg File not found.
    If the script is run directly ie not imported  - it can processes the command line argument.

 

    
## Getting started.
     There were requirements for Visual Studio Code (https://code.visualstudio.com/) in order to work with the repository in Github.
     The code used is python, so Annaconda (https://www.anaconda.com/download) was also down loaded and used. It has so many built in functions such as Pandas, Matplotlib        and Numpy.
     

## Author
    I study at [ATU] (https://www.atu.ie/). I am a mature student returning to education. I have a Bachelors of Business Studies from the former Institute of Technology     
    Sligo - now part of ATU. I find this an interesting subject and hope to continue learning online from the beautiful north west of Ireland. I will be looking for work in 
    the near future and at this moment I will leave my contact as my University Email. 
