rus = "йцукенгшщзхъфывапролджэячсмитьбю"
eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# print(len(rus),len(eng))
while True:
     word = input("\nPut word:").lower()
     if word == "exit":
         print("Thanks for used")
         break
     for letter in word:
        if letter in rus:
          print(eng[rus.index(letter)], end='')
        else:
          print(rus[eng.index(letter)], end='')



