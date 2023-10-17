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