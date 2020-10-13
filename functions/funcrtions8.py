def sayHello(people): 
    """ sayHello: Say Hello to name and tell the age
    
    Parameters
    ----------
    people: A dictionary of people containing name and age

    Returns
    -------
    
    """ 
    message = ""  
    for name in people:
        message += "Hello {}, you are {} years old\n".format(name, people[name])
        
    return message


def incrementAge(people):
    """ incrementAge: increment the age of members of people
    
    Parameters
    ----------
    people: A dictionary of people containing name and age
    """
    
    for name in people:
        print("incrementing age for " + name)
        people[name] += 1
    print()    
        
# members = {"Peter":11,"Paul":12, "Mary":13} 
members = {}
members["Peter"] = 11
members["Paul"] = 12
members["Mary"] = 13
   
helloMessage1 = sayHello(members)
incrementAge(members)
helloMessage2 =sayHello(members)
print(helloMessage1)
print(helloMessage2)
