import globals

def generateThingsToAsk():
    #隨機生成
    text = globals.habitCombine +'，'+'幫我隨機生成一個食譜(用繁體中文)'
    #生成食譜
    text = '幫我生成一個'+ globals.cuisineType +globals.mealType +'食譜(用繁體中文)'
    #輸入食材
    text = globals.habitCombine +'，'+ globals.ingredients+'，請幫我生成相關的食譜'
    return text

def exportHabit():
    globals.habitCombine = ''
    if(globals.eatingHabit!=''):
        globals.habitCombine = globals.habitCombine + '我' + globals.eatingHabit
    if(globals.eatingHabit!='' and globals.restriction!=''):
        globals.habitCombine = globals.habitCombine + ','
    if(globals.restriction!=''):
        globals.habitCombine = globals.habitCombine + '我' + globals.restriction
    return globals.habitCombine