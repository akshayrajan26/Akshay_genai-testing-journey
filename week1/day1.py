
message ='Dinkan'
print(message)    #1

message_dinakn = 'Dinku\'s'  #2  add the backward slash to escape the single quote in Dinku's
print(message_dinakn)
#second method 
message_dinakn = "Dinku's"  #3 use double quotes to avoid escaping
print(message_dinakn)
#4  third method  long line can be continued here using triple quotes

message_dinakanthought ="""This is dinkan's super power. He can fly and has super strength. He is the best superhero in the world."""
print(message_dinakanthought)

#5 To  print the length of the message_dinkanthought
print(len(message_dinakanthought))
print(message_dinakanthought.upper())  #6 to convert the message to uppercase
print(message_dinakanthought.lower())  #7 to convert the message to lowercase     
print(message_dinakanthought[0])  #8  print each character of the message one by one  
print("=======================================================")
print(message_dinakanthought[0:5]) #9  print the first 5 characters of the message  , first index is inclusive and second index is exclusive
print(message_dinakanthought[5:])  #10  print the characters from index 5 to the end of the message
print(message_dinakanthought[:5])  #11 print the first 5 characters of the message, same as message_dinakanthought[0:5]
print(message_dinakanthought[::2])  #12 print every second character of the message
print(message_dinakanthought[1::2])  #print every second character of the message starting from index 1

print("=======================================================")
#count method
print(message_dinakanthought.count('a'))  #14 count the number of times 'a' appears in the message
print(message_dinakanthought.find('super'))  #15 find the index of the first occurrence of 'super' in the message 

replace_message = message_dinakanthought.replace('dinkan', 'dinku')  #16 replace 'dinkan' with 'dinku' in the message
print(replace_message)

msq1="Greeting"
name="Akshay"
message =msq1 + "  " + name +"!"
print(message)

message = '{} {}! Namaskaram'.format(msq1, name)  #17  using the format method to format the message
print(message)
#f Strings

Test =f"hello {name}"
print(Test)

print(dir(name))  #18 to see all the methods available for the string variable name
print(help(name.upper))  #to see the documentation of the upper method for string variable name
