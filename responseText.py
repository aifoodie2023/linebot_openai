
#from app import eatingHabits
#from app import lineBotApiReply
from settingHobby import saveHabit, dietaryRestriction, saveIngredients
import globals
from templateItem import welcomeMessage, eatingHabits, whichMeal, cuisineType, chooseMeal, test, askAboutHobby
#from generateRecipe import generateRecipe

def messageApply(msg):

    if msg == '個人喜好':

        #葷/全素/蛋奶素
        #####msg = eatingHabits()
        #請輸入不吃的食物
        ##儲存
        reply = '個人喜好'
        

    elif msg == '料理生成':
        #請選擇下方選單中的服務進行食譜生成
        #早餐
        #泰式
        ##生成食譜
        reply = '料理生成'
#-------------------------------------------------------#
    elif msg == '輸入食材':
        #請輸入現有食材      
        reply = '請輸入現有食材，以我現在有開頭。'

        #購買連結
    elif '我現在有' in msg:
        #儲存現有食材
        saveIngredients(msg)
        reply='以下是依據您輸入的食材製作出來的食譜'
        globals.getRecipe = 1
        ##生成食譜(以下是依據您輸入的食材製作出來的食譜)
#-------------------------------------------------------#
    elif msg == '隨機生成':
        ##生成食譜
        #msg = '幫我隨機生成一個食譜'
        globals.getRecipe = 1
        reply = '隨機生成'
 #-------------------------------------------------------#       
    elif msg == '節慶食譜':
        ##生成節慶食譜
        reply = '節慶食譜'
#-------------------------------------------------------#
    elif  '不吃' in msg :
        dietaryRestriction(msg)
        reply='好的! 個人喜好設定已儲存'

    elif msg == '我吃葷' :
        saveHabit(msg)
        reply='儲存飲食習慣'

    elif msg == '我吃全素' :
        saveHabit(msg)
        reply='儲存飲食習慣'

    elif msg == '我吃蛋奶素' :
        saveHabit(msg)
        reply='儲存飲食習慣'
#-------------------------------------------------------#
    elif msg == '早餐':
        globals.mealType = '早餐'
    elif msg == '午餐':
        globals.mealType = '午餐'
    elif msg == '晚餐':
        globals.mealType = '晚餐'
    elif msg == '消夜':
        globals.mealType = '消夜'
    elif msg == '點心':
        globals.mealType = '點心'
    elif msg == '飲料':
        globals.mealType = '飲料'
#-------------------------------------------------------#
    elif msg == '中式':
        globals.cuisineType = '中式'
        reply = '為你生成-'+globals.cuisineType+globals.mealType
    elif msg == '西式':
        globals.cuisineType = '西式'
        reply = '為你生成-'+globals.cuisineType+globals.mealType
    elif msg == '日式':
        globals.cuisineType = '日式'
        reply = '為你生成-'+globals.cuisineType+globals.mealType
    elif msg == '泰式':
        globals.cuisineType = '泰式'
        reply = '為你生成-'+globals.cuisineType+globals.mealType
    elif msg == '法式':
        globals.cuisineType = '法式'
        reply = '為你生成-'+globals.cuisineType+globals.mealType
    elif msg == '隨便':
        globals.cuisineType = '隨便'
        reply = '為你生成-'+globals.cuisineType+globals.mealType

    return reply



def havingIngredient():
    return