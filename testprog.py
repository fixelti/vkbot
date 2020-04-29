students = dict()
# битва бомжей
# 1 фамилия 2 рейтин 3 комент 4 средний рейтинг 5 айди  
students['1'] = ['Агаркова',0,"",0,310410918]
students['2'] = ['Ажинов',0,"",0,263542561]
students['3'] = ['Акимов',0,"",0,262668821]
students['4'] = ['Алиев',0,"",0,469677495]
students['5'] = ['Антонян',0,"",0,556745169]


user_id = '262668821'
i = 1
while i <= len(students) : 
    peremenay = str(students[ str(i) ])
    peremenay1 = peremenay[peremenay.rfind(',') + 2:len (peremenay) - 1]
    print('permenay = '+ peremenay)
    print('permenay1 = '+ peremenay1)
    if user_id == peremenay1 :
        print( 'я нашел '  )
        peremenay2 = peremenay[peremenay.find(',') + 1:] 
        peremenay2 = peremenay2[:peremenay2.find(',') ]
        print('тот кусок '+ peremenay2)
        break

  
    i += 1