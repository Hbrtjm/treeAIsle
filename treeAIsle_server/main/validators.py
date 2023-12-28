import re as regex

def validate_email(email):
    email_validator_expression = r'^[a-zA-Z0-9_.+-]{1,}@([a-zA-Z0-9-]{1,}\.){1,3}[a-zA-Z0-9-]{1,}$'
    
    pattern = regex.compile(email_validator_expression)
    if regex.match(pattern,email):
        return True
    else:
        return False
    
def validate_phone_number(phone_number):
    # The expression below looks for phone numbers that begin with +, could be problematic,
    # But it might as well be stripped of dashes and whitespaces
    
    # phone_number.split(' ').join('').split('-').join('')
    # phone_regex  = r'^\+?[0-9]{3,20}$'
    
    phone_regex = r'^\+?[0-9\s-]{3,20}$'

    pattern = regex.compile(phone_regex)

    if regex.match(pattern, phone_number):
        return True
    else:
        return False