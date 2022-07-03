## The say hello class creates an instance that says hello
class Hello:
    '''
    A simple class to personalise a greeting
    '''
    sayhello: str
    name: str
    greeting: str
    def __init__(self, greeting, name):
        assert type(name) is str, "Name must be a valid python string."
        assert type(greeting) is str, "Greeting must be a valid python string."
        self.name = name
        self.greeting = greeting


    def __repr__(self):

        return f'{type(self).__name__,}(' \
               f'{self.greeting!r}, {self.name!r})'

    def sayhello(self):
        return f'{self.greeting} {self.name}!'

class Hi(Hello):
    '''
    A simple class to personalise a greeting, but always says "Hi"
    '''
    sayhello: str
    name: str
    def __init__(self, name):
        self.greeting = "Hi"
        super().__init__(self, name)


