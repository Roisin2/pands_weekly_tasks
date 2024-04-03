''' Weekly Task ; program takes positive floating point number as input
 and out puts an aproximation of its Square root.
'''
# Author: Roisin Stanley

# def <tt>sqrt</tt>(x):

def sqrt(x):

     if x < 0 :
          raise ValueError ("input must be a positive number")
     tol = 1e-6       # set tolerence level for convergence
          # start estimate of square root
     estimate = x/2

     while True:  # calculate new estimate using Newton
          new_estimate =  (estimate + x /estimate) /2                                                   
          if abs(new_estimate - estimate) < tol: # check if estimate has converged
               return new_estimate
               # update estimate
          estimate = new_estimate

# example
number = 14.5
result = sqrt(number)
print(f"The square root of { 14.5} is aprox {result:.6f}")