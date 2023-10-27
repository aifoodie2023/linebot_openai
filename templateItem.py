
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
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://i.postimg.cc/rmmYSYDy/breakfast.png',
                action=MessageAction(
                    label='早餐',
                    text='早餐'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i.postimg.cc/Qtxvfdy3/lunch.png',
                action=MessageAction(
                    label='午餐',
                    text='午餐'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i.postimg.cc/hPfcSpMB/dinner.png',
                action=MessageAction(
                    label='晚餐',
                    text='晚餐'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i.postimg.cc/9MLH2770/nightsnack.png',
                action=MessageAction(
                    label='消夜',
                    text='消夜'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i.postimg.cc/wvqYnV3n/dessert.png',
                action=MessageAction(
                    label='點心',
                    text='點心'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i.postimg.cc/TPX6JGxd/drink.png',
                action=MessageAction(
                    label='飲料',
                    text='飲料'
                )
            )
        ]
    )
        )
    return buttons_template_message

def cuisineType():
    buttons_template_message = TemplateSendMessage(
        alt_text = "哪一餐",
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.postimg.cc/zBc2pShC/chinese.png',
                    action=MessageAction(
                        label='中式',
                        text='中式'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.postimg.cc/152P4wYN/american.png',
                    action=MessageAction(
                        label='西式',
                        text='西式'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.postimg.cc/zGhNhv92/japanese.png',
                    action=MessageAction(
                        label='日式',
                        text='日式'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.postimg.cc/D0mkwwrg/thai.png',
                    action=MessageAction(
                        label='泰式',
                        text='泰式'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.postimg.cc/QMkr6PNp/french.png',
                    action=MessageAction(
                        label='法式',
                        text='法式'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.postimg.cc/QMqRgTSm/random.png',
                    action=MessageAction(
                        label='隨便',
                        text='隨便'
                    )
                )
            ]
        )
        )
    return buttons_template_message

def askAboutHobby():
    message = [
        eatingHabits(),
        TextSendMessage(
            text = "請輸入您不吃的食物，(不吃...)"
        )
    ]
    return message

def chooseMeal():
    message = [
        TextSendMessage(
            text = "請先點要吃哪一餐，再選想吃什麼料理~"
        ),
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
                    label='早餐',
                    text='早餐'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i.postimg.cc/9X9STLKP/american.png',
                action=MessageAction(
                    label='午餐',
                    text='午餐'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i.postimg.cc/Lsf4Gthz/japanese.png',
                action=MessageAction(
                    label='晚餐',
                    text='晚餐'
                )
            )
        ]
    )
        )
    return buttons_template_message
