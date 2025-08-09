import pdb

class User:

    _users = {}
    
    def __init__(self, name, title, password):
        self._name = name
        self._title = title
        self.__password = password
        self._id = User.generate_id()
        User._users[self._id] = self
        self.__post_init__()

    def __post_init__(self):
        pass

   
    
    def check_stored_password(self, attempted_password):
        """Checks if the attempted password matches the stored password"""
        return attempted_password == self.__password
    

    def login(self):
        """prompts the user to enter their password and validates it through check_stored_password(). It gives 3 attempts.
        Accordingly, informs user of successful login and returns True, or informs login failed and returns False."""
        max_attempts = 3
        attempts_left = max_attempts
        
        while attempts_left > 0:
            attempted_password = input('Please enter your password, or type "q" to quit: ')
            
            if attempted_password == "q":
                print("Login cancelled.")
                return False
            
            if self.check_stored_password(attempted_password):
                print("Access granted.")
                return True            
            
            else:
                attempts_left -= 1
                print("Access denied. The password you entered is not recognized.")                
                if attempts_left > 0:
                    print(f"You have {attempts_left} attempts left.")
                else:
                    print("No attempts remaining. Login failed.")
                    return False
                

    @property
    def id(self):
        return self._id


    @classmethod
    def get_users_items(cls):
        return cls._users

    @classmethod
    def set_user(cls, user):
        """not sure yet if i need it"""
        pass


    @classmethod
    def available_id(cls, id):
        """returns True if user ID is available, False if it's not available"""
        return id not in cls._users
    

    @classmethod    
    def generate_id(cls):
        """Generates a random 3 digit ID as string, using available_id() for validation"""
        import random
        while  True:                        
            id = str(random.randint(100,999))            
            if cls.available_id(id):                
                break                            
        return id     

