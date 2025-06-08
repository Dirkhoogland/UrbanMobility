import datetime
from Menus import toon_dynamisch_menu, genderOption, cityOption

def BirthdayManager():
    while True:
        try:
            Newbirthday = str(input("New Birthday (yyyy-mm-dd): ")).strip()
            frag = Newbirthday.split('-')

            if len(frag) != 3:
                print("Wrong format used, use the following format: (2025-01-01)")
                continue
            
            # year = int(frag[0]) 
            # month = int(frag[1])
            # day = int(frag[2])

            # 1 => 01 (month)
            if len(frag[1]) == 1: 
                frag[1] = "0" + frag[1]

            # 1 => 01 (day)
            if len(frag[2]) == 1: 
                frag[2] = "0" + frag[2]

            Newbirthday = frag[0] + "-" + frag[1] + "-" + frag[2]
            
            parsed_date = datetime.datetime.strptime(Newbirthday, "%Y-%m-%d").date() # used to check if date is valid

            return Newbirthday
        
        except:
            print("wrong format used, use fellowing format: (2025-01-01)")

def GenderManager():
    toon_dynamisch_menu(genderOption(), "Select Gender")
    gender = None # place holder
    while True:
        try:
            choice = int(input("select option: "))
        except ValueError:
            print("invalid input, choose between number: ")
            continue

        if choice == 1:
            return "F"
        
        if choice == 2:
            return "M"

        print("invalid input, choose between number: ")
        print("[1] ♀ Female")
        print("[2] ♂ Male")
        continue

def cityManager():
    toon_dynamisch_menu(cityOption(), "Select City")
    city = "UNKNOWN" # place holder
    while True:
        try:
            choice = int(input("select option: "))
        except ValueError:
            print("invalid input, choose between number: ")
            continue

        # ║ 1. Amsterdam                ║
        # ║ 2. Barendrecht              ║
        # ║ 3. Capelle aan den IJssel   ║
        # ║ 4. Krimpen aan den IJssel   ║
        # ║ 5. Rhoon                    ║
        # ║ 6. Ridderkerk               ║
        # ║ 7. Rotterdam                ║
        # ║ 8. Schiedam                 ║
        # ║ 9. The Hague                ║
        # ║ 10. Zoetemeer               ║

        if choice == 1:
            return "Amsterdam"
            
        if choice == 2:
            return "Barendrecht"

        if choice == 3:
            return "Capelle aan den IJssel"

        if choice == 4:
            return "Krimpen aan den IJssel"

        if choice == 5:
            return "Rhoon" 

        if choice == 6:
            return "Ridderker"
        
        if choice == 7:
            return "Rotterdam"
        
        if choice == 8:
            return "Schiendame"
        
        if choice == 9:
            return "The Hague"
        
        if choice == 10:
            return "Zoetemeer"
        
        print("invalid input, choose between number ")
        print("Example:")
        print("[1] Amesterdam")
        print("[2] Barendrecht")
        continue