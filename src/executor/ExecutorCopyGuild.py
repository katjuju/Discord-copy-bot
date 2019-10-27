from executor.Executor import *

from file.GuildFile import *

from utils.const import *
from utils.Logger import *

import discord

import os
import requests
import shutil

class ExecutorCopyGuild(Executor):

    def __init__(self, guild, listener):
        Executor.__init__(self, None);

        self.guild = guild;
        self.listener = listener;


    async def copyGuild(self):
        guildModel = await GuildFile.createFromGuild(self.guild);

        basePath = "guilds/"+str(self.guild.id)+"_"+self.guild.name.replace(" ", "_")+"/";

        await self.removeOldSave(basePath);
        await self.saveGuildModelInJson(basePath, guildModel);
        await self.saveGuildIcon(basePath, guildModel);
        await self.saveEmojis(basePath, guildModel);


    async def removeOldSave(self, basePath):
        await self.listener.taskChanged("Set up save folder");
        Logger.info("Setting up save folder");
        try:
            if(os.path.exists(basePath)):
                shutil.rmtree(basePath);

            os.makedirs(basePath+"emojis");
        except OSError as exc:
            pass;

        await self.listener.taskFinished();


    async def saveGuildModelInJson(self, basePath, guildModel):
        await self.listener.taskChanged("Saving Guild informations");

        file = open(basePath+"guild.json", "w");

        guildDict = guildModel.__dict__;
        guildDict["__version__"] = GUILD_FILE_VERSION;

        file.write(json.dumps(guildDict, indent=4));

        await self.listener.taskFinished();


    async def saveGuildIcon(self, basePath, guildModel):
        await self.listener.taskChanged("Saving Guild's Icon");
        if guildModel.icon != None:
            self.savePicture(guildModel.icon_url, basePath+"icon");

        await self.listener.taskFinished();


    async def saveEmojis(self, basePath, guildModel):
        await self.listener.taskChanged("Saving Guild's emojis");
        for emoji in guildModel.emojis:
            self.savePicture(emoji["url"], basePath+"emojis/"+str(emoji["id"]));

        await self.listener.taskFinished();

        await self.listener.completed();


    def savePicture(self, url, path):
        url = url[:url.rfind(".")]+".png";
        r = requests.get(url, allow_redirects=True);
        open(path+".png", 'wb').write(r.content);
