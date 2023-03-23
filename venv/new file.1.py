#time = "day"

#if time == "morning":
    #print("good morning")
#elif time == "day":
    #print("good afternoon")
#elif time == "evening":
    #print("good evening")

#else:
    #print("hello,i dont know time")


#a = ['h','5', 'o', 'i', 3, 8,]
#numbers = []
#letters = []
#for i in a:
 #if type(i) == int:
     #numbers.append(i)

 #else:
    #letters.append(i)
#print(letters)
#print(numbers)


#a = ['you',2,'me','i',3,4,]
#numbers = []
#words = []
#for i in a:
    #if type(i) == int:
       # numbers.append(i)

    #else:
       # words.append(i)
#print(numbers)
#print(words)



#циклы for.while.
#while True:
    #password = input('enter password: ')
   # if password == 'exit':
        #break

   # if len(password) >= 8:
       # if not password.isalnum():
           # print('пароль надежный')
             #break
       # else:
             #print('пароль ненадежный')
             
   # else:
       # print(f'длина пароля должна быть от 8 символов'
             # f'\nдлина вашего пароля {len(password)} ')


#while

#from time import sleep
#password = '123456'
#attempts = 3
#seconds = 10
#while True:
    #input_password = input(f'enter password (попыток {attempts}) ')
    #if attempts == 0:
        #while seconds != 0:
           # print(seconds)
           # seconds -= 1
            #ukta(1)
        #attempts = 3

  # if input_password == password:
      # print('доступ открыт!')
      # break
   #else:
       #attempts -= 1
      # print('пароль не верный!')


attempts = 3
seconds = 10
password = '123456'
while attempts != 0:
    input_password = input(f'enter pasword: attempts ({attempts})')
    if input_password != password:
         attempts -= 1
    else:
        print('верно!')
        break
if attempts == 0:
    while seconds != 0:
        print(seconds)
        seconds -= 1
        attempts = 3
 





