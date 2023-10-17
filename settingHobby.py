def saveHabit(habit):
    if habit == '我吃葷':
        eatingHabit='我吃葷'
    elif habit == '我吃素':
        eatingHabit='我是素食者'
    elif habit == '我吃蛋奶素':
        eatingHabit='我吃蛋奶素'
    return eatingHabit    


def dietaryRestriction(message):
    restriction = message
    return