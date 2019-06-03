from commands.Command import *

from file.ConfigFile import *
from file.GuildFile import *

import discord

class PasteDiscordCommand(Command):
    def __init__(self, bot):
        Command.__init__(self, bot.config.getDiscordPasteCommand(), bot);


    async def run(self, msg):
        guild = msg.guild;
        args = msg.content.split(" ");
        if len(args) <= 1:
            await msg.channel.send("Please, tell me the guild to paste...");
            return;

        guildIdToRestore = args[1];

        guildFile = GuildFile();
        guildModel = guildFile.loadGuild(guildIdToRestore);

        guildIcon = None;
        with open("guilds/"+guildIdToRestore+"/icon.png", "rb") as imageFile:
            guildIcon = imageFile.read()

        #Missing in Discord.py :
        #mfaLevel
        #default_message_notifications
        #explicit_content_filter
        #widget
        #system_channel_id

        #TODO
        #roles order
        #channel permissions overwrite
        #bans
        #members

        await guild.edit(name=guildModel["name"],
            icon=guildIcon,
            region=guildModel["region"],
            verification_level=discord.VerificationLevel(guildModel["verificationLevel"]),
            default_notifications=guildModel["default_message_notifications"],
            explicit_content_filter=discord.ContentFilter(guildModel["explicit_content_filter"])
        );

        for role in guildModel["roles"]:
            color = discord.Colour(role["color"]);
            permission = discord.Permissions(role["permissions"]["value"]);
            if(role["is_everyone"]):
                await guild.default_role.edit(
                    name=role["name"],
                    permissions=permission,
                    colour=color,
                    hoist=role["hoist"],
                    mentionable=role["mentionable"]
                );
            else:
                await guild.create_role(
                    name=role["name"],
                    permissions=permission,
                    colour=color,
                    hoist=role["hoist"],
                    mentionable=role["mentionable"]
                );

        for emoji in guildModel["emojis"]:
            emojiByte = None;
            with open("guilds/"+guildIdToRestore+"/emojis/"+str(emoji["id"])+".png", "rb") as imageFile:
                emojiByte = imageFile.read()

            await guild.create_custom_emoji(
                name=emoji["name"],
                image=emojiByte
            );

        newChannels = dict();
        for channel in guildModel["categories"]:

            channelCreated = await guild.create_category(
                name=channel["name"]
            );

            newChannels[channel["id"]] = channelCreated;

        for channel in guildModel["text_channels"]:
            if channel["parentId"] == None:
                category = None;
            else:
                category = newChannels[channel["parentId"]];

            channelCreated = await guild.create_text_channel(
                name=channel["name"],
				nsfw=channel["nsfw"],
                topic=channel["topic"],
                slowmode_delay=channel["slowmode_delay"],
                category=category
            );

            newChannels[channel["id"]] = channelCreated;

        for channel in guildModel["voice_channels"]:
            if channel["parentId"] == None:
                category = None;
            else:
                category = newChannels[channel["parentId"]];

            channelCreated = await guild.create_voice_channel(
                name=channel["name"],
                bitrate=channel["bitrate"],
                user_limit=channel["user_limit"],
                category=category
            );

            newChannels[channel["id"]] = channelCreated;

        for channel in guildModel["text_channels"]:
            await newChannels[channel["id"]].edit(position=channel["position"]);

        for channel in guildModel["voice_channels"]:
            await newChannels[channel["id"]].edit(position=channel["position"]);

        for ban in guildModel["bans"]:
            banUser = await self.bot.fetch_user(ban["user"]);
            await guild.ban(banUser, reason=ban["reason"], delete_message_days=0);

        system_channel = None;
        if guildModel["system_channel"] != None:
            system_channel = newChannels[guildModel["system_channel"]]

        await guild.edit(
            afk_channel=newChannels[guildModel["afkChannel"]],
            afk_timeout=guildModel["afkTimeout"],
            system_channel=system_channel
        );

        self.bot.log.info("Discord restored!");
        await msg.channel.send("Discord pasted!");
