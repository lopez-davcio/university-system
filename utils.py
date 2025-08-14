import re

def is_password_pattern_valid(password):
    """Compares provided password against the regex pattern"""
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    match = re.match(pattern, password)        
    return bool(match)

    
   
def print_password_requirements():        
        print("""\nThe new password must contain:
  - A capital letter
  - A small letter
  - A digit
  - At least 8 characters""")
        


def is_float(number):
    """Return a float number or False if number passed as argument can't be converted"""
    try:
        float_number = round(float(number), 2)
    except:
         return False
    else:
         return float_number
    


def is_integer(number):
    """Return an integer number or False if number passed as argument can't be converted"""
    try:
        int_number = round(int(number), 2)
    except:
         return False
    else:
         return int_number

