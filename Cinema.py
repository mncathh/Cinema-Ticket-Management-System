import random
import string
from collections import deque

class CinemaTicketManagementSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.bookings = {}
        self.queue = deque()  
        self.stack = []       
    
    def generate_uid(self):
        uid = 'CT' + ''.join(random.choices(string.digits, k=5))
        return uid
    
    def book_seat(self, customer_name):
        if self.available_seats > 0:
            uid = self.generate_uid()
            self.bookings[uid] = customer_name
            self.queue.append(uid)
            self.stack.append(("BOOK", uid))
            self.available_seats -= 1
            print(f"Seat booked successfully for {customer_name}. UID: {uid}")
            print(f"Available seats: {self.available_seats}")
        else:
            print("No seats available.")
    
    def cancel_booking(self, uid):
        if uid in self.bookings:
            self.available_seats += 1
            customer_name = self.bookings.pop(uid)
            self.stack.append(("CANCEL", uid))
            print(f"Booking for {customer_name} (UID: {uid}) has been canceled.")
            print(f"Available seats: {self.available_seats}")
        else:
            print(f"No booking found for UID: {uid}")
    
    def view_bookings(self):
        if self.bookings:
            print("Current bookings:")
            for uid, name in self.bookings.items():
                print(f"UID: {uid}, Name: {name}")
        else:
            print("No current bookings.")
    
    def undo_last_action(self):
        if self.stack:
            last_action, uid = self.stack.pop()
            if last_action == "BOOK":
                customer_name = self.bookings.pop(uid, None)
                if customer_name:
                    self.available_seats += 1
                    print(f"Booking for {customer_name} (UID: {uid}) has been undone.")
            elif last_action == "CANCEL":
                print(f"Restoring booking for UID: {uid}")
                customer_name = f"Customer_{uid}"  
                self.bookings[uid] = customer_name
                self.available_seats -= 1
                print(f"Booking for {customer_name} (UID: {uid}) restored.")
        else:
            print("No actions to undo.")
    
    def display_available_seats(self):
        print(f"Available seats: {self.available_seats}")

    print("=======================================")
    print("=                                     =")
    print("=                                     =")
    print("=       CINEMA TICKET MANAGEMENT      =")
    print("=                                     =")
    print("=                                     =")
    print("=======================================")

def main():
    total_seats = int(input("Enter number of seats available: "))
    cinema_system = CinemaTicketManagementSystem(total_seats)
    
    while True:
        print("        _______________________________")
        print("       |                               |")
        print("       |         CINEMA TICKET         |")
        print("       |_______________________________|")
        print("       |             MENU:             |")
        print("       |    1. Book a seat             |")
        print("       |    2. Cancel a booking        |")
        print("       |    3. View current bookings   |")
        print("       |    4. Undo last action        |")
        print("       |    5. Display available seats |")
        print("       |    6. Exit                    |")
        print("       |_______________________________|\n")
        print("             ||               ||")
        print("             ||               ||")
        print("        ==============================")
        print("       |  [][][][][][][][][][][][]  |")
        print("       |  [][][][][][][][][][][][]  |")
        print("       |  [][][][][][][][][][][][]  |")
        print("        ==============================")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            customer_name = input("Enter customer name: ")
            cinema_system.book_seat(customer_name)
        
        elif choice == '2':
            uid = input("Enter booking UID to cancel: ")
            cinema_system.cancel_booking(uid)
        
        elif choice == '3':
            cinema_system.view_bookings()
        
        elif choice == '4':
            cinema_system.undo_last_action()
        
        elif choice == '5':
            cinema_system.display_available_seats()
        
        elif choice == '6':
            print("=======================================")
            print("=                                     =")
            print("=        THANK YOU FOR USING          =")
            print("=         CINEMA TICKET SYSTEM        =")
            print("=                                     =")
            print("=   We hope to see you again soon!    =")
            print("=                                     =")
            print("=              Exiting...             =")
            print("=                                     =")
            print("=======================================")

            break
        
        else:
            print("Invalid choice. Please try again.")

main()