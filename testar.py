import random

file = open("bots.txt", "r")
bots = file.readlines()
file.close()
qtdBots = 24
listaBots = random.sample(bots, 5)
bot = listaBots.pop()
num = str(random.randint(100,999))
print("Bot"+bot.strip()+str(num))
