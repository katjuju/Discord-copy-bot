from executor.Executor import *

from utils.const import *

import discord

class ExecutorPasteGuild(Executor):

    def __init__(self, bot, guild, guildModel, guildIdToRestore, listener):
        Executor.__init__(self, None);

        self.bot = bot;
        self.guild = guild;
        self.guildModel = guildModel;
        self.guildIdToRestore = guildIdToRestore;
        self.listener = listener;


    async def run(self):
        await self.pasteGuildSettings();
        await self.pasteGuildRoles();
        await self.pasteGuildEmojis();
        await self.pasteGuildChannels();
        await self.pasteGuildBans();
        await self.pasteGuildPostChannelSettings();

        await self.listener.completed();


    async def pasteGuildSettings(self):
        await self.listener.taskChanged("Restoring Guild settings");

        guildIcon = None;
        try:
            with open("guilds/"+self.guildIdToRestore+"/icon.png", "rb") as imageFile:
                guildIcon = imageFile.read()
        except:
            pass;

        await self.guild.edit(
            name=self.guildModel["name"],
            icon=guildIcon,
            region=self.guildModel["region"],
            verification_level=discord.VerificationLevel(self.guildModel["verificationLevel"]),
            default_notifications=self.guildModel["default_message_notifications"],
            explicit_content_filter=discord.ContentFilter(self.guildModel["explicit_content_filter"])
        );

        await self.listener.taskFinished("The Discord server you pasted had \"Two-Factor Authentication\" enabled. Please, ask the owner to re-enable it on this Discord server." if self.guildModel["mfaLevel"] else "";);


    async def pasteGuildRoles(self):
        await self.listener.taskChanged("Restoring Guild roles");

        self.newRoles = dict();
        for role in self.sortList(self.guildModel["roles"], True):
            color = discord.Colour(role["color"]);
            permission = discord.Permissions(role["permissions"]["value"]);

            if(role["is_everyone"]):
                await self.guild.default_role.edit(
                    name=role["name"],
                    permissions=permission,
                    colour=color,
                    hoist=role["hoist"],
                    mentionable=role["mentionable"]
                );

                roleCreated = self.guild.default_role;

            else:
                try:
                    roleCreated = await self.guild.create_role(
                        name=role["name"],
                        permissions=permission,
                        colour=color,
                        hoist=role["hoist"],
                        mentionable=role["mentionable"]
                    );
                except discord.errors.HTTPException:
                    await self.listener.taskError("You reached the role limit.");
                    return;

            self.newRoles[role["id"]] = roleCreated;

        await self.listener.taskFinished();


    async def pasteGuildEmojis(self):
        await self.listener.taskChanged("Restoring Guild emojis");

        for emoji in self.guildModel["emojis"]:
            emojiByte = None;
            with open("guilds/"+self.guildIdToRestore+"/emojis/"+str(emoji["id"])+".png", "rb") as imageFile:
                emojiByte = imageFile.read()

            try:
                await self.guild.create_custom_emoji(
                    name=emoji["name"],
                    image=emojiByte
                );
            except discord.errors.HTTPException:
                await self.listener.taskError("You reached the emoji limit.");
                return;

        await self.listener.taskFinished();


    async def pasteGuildChannels(self):
        await self.listener.taskChanged("Restoring Guild channels");

        self.newChannels = dict();
        for channel in self.sortList(self.guildModel["categories"]):
            overwrites = {
                self.newRoles[int(k)]: self.getOverwrites(v) for k, v in channel["overwrites"].items() if int(k) in self.newRoles
            }

            channelCreated = await self.guild.create_category(
                name=channel["name"],
                overwrites=overwrites
            );

            self.newChannels[channel["id"]] = channelCreated;

        for channel in self.sortList(self.guildModel["text_channels"]):
            if channel["parentId"] == None:
                category = None;
            else:
                category = self.newChannels[channel["parentId"]];

            overwrites = {
                self.newRoles[int(k)]: self.getOverwrites(v) for k, v in channel["overwrites"].items() if int(k) in self.newRoles
            }

            channelCreated = await self.guild.create_text_channel(
                name=channel["name"],
				nsfw=channel["nsfw"],
                topic=channel["topic"],
                slowmode_delay=channel["slowmode_delay"],
                category=category,
                overwrites=overwrites
            );

            self.newChannels[channel["id"]] = channelCreated;

        for channel in self.sortList(self.guildModel["voice_channels"]):
            if channel["parentId"] == None:
                category = None;
            else:
                category = self.newChannels[channel["parentId"]];

            overwrites = {
                self.newRoles[int(k)]: self.getOverwrites(v) for k, v in channel["overwrites"].items() if int(k) in self.newRoles
            }

            channelCreated = await self.guild.create_voice_channel(
                name=channel["name"],
                bitrate=channel["bitrate"],
                user_limit=channel["user_limit"],
                category=category,
                overwrites=overwrites
            );

            self.newChannels[channel["id"]] = channelCreated;

        await self.listener.taskFinished();


    async def pasteGuildBans(self):
        await self.listener.taskChanged("Restoring Guild bans");

        for ban in self.guildModel["bans"]:
            banUser = await self.bot.fetch_user(ban["user"]);
            await self.guild.ban(banUser, reason=ban["reason"], delete_message_days=0);

        await self.listener.taskFinished();


    async def pasteGuildPostChannelSettings(self):
        await self.listener.taskChanged("Restoring Guild Post channel settings (AFK, System channel)");

        system_channel = None;
        if self.guildModel["system_channel"] != None:
            system_channel = self.newChannels[self.guildModel["system_channel"]]

        afkChannel = None if self.guildModel["afkChannel"] == None else self.newChannels[self.guildModel["afkChannel"]];

        await self.guild.edit(
            afk_channel=afkChannel,
            afk_timeout=self.guildModel["afkTimeout"],
            system_channel=system_channel,
            system_channel_flags=discord.SystemChannelFlags(**self.guildModel["system_channel_flags"])
        );

        await self.listener.taskFinished();


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


    def sortList(self, list, reversed = False):
        n = len(list);
        for i in range(n):
            k = i;
            for j in range(i+1, n):
                if list[k]["position"] > list[j]["position"] and not reversed:
                    k = j;
                elif list[k]["position"] < list[j]["position"] and reversed:
                    k = j;
            list[k], list[i] = list[i], list[k];

        return list;
