from commands.Command import *

from file.ConfigFile import *
from file.GuildFile import *

import discord

class PasteDiscordCommand(Command):
    def __init__(self, bot):
        Command.__init__(self, bot.config.getDiscordPasteCommand(), bot);


    async def run(self, msg):
        guild = msg.server;
        args = msg.content.split(" ");
        if len(args) <= 1:
            await self.bot.send_message(msg.channel, "Please, tell me the server to paste...");
            return;

        guildIdToRestore = args[1];

        guildFile = GuildFile();
        guildModel = guildFile.loadGuild(guildIdToRestore);

        guildIcon = None;
        with open("guilds/"+guildIdToRestore+"/icon.png", "rb") as imageFile:
            guildIcon = imageFile.read()

        #Missing in Discord.py :
        #mfaLevel

        #TODO
        #afk channel
        #roles order
        #channels
        #bans
        #members
        await self.bot.edit_server(guild,
            name=guildModel["name"],
            icon=guildIcon,
            region=guildModel["region"],
            afk_timeout=guildModel["afkTimeout"],
            verification_level=discord.VerificationLevel(guildModel["verificationLevel"])
        );

        for role in guildModel["roles"]:
            color = discord.Colour(role["color"]);
            permission = discord.Permissions(role["permissions"]["value"]);

            await self.bot.create_role(guild,
                name=role["name"],
                permissions=permission,
                colour=color,
                hoist=role["hoist"],
                mentionable=role["mentionable"]
            );

        for emoji in guildModel["emojis"]:
            emojiByte = None;
            with open("guilds/"+guildIdToRestore+"/emojis/"+emoji["id"]+".png", "rb") as imageFile:
                emojiByte = imageFile.read()

            await self.bot.create_custom_emoji(guild,
                name=emoji["name"],
                image=emojiByte
            );

        self.bot.log.info("Discord restored!");
        await self.bot.send_message(msg.channel, "Discord pasted!");
