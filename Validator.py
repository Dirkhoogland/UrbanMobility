import re
from datetime import date
# checks if emails are valid
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# checks if phone numbers are valid
def is_valid_phone(phone):
    pattern = r'^\+?\d{7,15}$'  
    return re.match(pattern, phone) is not None



# checks if dates are valid and not in the future
def is_valid_iso_date(date_str):
    try:
        bday = date.fromisoformat(date_str)
        return bday <= date.today()  # geen toekomstige datums toegestaan
    except ValueError:
        return False



