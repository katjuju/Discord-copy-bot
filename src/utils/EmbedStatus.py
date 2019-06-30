import discord

from utils.const import *

class EmbedStatus:

    def __init__(self, title="Status"):
        self.colors = {CONST_STATUS_OK : 0x00ff00, CONST_STATUS_IN_PROGRESS : 0xff7f00, CONST_STATUS_FAIL : 0xff0000};
        self.icons = {CONST_STATUS_OK : ":white_check_mark:", CONST_STATUS_IN_PROGRESS : ":hourglass_flowing_sand:", CONST_STATUS_FAIL : ":x:", CONST_STATUS_WAITING : ":white_large_square:"};

        self.embed = discord.Embed(title=title, url="https://github.com/anondax/Discord-copy-bot", color=self.colors[CONST_STATUS_IN_PROGRESS]);

        self.posted = False;
        self.index = 0;


    def setTitle(self, title):
        self.embed.title = title;


    def addField(self, name):
        status = CONST_STATUS_WAITING if len(self.embed.fields) > 0 else CONST_STATUS_IN_PROGRESS;

        self.embed.add_field(name=name, value=self.icons[status], inline=False);


    async def setStatus(self, status, message=""):
        if(self.index >= len(self.embed.fields)):
            return;

        self.embed.set_field_at(self.index, name=self.embed.fields[self.index].name, value=self.icons[status] + " " + message, inline=False)
        self.index += 1;

        if(self.index == len(self.embed.fields)):
            await self.taskCompleted();
        else:
            self.embed.set_field_at(self.index, name=self.embed.fields[self.index].name, value=self.icons[CONST_STATUS_IN_PROGRESS], inline=False)


        if(status == CONST_STATUS_FAIL):
            self.embed.color = self.colors[CONST_STATUS_FAIL];

        await self.update();


    async def taskCompleted(self):
        if(self.embed.color.value == self.colors[CONST_STATUS_IN_PROGRESS]):
            self.embed.color = self.colors[CONST_STATUS_OK];
            self.embed.set_footer(text="Done!");
        else:
            self.embed.set_footer(text="Done with errors!");

        await self.update();


    async def post(self, channel):
        self.posted = True;
        self.message = await channel.send(embed=self.embed);


    async def update(self):
        if(self.posted):
            await self.message.edit(embed=self.embed);
