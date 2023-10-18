def eatingHabit():
    message = [
        TextSendMessage(
            text = "Hello, 歡迎加入AI吃鬼，這裡可以自由生成食譜，也可以根據現成的食材生成喔!"
        ),
        TemplateSendMessage(
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
    ]
    return message



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

def saveIngredients (message):
    ingredients = message
    return  ingredients