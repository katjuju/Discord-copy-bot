import json
import requests

import os

class GuildFile:
    def __init__(self, bot):
    	self.bot = bot;


    def loadGuild(self, guildId):
        file = open("guilds/"+guildId+"/guild.json", "r");
        return json.load(file);


    def saveGuild(self, guildModel):
        basePath = "guilds/"+str(guildModel.id)+"_"+guildModel.name.replace(" ", "_")+"/";

        self.bot.log.info("Setting up save folder");
        try:
            os.makedirs(basePath+"emojis");
        except OSError as exc:
            pass;

        self.bot.log.info("Saving Guild informations");
        file = open(basePath+"guild.json", "w");
        file.write(json.dumps(guildModel.__dict__, indent=4));

        self.bot.log.info("Saving Guild's Icon");
        if guildModel.icon != None:
            self.savePicture(guildModel.icon_url, basePath+"icon");

        self.bot.log.info("Saving Guild's emojis");
        for emoji in guildModel.emojis:
            self.savePicture(emoji["url"], basePath+"emojis/"+str(emoji["id"]));


    def savePicture(self, url, path):
        url = url[:url.rfind(".")]+".png";
        r = requests.get(url, allow_redirects=True);
        open(path+".png", 'wb').write(r.content);
