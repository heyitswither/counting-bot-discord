import discord

bot = discord.Client()
with open('bot.token', 'r') as fileIn:
  botToken = fileIn.read().replace('\n', '')
previousMsg = 0
countingChannel == ""

async def isInt(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

@bot.event
async def on_ready():
  print("Going through on ready!")
  print(bot.user.name + "#" + bot.user.discriminator)
  print("------------------------\n")
  await bot.change_presence(game=discord.Game(name='counting', url='https://twitch.tv/twitch', type=1))

@bot.event
async def on_message(message):
  global previousMsg
  if message.channel.id == countingChannel:
    if await isInt(message.content):
      if int(message.content) - 1 == previousMsg:
        previousMsg = int(message.content)
      else:
        await bot.delete_message(message)
    else:
      await bot.delete_message(message)

@bot.event
async def on_message_delete(message):
  global previousMsg
  if message.channel.id == countingChannel and await isInt(message.content):
    if int(message.content) == previousMsg:
      previousMsg = previousMsg - 1
      await bot.send_message(message.channel, previousMsg + 1)

bot.run(botToken)
