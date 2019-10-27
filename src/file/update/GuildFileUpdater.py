from file.update.FileUpdateV2 import *

from utils.Logger import *

class GuildFileUpdater:

    def __init__(self):
        pass;

    # Apply every update to the guild model
    def updateToLatestVersion(self, guildModel):
        updater = self.findUpdater(guildModel["__version__"]);
        if(updater == None):
            Logger.info("Guild file updated");
            return guildModel;

        guildModel = updater.process(guildModel);
        return self.updateToLatestVersion(guildModel);


    # Return the FileUpdate for a specific version
    def findUpdater(self, guildModelVersion):
        if(guildModelVersion == 1):
            return FileUpdateV2();

        return None;
