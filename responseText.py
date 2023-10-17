#from app import eatingHabits
#from app import lineBotApiReply
from settingHobby import saveHabit
from settingHobby import dietaryRestriction

def messageApply(msg):
    if msg == '個人喜好':
        #葷/全素/蛋奶素
        #####msg = eatingHabits()
        #請輸入不吃的食物
        ##儲存
        msg = '個人喜好'
    elif msg == '料理生成':
        #請選擇下方選單中的服務進行食譜生成
        #早餐
        #泰式
        ##生成食譜
        msg = '料理生成'
    elif msg == '輸入食材':
        #請輸入現有食材
        #儲存現有食材
        ##生成食譜(以下是依據您輸入的食材製作出來的食譜)
        msg = '輸入食材'
        #購買連結
    elif msg == '隨機生成':
        ##生成食譜
        msg = '笑話'
    elif msg == '節慶食譜':
        ##生成節慶食譜
        msg = '節慶介紹'
    elif  '我不吃' in msg :
        dietaryRestriction(msg)
        msg='好的! 個人喜好設定已儲存'
    elif '我吃' in msg:
        saveHabit(msg)
        msg='儲存飲食習慣'
    return msg