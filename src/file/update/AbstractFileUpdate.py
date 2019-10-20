class AbstractFileUpdate:

    def __init__(self, oldVersion, newVersion, bot):
        self.oldVersion = oldVersion;
        self.newVersion = newVersion;

        self.bot = bot;


    # If the guildModel is in an older version we update it into a newer
    def process(self, guildModel):
        if(guildModel["__version__"] == self.oldVersion):
            self.bot.log.info("Updating file into V"+str(self.newVersion));

            guildModel = self.doUpdate(guildModel);
            guildModel["__version__"] = self.newVersion;

        return guildModel;

    # This method is overwritten in subclasses. It's were magic happen
    def doUpdate(self, guildModel):
        return guildModel;