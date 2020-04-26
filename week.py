from datetime import datetime


def Week(fuck):
    day = (datetime.now().strftime('%a'))
    ind_fri = fuck.rfind("Пятница")
    ind_sat = fuck.rfind("Суббота")
    time_now = int(datetime.now().strftime('%U'))

    if ((ind_fri != -1) and (day == 'Fri')) or ((ind_sat != -1) and (day == 'Sat')) or (day == 'Sun'):
        time_now += 1
        if time_now % 2 != 0:
            wik = "Cледующая неделя нижняя нижняя неделя"
            # num = 1
        else:
            wik = "Cледующая неделя верхняя неделя"
            # num = 2
    else:
        if time_now % 2 == 0:
            wik = "Сейчас нижняя неделя"
            # num = 1
        else:
            wik = "Сейчас верхняя неделя"
            # num = 2

    return wik
