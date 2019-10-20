from file.update.AbstractFileUpdate import *

# This class is for a future update from Discord
class FileUpdateV2(AbstractFileUpdate):

    def __init__(self, bot):
        AbstractFileUpdate.__init__(self, 1, 2, bot);


    # Execute update here
    def doUpdate(self, guildModel):
        return guildModel;
