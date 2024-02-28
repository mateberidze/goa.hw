def main():
   
    correct_password = "12345"

    logged_in = False

    while not logged_in:
    
        user_password = input("Enter the password (or 'q' to quit): ")

       
        if user_password.lower() == 'q':
            print("Exiting...")
            break  

        if user_password == correct_password:
            print("Successfully logged in!")
          
        else:
            print("Incorrect password. Please try again.")

if __name__ == "__main__":
    main()
