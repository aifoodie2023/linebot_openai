def apply():
    # 處理訊息
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        msg = event.message.text
        GPT_answer = GPT_response(msg)
        print(GPT_answer)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(GPT_answer))

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