CONFERENCE_NAME = "EL Classico Conference"
NUMBER_OF_TICKETS = 50
remaining_tickets = 50
bookings = []

user = {}

def greetings(conference_name, number_of_tickets):
    print(f"Hello, you are welcome to {conference_name}, we only have {number_of_tickets} tickets available.\n")

def get_user_details():
    username = input("Kindly provide your name?\n")
    user_email = input("Kindly provide your email?\n")
    user_tickets = input("How many tickets are you booking?\n") 
    return username, user_email, user_tickets

def invalid_user_tickets(user_tickets, remaining_tickets):
    if not user_tickets.isdigit():
        print("Tickets must be a positive integer")
        return True
    if int(user_tickets) > remaining_tickets:
        print(f"We only have {remaining_tickets} left")
        return True
    return False

def valid_user_email(user_email):
    return "@" in user_email

def create_user(username, user_email, user_tickets):
    user = {
        "username": username,
        "email": user_email,
        "tickets": user_tickets 
    }
    return user
 
    
def main():
    remaining_tickets = 50
    while remaining_tickets > 0:
        greetings(CONFERENCE_NAME, remaining_tickets)
        
        username, user_email, user_tickets = get_user_details()
        
        if not valid_user_email(user_email):
            print("User email is invalid!!!")
            continue

        if invalid_user_tickets(user_tickets, remaining_tickets):
            continue
        
        user_tickets = int(user_tickets)
        user = create_user(username, user_email, user_tickets)

        bookings.append(user)

        remaining_tickets -= user_tickets

        print(f'Hello {username}, your {user_tickets} tickets have been successfully booked, check your email: {user_email} for your ticket number')
        print("Bookings:", bookings)
        print("Remaining tickets:", remaining_tickets)


if __name__ == "__main__":
    main()