import getpass

# Simulating a user database
users = {
    'john_doe': {
        'password': 'password123',
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'posts': [],
    }
}

def register():
    username = input("Username: ")
    if username in users:
        print("Username already taken.")
        return
    
    password = getpass.getpass("Password: ")
    name = input("Name: ")
    email = input("Email: ")
    
    users[username] = {
        'password': password,
        'name': name,
        'email': email,
        'posts': [],
    }
    
    print("Registration successful.")

def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    if username not in users or users[username]['password'] != password:
        print("Invalid username or password.")
        return
    
    print("Login successful.")
    user_menu(username)

def create_post(username):
    post = input("Write your post: ")
    users[username]['posts'].append(post)
    print("Post created successfully.")

def view_posts(username):
    print("---- Recent Posts ----")
    for post in users[username]['posts']:
        print(post)
    print("----------------------")

def user_menu(username):
    while True:
        print("\n--- User Menu ---")
        print("1. Create Post")
        print("2. View Posts")
        print("3. Logout")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            create_post(username)
        elif choice == '2':
            view_posts(username)
        elif choice == '3':
            print("Logged out successfully.")
            return
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting the program.")
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()
