import json
import requests

import os

class GuildFile:
    def __init__(self):
    	pass;


    def saveGuild(self, guildModel):
        basePath = "guilds/"+guildModel.id+"_"+guildModel.name+"/";

        try:
            os.makedirs(basePath+"emojis");
        except OSError as exc:
            pass;

        file = open(basePath+guildModel.name+".json", "w");
        file.write(json.dumps(guildModel.__dict__, indent=4));

        self.savePicture(guildModel.icon_url, basePath+guildModel.icon);

        for emoji in guildModel.emojis:
            self.savePicture(emoji["url"], basePath+"emojis/"+emoji["id"]);



    def savePicture(self, url, path):
        r = requests.get(url, allow_redirects=True);
        open(path+"."+url[url.rfind(".")+1:], 'wb').write(r.content);
