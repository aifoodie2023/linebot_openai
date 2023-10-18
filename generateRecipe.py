#from app import GPT_response
#import globals

def generateThingsToAsk():
    #combine all the things to ask for recipe
    return

'''
def generateRecipe(msg):
    GPT_answer = GPT_response(msg)
    print(GPT_answer)
    recipe = TextSendMessage(GPT_answer)
    globals.getRecipe = 0
    return recipe


def whichMeal():
    buttons_template_message = TemplateSendMessage(
        alt_text = "哪一餐",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url ='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    #title = "請輸入您的個人喜好",
                    #text ="請點你的飲食習慣",
                    actions =[
                        MessageAction(
                            label= "早餐",
                            text= "早餐" )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    actions =[
                        MessageAction(
                            label= "午餐",
                            text= "午餐" )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url ='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
                    actions =[
                        MessageAction(
                            label= "晚餐",
                            text= "晚餐" )
                        ]
                    )
                ]
            )
        )
    return buttons_template_message
    '''