class EmojiModel:
    def __init__(self):
        self.id = None;
        self.name = None;
        self.require_colons = None;
        self.managed = None;
        self.url = None;
    

    def fillFromEmoji(self, emoji):
        self.id = emoji.id;
        self.name = emoji.name;
        self.require_colons = emoji.require_colons;
        self.managed = emoji.managed;
        self.url = emoji.url;
