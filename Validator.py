import re
from datetime import datetime, date

def sanitize_input(input_display=""):
    while True:
        try:
            string = input(input_display)
        except EOFError:
            print("\n[ERROR] No input (EOF).")
            continue  
        except KeyboardInterrupt:
            print("\n[INFO] input cancelled by user.")
            continue 
        except:
            print("Unknown input error")

        # Check for too-long input
        if is_string_too_long(string, 124):
            print("Error: input too long.")
            continue

        # Whitelist filter (only allowed characters)
        white_list = r"^[a-zA-Z0-9~!@#$%&_\-+=/`|\\()\[\]{}:;'<>,.? ]+$"
        if not re.fullmatch(white_list, string):
            print("Error: forbidden characters detected.")
            continue

        break

    return string.strip()

def int_input(input_display=""):
    while True:
        try:
            optie = int(input(input_display))
            break
        except ValueError:
            print("invalid input, choose a number.")
            continue
        except EOFError:
            print("\n[ERROR] No input (EOF).")
            continue  
        except KeyboardInterrupt:
            print("\n[INFO] input cancelled by user.")
            continue 
        except:
            print("Unknown input error")
            
    return optie


def is_string_too_long(s: str, max_length: int) -> bool:
    return len(s) > max_length

def is_valid_latitude(lat: str) -> bool:
    pattern = r"^-?([0-8]?\d(\.\d{5})?|90\.00000)$"
    return re.match(pattern, lat) is not None

def is_valid_longitude(lon: str) -> bool:
    pattern = r"^-?(1?[0-7]?\d(\.\d{5})?|180\.00000)$"
    return re.match(pattern, lon) is not None

# checks if emails are valid
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# checks if phone numbers are valid
def is_valid_phone(phone):
    pattern = r'^31-6-\d{8}$'  
    return re.match(pattern, phone) is not None


def is_valid_zipCode(zipCode):
    pattern = r'^\d{4}[A-Z]{2}$'
    return re.match(pattern, zipCode) is not None


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

def validate_out_of_service(input_str):
    input_str = input_str.strip()
    if input_str in ['1', '0']:
        return True
    else:
        print("Invalid input 0 or 1.")
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

def is_valid_milage(value):
        try:
            milage = float(value)
            if milage < 0:
                print("Kilometervalue cant be negative .")
                return False
            elif milage > 1_000_000:
                print("Kilometervalue is too high.")
                return False
            return True
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

