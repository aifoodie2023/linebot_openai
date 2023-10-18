
from linebot.models import *

def welcomeMessage():
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
                    ),
                TextSendMessage(
                    text = "請輸入您不吃的食物"
                )
            ]
    return message

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
                            label= "早餐",
                            text= "早餐" ),
                        MessageAction(
                            label= "早餐",
                            text= "早餐" ),
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://i.postimg.cc/59HJr5Gj/lunch.png',
                    title = "123",
                    text ="123",
                    actions =[
                        MessageAction(
                            label= "午餐",
                            text= "午餐" ),
                        MessageAction(
                            label= "午餐",
                            text= "午餐" ),
                        MessageAction(
                            label= "蛋奶素",
                            text= "我吃蛋奶素" ),
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    title = "請輸入您的個人喜好",
                    text ="請點你的飲食習慣",
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
        alt_text = "哪一餐",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url ='https://i.postimg.cc/7Z4ybFLT/chinese.png',
                    title = "123",
                    text ="123",
                    actions =[
                        MessageAction(
                            label= "中式",
                            text= "早餐" ),
                        MessageAction(
                            label= "a",
                            text= "早餐" ),
                        MessageAction(
                            label= "早餐",
                            text= "早餐" ),
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://i.postimg.cc/9X9STLKP/american.png',
                    title = "123",
                    text ="123",
                    actions =[
                        MessageAction(
                            label= "西式",
                            text= "午餐" ),
                        MessageAction(
                            label= "a",
                            text= "午餐" ),
                        MessageAction(
                            label= "蛋奶素",
                            text= "我吃蛋奶素" ),
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://i.postimg.cc/Lsf4Gthz/japanese.png',
                    title = "請輸入您的個人喜好",
                    text ="請點你的飲食習慣",
                    actions =[
                        MessageAction(
                            label= "日式",
                            text= "晚餐" ),
                        MessageAction(
                            label= "a",
                            text= "我吃全素" ),
                        MessageAction(
                            label= "蛋奶素",
                            text= "我吃蛋奶素" ),
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://i.postimg.cc/vZCHPq8Y/thais.png',
                    title = "請輸入您的個人喜好",
                    text ="請點你的飲食習慣",
                    actions =[
                        MessageAction(
                            label= "泰式",
                            text= "晚餐" ),
                        MessageAction(
                            label= "a",
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

def askAboutHobby():
    message = [
        eatingHabits(),
        TextSendMessage(
            text = "請輸入您不吃的食物"
        )
    ]
    return message

def chooseMeal():
    message = [
        whichMeal(),
        cuisineType()
    ]
    return message

def test():
    buttons_template_message = TemplateSendMessage(
        alt_text = "哪一餐",
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://i.postimg.cc/7Z4ybFLT/chinese.png',
                action=MessageAction(
                    label='中式',
                    text='中式'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i.postimg.cc/9X9STLKP/american.png',
                action=MessageAction(
                    label='西式',
                    text='西式'
                )
            )
        ]
    )
        )
    return buttons_template_message
