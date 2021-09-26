import discord

file = open("login.txt", "r")
TOKEN = file.readline()
class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        self.previous_author = ""

    async def on_message(self, message):
        print(message.content)

        # don't respond to ourselves
        if message.author == self.user:
            return

        minutes = 0
        seconds = 0

        # Sentence pre-process
        remove_these = ".,'-+()%_=:;!#¤/"
        for character in remove_these:
            message.content = message.content.replace(character, "")

        message.content = " ".join(message.content.split())
        message.content = message.content.split(' ')

        # Find minutes and seconds
        for i in range(len(message.content)):
            if message.content[i] == "minutes":
                minutes = message.content[i-1]
            if message.content[i] == "seconds":
                seconds = message.content[i-1]
        
        # If they were found
        string_result = ""
        if minutes != 0 or seconds != 0:
            string_result = str(self.previous_author) + "'s trip: " + str(minutes) + " minutes, " + str(seconds) + " seconds"
        self.previous_author = message.author

        if string_result=="":
            print("No minutes in message")
            return

        channel = client.get_channel(message.channel.id)
        if not channel or string_result=="":
            print("No channel found")
            return
        print(string_result)
        #await channel.send(string_result)




client = MyClient()
client.run(TOKEN)