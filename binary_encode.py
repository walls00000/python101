# Python3 code to demonstrate working of 
# Converting String to binary 
# Using join() + ord() + format() 
  
# initializing string  
test_str = "GeeksforGeeks"
  
# printing original string  
print("The original string is : " + str(test_str)) 
  
# using join() + ord() + format() 
# Converting String to binary 
# res = ''.join(format(ord(i), 'b') for i in test_str) 
### OR ###
# using join() + bytearray() + format() 
# Converting String to binary 
res = ''.join(format(i, 'b') for i in bytearray(test_str, encoding ='utf-8'))
  
# printing result  
print("The string after binary conversion : " + str(res))