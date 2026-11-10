import csv

USERS_FILE = "data/users.csv"
ADMINS_FILE = "data/admins.csv"

def register_user(name, email, phone, username, password):

    file = open("data/users.csv", "a")

    file.write(
        name + "," +
        email + "," +
        phone + "," +
        username + "," +
        password + "\n"
    )

    file.close()

def check_admin(username, password):
    with open(ADMINS_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            if row[0] == username and row[1] == password:
                return True

    return False

def check_user(username, password):

    file = open("data/users.csv", "r")
    reader = csv.reader(file)

    for row in reader:

        if len(row) < 5:
            continue

        stored_username = row[3].strip()
        stored_password = row[4].strip()

        if stored_username == username and stored_password == password:
            file.close()
            return True

    file.close()
    return False