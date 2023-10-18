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
from settingHobby import saveHabit
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
    globals.getRecipe = 0
    return recipe

def eatingHabits():
    buttons_template_message = TemplateSendMessage(
        alt_text = "葷素",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url ='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    title = "請輸入您的個人喜好",
                    text ="請點你的飲食習慣",
                    actions =[
                        MessageAction(
                            label= "葷",
                            text= "我吃葷" ),
                        MessageAction(
                            label= "全素",
                            text= "我吃全素" ),
                        MessageAction(
                            label= "蛋奶素",
                            text= "我吃蛋奶素" ),
                        ]
                    )
                ]
            )
        )
    return buttons_template_message

def whichMeal():
    buttons_template_message = TemplateSendMessage(
        alt_text = "哪一餐",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url ='https://i.postimg.cc/W4hn9MSc/breakfast.jpg',
                    title = "123",
                    text ="123",
                    actions =[
                        MessageAction(
                            label= "早餐",
                            text= "早餐" ),
                        MessageAction(
                            label= "早餐1",
                            text= "早餐1" ),
                        MessageAction(
                            label= "早餐2",
                            text= "早餐2" ),
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    title = "請輸入您的個人喜好",
                    text ="請點你的飲食習慣",
                    actions =[
                        MessageAction(
                            label= "午餐",
                            text= "午餐" ),
                        MessageAction(
                            label= "午餐1",
                            text= "午餐1" ),
                        MessageAction(
                            label= "午餐2",
                            text= "午餐2" ),
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    title = "",
                    text ="",
                    actions =[
                        MessageAction(
                            label= "晚餐",
                            text= "晚餐" ),
                        MessageAction(
                            label= "全素",
                            text= "我吃全素" ),
                        MessageAction(
                            label= "蛋奶素",
                            text= "我吃蛋奶素" ),
                        ]
                    )
                ]
            )
        )
    return buttons_template_message

def cuisineType():
    buttons_template_message = TemplateSendMessage(
        alt_text = "料理種類",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url ='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    #title = "請輸入您的個人喜好",
                    #text ="請點你的飲食習慣",
                    actions =[
                        MessageAction(
                            label= "中式",
                            text= "中式" )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    actions =[
                        MessageAction(
                            label= "西式",
                            text= "西式" )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    actions =[
                        MessageAction(
                            label= "日式",
                            text= "日式" )
                        ]
                    )
                ]
            )
        )
    return buttons_template_message

def lineBotApiReply(evemt, message):
    line_bot_api.reply_message(evemt, message)

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = messageApply(event.message.text)
    if  '個人喜好' in msg :
        reply = eatingHabits()
        #lineBotApiReply(event.reply_token , reply)
        #reply = TextSendMessage(text='請輸入您不吃的食物')
    elif msg == '料理生成' :
        reply = whichMeal()
    elif '隨機生成' in msg :
        reply = generateRecipe('幫我隨機生成一個食譜')
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
    globals.uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, globals.uid)
    name = profile.display_name
    #message = TextSendMessage(text=f'{name}歡迎加入')
    message = TextSendMessage(text='Hello, 歡迎加入AI吃鬼，這裡可以自由生成食譜，也可以根據現成的食材生成喔!')
    line_bot_api.reply_message(event.reply_token, message)
   
        
        
import os
if __name__ == "__main__":
    globals.intitials()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    print(globals.uid)
    