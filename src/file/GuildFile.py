import json
import requests

import os

class GuildFile:
    def __init__(self):
    	pass;


    def loadGuild(self, guildId):
        file = open("guilds/"+guildId+"/server.json", "r");
        return json.load(file);


    def saveGuild(self, guildModel):
        basePath = "guilds/"+guildModel.id+"_"+guildModel.name.replace(" ", "_")+"/";

        try:
            os.makedirs(basePath+"emojis");
        except OSError as exc:
            pass;

        file = open(basePath+"server.json", "w");
        file.write(json.dumps(guildModel.__dict__, indent=4));

        if guildModel.icon != None:
            self.savePicture(guildModel.icon_url, basePath+"icon");

        for emoji in guildModel.emojis:
            self.savePicture(emoji["url"], basePath+"emojis/"+emoji["id"]);


    def savePicture(self, url, path):
        url = url[:url.rfind(".")]+".png";
        r = requests.get(url, allow_redirects=True);
        open(path+".png", 'wb').write(r.content);
