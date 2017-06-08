class User(object):
    """docstring for User."""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False

    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self

robert = User('robert', 'me@robertv.co')
sandra = User('sandra', 'me@sandrav.co')

print robert.login()
print robert.logged
