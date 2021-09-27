import discord
from ahk import AHK
import random

command = "+m kill lizardman shaman"
peepos = ["FeelsBanMan", "9525_pepe_facemask", "8763_pepe_smug", 
"8996_pepe_facepalm", "9462_pepe_sad", "9432pepecowboy", 
"8729_pepe_peek", "9237pepesmile", "8608_pepe_grin", 
"7948pepelipbite", "9103_pepe_hearteyes", "8303_pepe_trollface", 
"7515_pepe_owo", "6897pepeclap", "7190_linkpepehype", 
"5837_pepe_sleep", "5566_pepe_sunglasses", "5635pepesalute", 
"4971_pepe_thinking", "4587pepeguns", "5403_pepe_closedsmile", 
"4551pepeparty", "4275_pepe_5head", "4140pepecigarettesmoke", 
"3740pepeupsidedownsmile", "3912_pepe_ugh", "3962pepetradeoffer", 
"1765_pepe_vomit", "3804_pepe_whatif", "3817_pepe_glare",  
"3708pepederp", "3528_pepe_youcantifyoudont", "3394_pepe_shy",  
"2792pepepray", "1529_pepe_ok", "2295_pepe_oof",  
"2417pepelurk", "PepeYikes", "3205_pepe_uwu",  
"monkaS", "monkaStab", "2125_pepe_omegalol",   
"2008_pepe_thumbsdown", "1997_pepe_thief", "1970_pepe_sweat",   
"1389pepenoted", "1749_pepe_buy", "1304_pepe_thumbsup"]

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
                
                # Post 3 peepos in chat
                peepo_string = ":" + random.choice(peepos) + ": " + ":" + random.choice(peepos) + ": " + ":" + random.choice(peepos) + ":"
                ahk.send_raw(peepo_string)
                ahk.key_press('Enter')

                # Command
                ahk.send_raw(command)
                ahk.key_press('Enter')

            #await channel.send(string_result)
            return




client = MyClient()
client.run(TOKEN)