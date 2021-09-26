import discord
from ahk import AHK

command = "+m kill lizardman shaman"

file_lines = open("login.txt", "r").read().splitlines()

TOKEN = file_lines[0]
DISCORD_USER_ID = file_lines[1]
DISCORD_OSRS_BOT_RESPONSE_ID = file_lines[2]
DISCORD_OSRS_BOT_NOTIFY_IDS = {file_lines[3], file_lines[4]}

ahk = AHK()

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        self.previous_author = ""

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        # If its osrs bot
        if str(message.author.id) in DISCORD_OSRS_BOT_NOTIFY_IDS:

            # Sentence pre-process
            remove_these = ".,'-+()%_=:;!#¤/<>@"
            for character in remove_these:
                message.content = message.content.replace(character, "")
            message.content = " ".join(message.content.split())
            message.content = message.content.split(' ')

            # Check if user is target user
            if message.content[0] == DISCORD_USER_ID:
                channel = client.get_channel(message.channel.id)
                if not channel:
                    print("No channel found")
                    return
                
                # Send the command
                ahk.send_raw(command)
                ahk.key_press('Enter')

            #await channel.send(string_result)
            return
        print("Author mismatch!")




client = MyClient()
client.run(TOKEN)