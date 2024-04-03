# Program that outputs whether or not today is a weekday.
# Author Roisin Stanley
'''
 reference https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior#
  reference :https://www.geeksforgeeks.org/isoweekday-method-of-datetime-class-in-python/
'''
import datetime    
# datetime module to get current date

def is_weekday():
    # Get the current day of the week (0 = Monday, 6 = Sunday)
    weekno = datetime.datetime.today().weekday()        # calls todays day

    if weekno < 5:  # 0-4 is mon-fri    
        return "Weekday"
    else:
        return "Weekend"

if __name__ == "__main__":          
    result = is_weekday()             # calls function from above 
    if result == "Weekday":
        print("Yes, unfortunately today is a weekday.")
    else:
        print("It is the weekend, yay!")


#An object is hashable if it has a hash value which never changes during its lifetime,
 # (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() method).
         # Hashable objects which compare equal must have the same hash value.
           


           
    
            