import random

max_num_limit=input('orru number id') 

if max_num_limit.isdigit():
    max_num_limit=int(max_num_limit)
    
    if max_num_limit==0:
        print('innorka number idreng 0 do ganti yara id')
        quit()
        
    else:
        print('number id monu endro akynoth ulle neen')
        
random_number=random.randint(0,max_num_limit)
guesses=0

while True:
    guesses+=1
    user_guess=input('Guess a number')
    if user_guess.isdigit():
       user_guess=int(user_guess)
    else:
       print('oru number id chengayi nikk etthare pata chelde')

    if user_guess == random_number:
       print('neen sama mone')
       break
    elif user_guess>random_number:
       print('neen guess akyo number yara aith')
    else:
       print('neen guess akyo number korodo aith')

print('nikk id '+ guesses+ ' l kittiyo congrats mone')
    
        

