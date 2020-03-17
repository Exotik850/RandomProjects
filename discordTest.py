import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('Njg5MzQ4Nzg0MTM5OTI3NTcz.XnBkMw.k8Te5W72beU7ZLuGN8ckqX0q9jM')