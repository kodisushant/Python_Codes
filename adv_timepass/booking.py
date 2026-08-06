import os

# ---------- CONFIG ----------
THEATRES = 2
SCREENS = 2
SHOWS = 3
SEATS = 50

DATA_DIR = "booking_data"

# ---------- SETUP ----------
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# ---------- FILE HANDLING ----------
def get_file_path(theatre, screen, show):
    return f"{DATA_DIR}/T{theatre}_S{screen}_SH{show}.txt"


def load_seats(theatre, screen, show):
    path = get_file_path(theatre, screen, show)
    
    if not os.path.exists(path):
        seats = ["0"] * SEATS
        with open(path, "w") as f:
            f.write(",".join(seats))
        return seats
    
    with open(path, "r") as f:
        return f.read().split(",")


def save_seats(theatre, screen, show, seats):
    path = get_file_path(theatre, screen, show)
    with open(path, "w") as f:
        f.write(",".join(seats))


# ---------- DISPLAY ----------
def show_seats(seats):
    for i in range(SEATS):
        print(f"{i+1}:{'X' if seats[i]=='1' else 'O'}", end="  ")
        if (i + 1) % 10 == 0:
            print()
    print("\nO = Available | X = Booked\n")


# ---------- BOOK ----------
def book_seat():
    theatre = int(input("Select Theatre (1-2): "))
    screen = int(input("Select Screen (1-2): "))
    show = int(input("Select Show (1-3): "))
    
    seats = load_seats(theatre, screen, show)
    
    clear()
    print("Seat Layout:")
    show_seats(seats)
    
    seat_no = int(input("Enter seat number to book: "))
    
    if seats[seat_no - 1] == "1":
        print("❌ Seat already booked.")
    else:
        seats[seat_no - 1] = "1"
        save_seats(theatre, screen, show, seats)
        print("✅ Booking successful.")


# ---------- MAIN ----------
def main():
    while True:
        clear()
        print("=== Movie Booking System ===")
        print("1. Book Seat")
        print("2. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            book_seat()
            input("Press Enter to continue...")
        elif choice == "2":
            break
        else:
            print("Invalid choice")
            input("Press Enter...")


if __name__ == "__main__":
    main()