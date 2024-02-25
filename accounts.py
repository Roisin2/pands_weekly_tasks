# A python program called accounts.py that reads in a 10 character account number. 
# And outputs the account number with the last 4 digits showing and primary 6 digits replaced with X.
 
#Author: Roisin Stanley

    #prompt for entering number
account_1 = input("please enter 10 digit code: ")
    #check for length of 10 didgit code (and if are digits)
if len(account_1)!= 10 or not account_1 .isdigit():
    print("invalid account number")
else:  #if 10 digits ok only show last 4 numbers
    masked_number = "xxxxxx" + account_1[-4: ]
    print("your masked a/c number is:", masked_number)

#(reference)
#https://www.bing.com/search?q=masking+numbers+in+python+code
#https://stackoverflow.com/questions/4511257/mask-account-number-with-string-formatS
    
# Extra: Modify the program to deal with account numbers of any length ...Possibly because of revolute or other international banks.
    
   # if not account_1.isdigit():
   #     print("invalid account number")
                                    # as long as digits entered as an a/c number but only allow last 4 numbers to be visable
    #else:
        #masked_number ="x"* (len(account_1)-4) + account_1[-4: ] 
        #print("your masked a/c number is:",masked_number)
    
# Reference
    #stackoverflow.com/questions/17550024/masking-a-number-by-showing-last-x-digits-with-1-mask-character-in-front?rq=3
    #https://datagy.io/python-isdigit/
 