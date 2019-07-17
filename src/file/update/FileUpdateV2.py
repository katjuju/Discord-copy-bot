from file.update.AbstractFileUpdate import *

class FileUpdateV2(AbstractFileUpdate):

    def __init__(self, bot):
        AbstractFileUpdate.__init__(self, 1, 2, bot);


    def doUpdate(self, guildModel):
        # Execute update here
        return guildModel;
