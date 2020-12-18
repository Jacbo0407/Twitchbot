from twitchio.ext import commands
import random
import time
while 1 == 1:
    rating = random.randint(0, 10)

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='oauth:ptj2iedsh4vsgqby2n4qwxrue7rty4', client_id='zjb11n7hitlo1bmnmw91uns9ckd0ef', nick='Gaybuttstuff', prefix='!', initial_channels=['ppopu'])

    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    @commands.command(name='rate')
    async def my_command(self, ctx):
        await ctx.send(f'{ctx.author.name} your a solid {rating}')


bot = Bot()
bot.run()
