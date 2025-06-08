import re
from datetime import datetime, date

def sanitize_input(user_input: str) -> str:

    # Verwijder SQL-injectiegevoelige tekens
    dangerous_patterns = r"['\";]|--|(/\*.*?\*/)|(\b(SELECT|INSERT|DELETE|DROP|UPDATE|UNION|OR|AND)\b)"
    safe_input = re.sub(dangerous_patterns, "", user_input, flags=re.IGNORECASE)

    # Optioneel: trim spaties
    return safe_input.strip()


# checks if emails are valid
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# checks if phone numbers are valid
def is_valid_phone(phone):
    pattern = r'^\+?\d{7,15}$'  
    return re.match(pattern, phone) is not None


def is_valid_username(username):
    pattern = r"^[a-z_][a-z0-9_.']{7,9}$"  # 1e char letter/_ + 7-9 rest = totaal 8-10
    return bool(re.fullmatch(pattern, username, re.IGNORECASE))

def is_valid_password(password):
 
    if not 12 <= len(password) <= 30:
        return False

    # Vereiste tekens, kleine letter, hooftletters, cijfers en tekens.
    if not re.search(r"[a-z]", password):  
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):  
        return False
    if not re.search(r"[~!@#$%&_\-+=`|\\(){}\[\]:;\"'<>,.?/]", password):
        return False

    return True
# checks if dates are valid and not in the future
def is_valid_iso_date(date_str):
    try:
        bday = date.fromisoformat(date_str)
        return bday <= date.today()  # geen toekomstige datums toegestaan
    except ValueError:
        return False

# checks if driving licence number is valid
def is_valid_DLN(DLN):
    pattern_1 = r'^[A-Z]{1}\d{8}$'
    pattern_2 = r'^[A-Z]{2}\d{7}$'
    return re.match(pattern_1, DLN) is not None or re.match(pattern_2, DLN) is not None


def is_valid_serialnumber(s):
    return isinstance(s, str) and 10 <= len(s) <= 17

# strips de datum van andere tekens en kijkt of het y-m-d is en ook of het niet in de toekomst is
def is_valid_maintenance_date(datum_str):
    try:
        datum_str = str(datum_str)
        onderhoudsdatum = datetime.strptime(datum_str, "%Y-%m-%d").date()
        return onderhoudsdatum <= date.today()
    except ValueError:
        return False


    # accepteert dus 2.5 kWh of 2kWh
def is_valid_battery_capacity(value):
    return bool(re.fullmatch(r"\d+(\.\d+)?\s*kWh", value.strip(), re.IGNORECASE))


# accepteert "45km/h" "25 km/h"
def is_valid_top_speed(value):
    return bool(re.fullmatch(r"\d+\s*km/h", value.strip(), re.IGNORECASE))

# accepteerd "90%", "100%"
def is_valid_soc(value):
    if not re.fullmatch(r"\d{1,3}%$", value.strip()):
        return False
    soc_value = int(value.strip().rstrip('%'))
    return 0 <= soc_value <= 100