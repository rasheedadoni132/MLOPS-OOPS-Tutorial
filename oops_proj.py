class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to chatbook, How would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to Singin
                           3. Press 3 to Write a post
                           4. Press 4 to Message a friend
                           5. Press anyother key to exit""")
        
        if user_input == '1':
            self.Signup()
        elif user_input == '2':
            self.Signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()


    def Signup(self):
        email = input('Enter your email id')
        password = input('Enter your password')
        self.username = email
        self.password = password
        print('You have signedup successfuly')
        print('\n')
        self.menu()

    def Signin(self):
        if self.username == "" and self.password == "":
            print('First signup by selecting 1 option in the meain menu')
        else:
            username = input('Enter your email id/usename')
            password = input('Enter your password')
            if self.username == username and self.password == password:
                print('You have logged in successfuly')
                self.loggedin = True
            else:
                print('Kindly input correct credentials....')
        print('\n')
        self.menu()


    

obj = chatbook()
