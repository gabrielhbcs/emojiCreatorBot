import tweepy
import random
import emojis
import io

todosEmotes = []
frasesTXT = open("frases.txt", "r")
frases = []
for linha in frasesTXT:
    frases.append(linha.strip())
print(frases)
frasesTXT.close()
desenhosTXT = io.open("desenhos.txt", "r")
desenhos = []
for linha in desenhosTXT:
    desenhos.append(linha.strip())
print(desenhos)
chavesTXT = open("chaves.txt", "r")
chaves = []
for linha in chavesTXT:
    chaves.append(linha.strip())
print(f'''
Consumer key: {chaves[0]}
Consumer secret: {chaves[1]}
Access key: {chaves[2]}
Access secret: {chaves[3]}

Chaves retiradas de 'chaves.txt'
Para acessar as chaves vá em https://developer.twitter.com/en/apps
''')


def tweetToTwitter():
    consumer_key = chaves[0]
    consumer_secret = chaves[1]
    access_key = chaves[2]
    access_secret = chaves[3]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    while True:
        emotesUsar = list(random.sample(todosEmotes, random.randint(1,4)))
        statusText = f'''{frases[random.randint(0, len(frases)-1)]}
{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}
⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜
⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜
⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜
{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}
{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}
⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜
⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜
⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜
{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}
{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}
⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜
⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜
⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜
{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}
{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}
⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜
⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜
⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜
{emotesUsar[random.randint(0,len(emotesUsar)-1)]}⬜⬜⬜{emotesUsar[random.randint(0,len(emotesUsar)-1)]}
'''
        print('\nTweetando:')
        print(statusText)
        resp = input("Publicar?(S/N)\n")
        if(resp == "S" or resp == "s"):
            api.update_status(status=statusText)
            break
        resp = input("Gerar outro?(S/N)\n")
        if (resp == "N" or resp == "n"):
            break


def main():
    print('Bom dia')
    for categoria in emojis.db.get_categories():
        #print(categoria)
        for emote in emojis.db.get_emojis_by_category(categoria):
            #print(emote[1])
            if(len(emote[1]) == 1):
                todosEmotes.append(emote[1])
    #print(todosEmotes)
    resp = input("Deseja tweetar? (S/N)\n")
    if(resp == "S" or resp == "s"):
        tweetToTwitter()
    else:
        print('flw enton')
if __name__ == "__main__":
    main()
