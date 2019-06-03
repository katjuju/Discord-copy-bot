from commands.Command import *

from file.ConfigFile import *
from file.GuildFile import *

import discord

class PasteDiscordCommand(Command):
    def __init__(self, bot):
        Command.__init__(self, bot.config.getDiscordPasteCommand(), bot);


    async def run(self, msg):
        if not msg.author.guild_permissions.manage_guild:
            await msg.channel.send("Only user with the \"Manage Guild\" permission can execute this command.");
            return

        guild = msg.guild;
        args = msg.content.split(" ");
        if len(args) <= 1:
            await msg.channel.send("Please, tell me the guild to paste...");
            return;

        guildIdToRestore = args[1];

        guildFile = GuildFile(self.bot);
        guildModel = guildFile.loadGuild(guildIdToRestore);

        guildIcon = None;
        with open("guilds/"+guildIdToRestore+"/icon.png", "rb") as imageFile:
            guildIcon = imageFile.read()


        self.bot.log.info("Restoring Guild settings");
        await guild.edit(name=guildModel["name"],
            icon=guildIcon,
            region=guildModel["region"],
            verification_level=discord.VerificationLevel(guildModel["verificationLevel"]),
            default_notifications=guildModel["default_message_notifications"],
            explicit_content_filter=discord.ContentFilter(guildModel["explicit_content_filter"])
        );

        self.bot.log.info("Restoring Guild roles");
        newRoles = dict();
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

                roleCreated = guild.default_role;

            else:
                roleCreated = await guild.create_role(
                    name=role["name"],
                    permissions=permission,
                    colour=color,
                    hoist=role["hoist"],
                    mentionable=role["mentionable"]
                );

            newRoles[role["id"]] = roleCreated;

        self.bot.log.info("Restoring Guild emojis");
        for emoji in guildModel["emojis"]:
            emojiByte = None;
            with open("guilds/"+guildIdToRestore+"/emojis/"+str(emoji["id"])+".png", "rb") as imageFile:
                emojiByte = imageFile.read()

            await guild.create_custom_emoji(
                name=emoji["name"],
                image=emojiByte
            );

        self.bot.log.info("Restoring Guild channels");
        newChannels = dict();
        for channel in guildModel["categories"]:
            overwrites = {
                newRoles[int(k)]: self.getOverwrites(v) for k, v in channel["overwrites"].items() if int(k) in newRoles
            }

            channelCreated = await guild.create_category(
                name=channel["name"],
                overwrites=overwrites
            );

            newChannels[channel["id"]] = channelCreated;

        for channel in guildModel["text_channels"]:
            if channel["parentId"] == None:
                category = None;
            else:
                category = newChannels[channel["parentId"]];

            overwrites = {
                newRoles[int(k)]: self.getOverwrites(v) for k, v in channel["overwrites"].items() if int(k) in newRoles
            }

            channelCreated = await guild.create_text_channel(
                name=channel["name"],
				nsfw=channel["nsfw"],
                topic=channel["topic"],
                slowmode_delay=channel["slowmode_delay"],
                category=category,
                overwrites=overwrites
            );

            newChannels[channel["id"]] = channelCreated;

        for channel in guildModel["voice_channels"]:
            if channel["parentId"] == None:
                category = None;
            else:
                category = newChannels[channel["parentId"]];

            overwrites = {
                newRoles[int(k)]: self.getOverwrites(v) for k, v in channel["overwrites"].items() if int(k) in newRoles
            }

            channelCreated = await guild.create_voice_channel(
                name=channel["name"],
                bitrate=channel["bitrate"],
                user_limit=channel["user_limit"],
                category=category,
                overwrites=overwrites
            );

            newChannels[channel["id"]] = channelCreated;

        self.bot.log.info("Restoring Guild bans");
        for ban in guildModel["bans"]:
            banUser = await self.bot.fetch_user(ban["user"]);
            await guild.ban(banUser, reason=ban["reason"], delete_message_days=0);

        self.bot.log.info("Restoring Guild Post channel settings (AFK, System channel)");
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

    def getOverwrites(self, permissions):
        return discord.PermissionOverwrite(
            create_instant_invite=permissions["create_instant_invite"],
            kick_members=permissions["kick_members"],
            ban_members=permissions["ban_members"],
            administrator=permissions["administrator"],
            manage_channels=permissions["manage_channels"],
            manage_guild=permissions["manage_guild"],
            add_reactions=permissions["add_reactions"],
            view_audit_log=permissions["view_audit_logs"],
            priority_speaker=permissions["priority_speaker"],
            stream=permissions["stream"],
            read_messages=permissions["read_messages"],
            send_messages=permissions["send_messages"],
            send_tts_messages=permissions["send_tts_messages"],
            manage_messages=permissions["manage_messages"],
            embed_links=permissions["embed_links"],
            attach_files=permissions["attach_files"],
            read_message_history=permissions["read_message_history"],
            mention_everyone=permissions["mention_everyone"],
            external_emojis=permissions["external_emojis"],
            connect=permissions["connect"],
            speak=permissions["speak"],
            mute_members=permissions["mute_members"],
            deafen_members=permissions["deafen_members"],
            move_members=permissions["move_members"],
            use_voice_activation=permissions["use_voice_activation"],
            change_nickname=permissions["change_nickname"],
            manage_nicknames=permissions["manage_nicknames"],
            manage_roles=permissions["manage_roles"],
            manage_webhooks=permissions["manage_webhooks"],
            manage_emojis=permissions["manage_emojis"]
        );
