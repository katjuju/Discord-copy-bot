from file.update.FileUpdateV2 import *

class GuildFileUpdater:

    def __init__(self, bot):
        self.bot = bot;

    # Apply every update to the guild model
    def updateToLatestVersion(self, guildModel):
        updater = self.findUpdater(guildModel["__version__"]);
        if(updater == None):
            self.bot.log.info("Guild file updated");
            return guildModel;

        guildModel = updater.process(guildModel);
        return self.updateToLatestVersion(guildModel);


    # Return the FileUpdate for a specific version
    def findUpdater(self, guildModelVersion):
        if(guildModelVersion == 1):
            return FileUpdateV2(self.bot);

        return None;
