class EmojiModel:
    def __init__(self):
        self.id = None;
        self.name = None;
        self.url = None;


    def fillFromEmoji(self, emoji):
        self.id = emoji.id;
        self.name = emoji.name;
        self.url = emoji.url;
