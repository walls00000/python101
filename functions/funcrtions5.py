def sayHello(name, age):    
    #message = "hello " + name + "I am " + age + " years old"
    message = "Hello {}, you are {} years old".format(name, age)
    return message
 
name1 = "Peter"
name2 = "Paul"
name3 = "Mary"
   
print(sayHello(name1, 11))
print(sayHello(name2, 12))
print(sayHello(name3, 13))