from app import GPT_response
import globals

def generateThingsToAsk():
    #combine all the things to ask for recipe
    return

def generateRecipe(msg):
    GPT_answer = GPT_response(msg)
    print(GPT_answer)
    recipe = TextSendMessage(GPT_answer)
    globals.getRecipe = 0
    return recipe