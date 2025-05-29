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


def is_valid_serialnumber(s):
    return isinstance(s, str) and 10 <= len(s) <= 17

# strips de datum van andere tekens en kijkt of het y-m-d is en ook of het niet in de toekomst is
def is_valid_maintenance_date(datum_str):
    try:
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