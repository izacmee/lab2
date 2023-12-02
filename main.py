def ChangeName():
    global Name
    print('text ur new name')
    Name = input()

print('Text ur name')
Name = input()

while(True):
    message = input()
    
    if message == 'change name':
        ChangeName()
        
    elif message == 'help':
        print('i have only 1 command: change name')
        
    elif message == 'my name':
        print(Name)
        
    else:
        print('what?')
