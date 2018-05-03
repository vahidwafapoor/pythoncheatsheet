
                    ▕▔▔╲╱▔▔▔╲╱▔▔▏
                    ┈╲＿╱╰╮┈╭╯╲＿╱
                    ┈┈┈▏▉╮┈╭▉▕
                    ┈┈╱╲╰╰┊╯╯╱╲
                    ┈╱╰▕╰╰┳╯╯▏╯╲
                    ▕╰╰╰╲╰┻╯╱╯╯╯▏
                    ▕╰╰╰╰▔▔▔╯╯╯╯▏
                    ▕╰╰╰╰╰╮╭╯╯╯╯▏
                    ┈╲╭╮┈╰╮╭╯╭╮╱
                    ┈┈┫┣╭━━━╮┫┃
                    ┈┈┃┃┃┈┈┈┃┃┃
                    ┈┈┗┛┛┈┈┈┗┗┛

name ="keyword operator from-rainbow">= "Joe Blue"  # storing a string

age = 35 # storing an int

weight = 160.57 # storing a float

dead = False # storing a boolean

ninjas = ['Rozen', 'KB', 'Oliver'] # storing lists

new_person = {"name":"John","age":35,"weight":160.2,"dead":False} # storing dictionaries

# list
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []
print(ninjas[0]) # prints Rozen
print(ninjas[1]) # prints KB
print(ninjas[2]) # prints Oliver
print(len(ninjas)) # prints the length of the ninjas list
ninjas.append("Michael") # adds Michael to the end of ninjas
ninjas.pop() # pops the last value in the list
ninjas.pop(1) # pops index 1 off the list
ninjas[2] = 'John' # updates index 2's value to John

# if statements
if age >= 18:
    print('Your age is above 18.')
elif age == 17:
    print('You are seventeen.')
else:
    print('You are so young!')

# for loops
for count in range(0,5):
    print("looping - ", count)

# looping through an array
for element in ninjas:
    print(element)

# define a function that returns the sum of two numbers
def sum(a,b):
    print("a:", a, "b:", b) # prints the values of a and b
    return a+b # returns the sum of a+b
print(sum(3,5))
print(sum(2,4)+sum(1,5))

# define a function that says hello to the name provided

# this starts a new block
def say_hello(name=""):
    #these lines are indented and therefore part of the function
    if name:
        print('Hello, ' + name + ', from inside the function')
    else:
        print('No name')

# now we're unindented and have ended the previous block
print('Outside of the function')

# Data type refers to how the computer knows to classify information. To determine data type, ask what category a value belongs to. Here's a list of the data types that you will surely be using in building web applications.
#
# There are several general classifications for data we're interested in. Primitive data types are the basic building blocks of a language. Most languages have these in common. Here are the most common:
#
# Boolean Values - Assesses the truth value of something. It has only two values: True and False
# Numbers - Integers (whole numbers), floating point numbers (commonly known as decimal numbers), and complex numbers.
# Strings - A text literal. Most pages in the web work with strings quite often.
# Composite types are collections composed of the above primitive types.
#
# Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
# Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
# Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values.
# We will cover these data types more in the following modules.
#
# In Python, (almost) everything is an object. We will touch on this later when we get into Object Oriented Programming (OOP).
#
# Indentation & Line-Endings
# One of the most important aspects of Python is indentation. Python has no brackets, braces, or keywords to indicate the start and end of certain code blocks such as functions, if statements, and loops. The only delimiter is the colon (:) and the indentation of the code itself. You'll see that indenting starts a new code block and un-indenting ends that block. Don't worry if these codes don't make sense right now; we'll go over function and if- statements later. Just take note of how the indentation looks.
#
# It is extremely important that your whitespace be consistent. The official PEP-8 Python Style Guide says to use 4 spaces whenever indenting and to stay away from tabs. However, as long as we are consistent with our whitespace, everything will be fine... until we try to merge our code with someone else's that uses a different indentation standard. Then we'll see this warnings like this in our terminal a lot:
#
# IndentationError: unindent does not match any outer indentation level
# We advise that you have your text editor render whitespace, especially while coding in Python. This will place a pale gray dot in each space so y


Instancing a User 
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = True
    def login(self):
        self.logged = True
        print(self.name + " is logged in.")
        return self
    def logout(self):
        self.logged = False
        print(self.name + " is not logged in")
        return self
    def show(self):
        print(f"My name is {self.name}. You can email me at {self.email}.")
        return self

#You can easiliy create a class in Python by typing the keyword class followed by the name of your class

class User:
    pass # pass is a placeholder 

class ClassName:
    # attributes and methods here (we'll talk more about these in a moment)

# Think of the class as a blueprint for creating something. Once we've finished our blueprint we can create instances of this class. The User class we defined above is a blueprint for creating users. We create a new instance by using the class name as if it were a function. Let's go ahead and make instances of our User class
Michael = User()
Anna = User()

Classes include two types of things:

# Attributes: Characteristics shared by all instances of the class type. Think about what we want to know about our users, for example. We may decide that all users should have a name and an email. We'll show you how to handle this in the next module.
# Methods: Actions that an object can perform. A user, for example, might be able to make a purchase. A method is like a function that belongs to a class. It's some instructions that will only work when called on an object that has been created from that class. We'll show you how shortly.



CREATING A CLASS 
# declare a class and give it name User
class User:
    # the __init__ method is called every time a new object is created
    def __init__(self, name, email):
        # set some instance variables. just like any variable we can call these anything                --- INSTANCE VARIABLES(ATTRIBUTES) ---
        self.name = name
        self.email = email
        self.logged = False
    # this is a method we created to help a user login             --- METHOD CREATION ----
    def login(self):
        self.logged = True
        print(self.name + " is logged in.")
        return self
#now create an instance of the class
new_user = User("Anna","anna@anna.com")
print(new_user.email)
# More about self later. After the __init__() method is another method called login(). All the method does for now is print a string. The logic we need to log a user into a web app is pretty complicated. It requires a database, for one. We'll be writing the code for that later in Flask.

SELF 
# You can change the state of an object by making modifications only to self. The self parameter includes all the information about teh individual object that has called the method. Without self every time we change 
#one of the object's attributes we would change the attribute for all the items of that type. 

__init__()
# Python's init method is known as a magic method, magic methods are automatically created and sometimes invoked when a new instance class is created. 

# example
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    
user1 = User("Anna Propas", "anna@anna.com")
print(user1.name)
print(user1.logged)
print(user1.email)
# Above, we are able to create objects that share characteristics but are still separate and distinct. When the object is created, we can specify the values we'd like to assign to each attribute. 
# In the __init__() method we are assigning the values we passed in as values of the attributes of each individual object.

# Note: We can create two objects that are identical in regards to the data they store, but they will be different. 
# This is because each object will be stored in different places in memory and is referred to according to that unique placement.
# The above concepts can be challenging to learn and confusing at first. It'll get easier over time, but first, you have to challenge yourself to learn something tough. Stick with it!

CHAINING Methods

user1.login().show().logout()
#IS POSSIBLE if you make sure to remember to return self for each method like below. 
class User:
    def login(self):
        // your code goes here...
        return self

_________________

Flask Example 

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! This is My First WebApp'


if __name__ == '__main__':
    app.run()

@app.route('/success')
def success():
  return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "hello "+name
    
@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id



_________________

Flask

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! This is My First WebApp'


if __name__ == '__main__':
    app.run()

@app.route('/success')
def success():
  return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "hello "+name
    
@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

