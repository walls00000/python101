def sayHello(name, age): 
    """ sayHello: Say Hello to name and tell the age
    
    Parameters
    ----------
    name: The string name of the individual to say hello to
    age: The integer age of the individual
    
    Returns
    -------
    message: a string message containing the name and age
    
    """   
    message = "Hello {}, you are {} years old".format(name, age)
    return message
 
name1 = "Peter"
name2 = "Paul"
name3 = "Mary"

age1 = 11
age2 = 12
age3 = 13
   
print(sayHello(name1, age1))
print(sayHello(name2, age2))
print(sayHello(name3, age3))