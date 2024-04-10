import functions as fs
import trainerInterface as trainer
import memberInterface as member

# Member interface
def member_interface(member_id):
    print(f"\nWelcome Member {member_id}")
    while True:
        print(
            "\n1. Update Profile\n2. View Dashboard\n3. Schedule Personal Training Session\n4. Register for Group Fitness Class\n5. Logout"
        )
        choice = input("Enter choice: ")
        if choice == "1":
            print("---- Update Your Profile ----")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            height = input("Height (cm): ")
            weight = input("Weight (kg): ")
            fs.update_member_profile(member_id, first_name, last_name, height, weight)
        elif choice == "2":
            # Assume display_member_dashboard function exists and is implemented correctly
            pass
        elif choice == "3":
            # Assume schedule_session function exists and is implemented correctly
            pass
        elif choice == "4":
            # Assume register_for_class function exists and is implemented correctly
            pass
        elif choice == "5":
            break
        else:
            print("Invalid option.")


# Trainer interface
def trainer_interface(trainer_id):
    print(f"\nWelcome Trainer {trainer_id}")
    while True:
        print("\n1. Set Availability\n2. View Member Profiles\n3. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            trainer.setAvailability(trainer_id)
        elif choice == "2":
            trainer.searchForMember()
        elif choice == "3":
            break
        else:
            print("Invalid option.")


# Admin interface
def admin_interface():
    print("\nWelcome Admin")
    while True:
        print(
            "\n1. Manage Room Bookings\n2. Monitor Equipment Maintenance\n3. Update Class Schedules\n4. Process Payments\n5. Logout"
        )
        choice = input("Enter choice: ")
        if choice == "1":
            fs.manageRoomBookings()
        elif choice == "2":
            fs.monitorEquipmentMaintenance()
        elif choice == "3":
            fs.updateClassSchedule()
            pass
        elif choice == "4":
            fs.billingsAndPayment()
            pass
        elif choice == "5":
            break
        else:
            print("Invalid option.")


# Main menu
def main():
    while True:
        print("\nMain Menu")
        print("1. Login as a Member")
        print("2. Login as Trainer")
        print("3. Login as Admin")
        print("4. Register")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            member_id = input("Enter Member ID: ")
            if fs.check_id_exists(member_id, "member", "member_id"):
                member_interface(member_id)
            else:
                print("\nMember ID does not exist. Please try again.")
        elif choice == "2":
            trainer_id = input("Enter Trainer ID: ")
            if fs.check_id_exists(trainer_id, "trainer", "trainer_id"):
                trainer_interface(trainer_id)
            else:
                print("\nTrainer ID does not exist. Please try again.")
        elif choice == "3":
            employee_id = input("Enter Employee ID: ")
            if fs.check_id_exists(employee_id, "adminstaff", "employee_id"):
                admin_interface()
            else:
                print("\nEmployee ID does not exist. Please try again.")
        elif choice == "4":
           member.register()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option.")


main()
