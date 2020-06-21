class MessageClient():
    def __init__(self, sender, sent_dt, content):
        self.sender = sender
        self.sent_dt = sent_dt
        self.content = content
        
class ChannelMessageClient(MessageClient):
    def __init__(self, sender, sent_dt, content, channel_id):
        super().__init__(sender, sent_dt, content)
        self.channel_id = channel_id
      
class PrivateMessageClient(MessageClient):
    def __init__(self, sender, sent_dt, content, receiver):
        super().__init__(sender, sent_dt, content)
        self.receiver = receiver
        