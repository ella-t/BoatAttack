import slackapp

if __name__ == '__main__':
    conversation_id = slackapp.get_conversation_id()
    if conversation_id is not None:
        slackapp.post_latest_test(conversation_id)