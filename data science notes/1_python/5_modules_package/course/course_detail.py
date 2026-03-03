# now main objective is to access the payment.py from this course.py file

# from payment import payment_detail

# def course():
#     print ("this is my course detail")

# payment_detail.payment()
# but we get error of module not found 
# so to avoid this error 



import os, sys
from os.path import dirname, join, abspath

# Add parent directory to sys.path so Python can find 'payment' package
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

# Import the module
from payment import payment_detail

def course():
    print("this is my course detail")

# Call the function from payment_detail module
payment_detail.payment()
