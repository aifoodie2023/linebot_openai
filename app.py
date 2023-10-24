from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#import from another script
from responseText import messageApply
from templateItem import welcomeMessage, eatingHabits, whichMeal, cuisineType, chooseMeal, test, askAboutHobby
from settingHobby import saveHabit, exportHabit, habitCombine
import globals
#======python的函數庫==========
import tempfile, os
import datetime
import openai
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
# Channel Secret
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))
# OPENAI API Key初始化設定
openai.api_key = os.getenv('OPENAI_API_KEY')

def GPT_response(text):
    # 接收回應
    response = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0.5, max_tokens=500)
    print(response)
    # 重組回應
    answer = response['choices'][0]['text'].replace('。','')
    return answer


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def generateRecipe(msg):
    GPT_answer = GPT_response(msg)
    print(GPT_answer)
    recipe = TextSendMessage(GPT_answer)
    #globals.getRecipe = 0
    return recipe






def lineBotApiReply(evemt, message):
    line_bot_api.reply_message(evemt, message)

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply = None  # 在函数外初始化 reply 变量
    msg = messageApply(event.message.text)
#-------------------------個人喜好----------------------------------------------#
    if  msg == '個人喜好' :
        reply = askAboutHobby()
#-------------------------料理生成----------------------------------------------#
    elif msg == '料理生成' :
        reply = whichMeal()
    elif msg in ['早餐', '午餐', '晚餐', '消夜','點心','飲料']:
        reply = cuisineType()
    elif '為你生成' in msg :
        reply = [
                TextSendMessage(
                    text = '以下是'+globals.cuisineType+globals.mealType+'的食譜'
                ),
                generateRecipe('幫我生成一個'+ globals.cuisineType +globals.mealType +'食譜(用繁體中文)')
        ]
#-------------------------隨機生成----------------------------------------------#
    elif msg == '隨機生成' :
        reply = [
            TextSendMessage(
                    text = "隨機生成食譜如下"
            ),
            generateRecipe('幫我隨機生成一個食譜(用繁體中文)')
        ]
#-------------------------輸入食材---------------------------------------------#
    elif msg == '以下是依據您輸入的食材製作出來的食譜' :
         reply = [
                TextSendMessage(
                    text = "以下是依據您輸入的食材製作出來的食譜"
                ),
                TextSendMessage(
                    text = '#剛剛輸入:' + globals.ingredients
                ),
                TextSendMessage(
                    text = exportHabit()
                ),
                generateRecipe(globals.ingredients+'，請幫我生成相關的食譜')
         ]
#-------------------------節慶食譜----------------------------------------------#
    elif msg == '節慶食譜':
        reply = [
               TextSendMessage(
                    text = "以下是聖誕節的食譜"
                ),
                generateRecipe('請幫我生成聖誕節的食譜')
        ]
    
    else:
        reply = TextSendMessage(msg)
        '''
        GPT_answer = GPT_response(msg)
        print(GPT_answer)
        reply = TextSendMessage(GPT_answer)
        '''
    '''
    GPT_answer = GPT_response(msg)
    print(GPT_answer)
    lineBotApiReply(event.reply_token, TextSendMessage(GPT_answer))
    '''
    lineBotApiReply(event.reply_token , reply)


@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    print(uid)
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    #message = TextSendMessage(text=f'{name}歡迎加入')
    message = TextSendMessage(text='Hello, 歡迎加入AI吃鬼，這裡可以自由生成食譜，也可以根據現成的食材生成喔!')
    line_bot_api.reply_message(event.reply_token, message)
   
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    globals.intitials()