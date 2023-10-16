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
    alt_text = "股票資訊",
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                #thumbnail_image_url ="https://chenchenhouse.com//wp-content/uploads/2020/10/%E5%9C%96%E7%89%871-2.png",
                title = "請輸入您的個人喜好",
                #text ="請點選想查詢的股票資訊",
                actions =[
                    MessageAction(
                        label= "葷",
                        text= "葷" ),
                    MessageAction(
                        label= "全素",
                        text= "全素" ),
                    MessageAction(
                        label= "蛋奶素",
                        text= "蛋奶素" ),
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
    if msg == '個人喜好':
        buttons_template_message = TemplateSendMessage(
        alt_text = "股票資訊",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    #thumbnail_image_url ="https://chenchenhouse.com//wp-content/uploads/2020/10/%E5%9C%96%E7%89%871-2.png",
                    title = "請輸入您的個人喜好",
                    #text ="請點選想查詢的股票資訊",
                    actions =[
                        MessageAction(
                            label= "葷",
                            text= "葷" ),
                        MessageAction(
                            label= "全素",
                            text= "全素" ),
                        MessageAction(
                            label= "蛋奶素",
                            text= "蛋奶素" ),
                        ]
                    )
                ]
            )
        )
        reply = buttons_template_message
    else:
        reply = TextSendMessage(msg)
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
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)