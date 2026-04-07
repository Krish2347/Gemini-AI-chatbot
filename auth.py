import bcrypt
def register():
    new_email = input("Email(e to go back): ")
    if new_email in ['e','E']:
        return "r_b"
    else:
        if '@' in new_email and '.' in new_email and new_email.index('@') < new_email.rindex('.'):
            duplicate = False
            with open("gemini_login.txt", "r") as database:
                for line in database:
                    if new_email in line:
                        duplicate = True
            if duplicate == False:
                new_password = input("Password: ")
                h_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
                new_username = input("What should I call you? ")
                with open("gemini_login.txt", "a") as database:
                    database.write(new_email + ", " + h_password.decode() + ", " + new_username + "\n")
                    print("Registration successful," + new_username + ". Please Login")
                    return "r_d"
            if duplicate == True:
                print("User with this email already exists")
                return "d_f"
        else:
            print("Invalid Email")
            return "i_e"

def login():
    entered_email = input("Email(e to go back): ")
    if entered_email in ['e', 'E']:
        return "l_b"
    else:
        entered_password = input("password: ")
        login = False
        with open("gemini_login.txt", "r") as database:
            for line in database:
                email, password, username = line.strip().split(", ")
                if entered_email == email and bcrypt.checkpw(entered_password.encode(), password.encode()) == True:
                    login = True
                    return username
                else:
                    login = False
                    return None