from app import eatingHabits
#from app import lineBotApiReply

def messageApply(msg):
    if msg == '個人喜好':
        #葷/全素/蛋奶素
        msg = eatingHabits()
        #請輸入不吃的食物
        ##儲存
        ######msg = '你好'
    elif msg == '料理生成':
        #請選擇下方選單中的服務進行食譜生成
        #早餐
        #泰式
        ##生成食譜
        msg = '早餐'
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
    return msg