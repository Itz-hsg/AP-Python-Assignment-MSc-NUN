class User:
    login_attempts = 0

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print('Users names are {} {}, and a {} years old {}'.format(self.first_name, self.last_name, self.age, self.gender))

    def greet_user(self):
        print('Good day, {} {}'.format(self.first_name, self.last_name))
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

    
user = User('Abbas', 'Ogaji', 25, 'male')

user.increment_login_attempts()
print(user.login_attempts)

user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)