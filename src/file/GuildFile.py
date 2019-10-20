import json
import requests

import os
import shutil

from file.update.GuildFileUpdater import *

from utils.EmbedStatus import *
from utils.const import *;

class GuildFile:
    def __init__(self, bot):
    	self.bot = bot;


    def loadGuild(self, guildId):
        file = open("guilds/"+guildId+"/guild.json", "r");

        guildModel = json.load(file);

        updater = GuildFileUpdater(self.bot);
        return updater.updateToLatestVersion(guildModel);


    async def saveGuild(self, guildModel, channel=None):
        basePath = "guilds/"+str(guildModel.id)+"_"+guildModel.name.replace(" ", "_")+"/";

        self.embedStatus = EmbedStatus("Copying Discord");
        self.embedStatus.addField("Set up save folder");
        self.embedStatus.addField("Guild informations");
        self.embedStatus.addField("Guild's Icon");
        self.embedStatus.addField("Guild's emojis");

        if(channel != None):
            await self.embedStatus.post(channel);

        self.bot.log.info("Setting up save folder");
        try:
            if(os.path.exists(basePath)):
                shutil.rmtree(basePath);

            os.makedirs(basePath+"emojis");
        except OSError as exc:
            pass;

        await self.embedStatus.setStatus(CONST_STATUS_OK);

        self.bot.log.info("Saving Guild informations");
        file = open(basePath+"guild.json", "w");

        guildDict = guildModel.__dict__;
        guildDict["__version__"] = GUILD_FILE_VERSION;

        file.write(json.dumps(guildDict, indent=4));

        await self.embedStatus.setStatus(CONST_STATUS_OK);

        self.bot.log.info("Saving Guild's Icon");
        if guildModel.icon != None:
            self.savePicture(guildModel.icon_url, basePath+"icon");

        await self.embedStatus.setStatus(CONST_STATUS_OK);

        self.bot.log.info("Saving Guild's emojis");
        for emoji in guildModel.emojis:
            self.savePicture(emoji["url"], basePath+"emojis/"+str(emoji["id"]));

        await self.embedStatus.setStatus(CONST_STATUS_OK);


    def savePicture(self, url, path):
        url = url[:url.rfind(".")]+".png";
        r = requests.get(url, allow_redirects=True);
        open(path+".png", 'wb').write(r.content);
