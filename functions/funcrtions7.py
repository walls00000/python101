def sayHello(people): 
    """ sayHello: Say Hello to name and tell the age
    
    Parameters
    ----------
    people: A dictionary of people containing name and age of the individual

    Returns
    -------
    
    """ 
    message = ""  
    for name in people:
        message += "Hello {}, you are {} years old\n".format(name, people[name])
        
    return message

members = {"Peter":11,"Paul":12, "Mary":13} 
   
helloMessage = sayHello(members)
print(helloMessage)
