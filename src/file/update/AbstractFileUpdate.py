class AbstractFileUpdate:

    def __init__(self, oldVersion, newVersion, bot):
        self.oldVersion = oldVersion;
        self.newVersion = newVersion;

        self.bot = bot;


    def process(self, guildModel):
        if(guildModel["__version__"] == self.oldVersion):
            self.bot.log.info("Updating file into V"+str(self.newVersion));

            guildModel = self.doUpdate(guildModel);
            guildModel["__version__"] = self.newVersion;

        return guildModel;


    def doUpdate(self, guildModel):
        return guildModel;
