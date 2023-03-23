day = int(input("ваш день рождения"))
mon = int(input("ваш месяц рождения"))
if(mon == 3 and 21 <=day<=31)or(mon == 4 and 1 <= day <= 20 ):
  print("овен")

elif(mon == 4 and 21 <= day <= 30) or (mon == 5 and 1 <= day <= 21 ):
  print("телец")

elif(mon == 5 and 22 <= day <=31 ) or (mon == 6 and 1 <= day <= 21):
  print("близнецы")

elif(mon == 6 and 22 <= day <= 30) or (mon == 7 and 1 <= day <= 22):
  print("рак")

elif(mon == 7 and 23 <= day <= 30) or (mon == 8 and 1 <= day <= 21):
  print("лев")

elif(mon == 8 and 22 <= day <= 31) or (mon == 9 and 1 <= day <= 23):
  print("дева")

elif(mon == 9 and 24 <= day <= 31) or (mon == 10 and 1 <= day <= 23):
  print("весы")

elif(mon == 10 and 24 <= day <= 30) or (mon == 11 and 1 <= day <= 22):
  print("скорпион")

elif(mon == 11 and 23 <= day <= 30) or (mon == 12 and 1 <= day <= 22):
  print("стрелец")

elif(mon == 12 and 23 <= day <= 29) or (mon == 1 and 1 <= day <= 20 ):
  print("козерог")

elif(mon == 1 and 21 <= day <= 30) or (mon == 2 and 1 <= day <= 19):
  print("водолей")

elif(mon == 2 and 20 <= day <= 30) or ( mon == 3 and 1 <= day <= 20):
  print("рыбы")

else:
    print("дата указана неверно")