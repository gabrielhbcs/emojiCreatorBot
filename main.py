import tweepy
import emojis
import random, io, time

QTDEVENTOS = 3

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

consumer_key = chaves[0]
consumer_secret = chaves[1]
access_key = chaves[2]
access_secret = chaves[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def hungerGamesEvent():
    statusText = '''
QUE COMECEM OS JOGOS VORAZES
Para participar comente algo nesse status, deixe seu grito de guerra, seu texto motivacional, qlqr coisa.
Você será notificado da sua participação
Se ganhar vc será reconhecido ;)
\n
RT/Fav pra fortalecer o bot <3
As inscrições terminam em 10 minutos
'''
    print(f"Tweetando:\n{statusText}")
    api.update_status(status = statusText)
    time.sleep(600)
    print("Pegando nomes do último status")
    tweet = api.user_timeline(screen_name=api.me().screen_name, count=1, tweet_mode='extended')[0]
    replies = tweepy.Cursor(api.search, q=f'to:@{api.me().screen_name}', since_id=tweet.id, tweet_mode='extended').items()
    participantesVivos = [[]]
    cont = 0
    i = 0
    while True and cont < 12:
        try:
            reply = replies.next()
            # print(reply.user.screen_name)
            for linha in participantesVivos:
                for participante in linha:
                    if(participante == reply.user.screen_name):
                        continue
            if(cont % 2 == 0):
                participantesVivos[i].append(reply.user.screen_name)
            else:
                participantesVivos[i].append(reply.user.screen_name)
                participantesVivos.append([])
                i += 1
            cont += 1
        except:
            break
    if (cont < 6):
        print("Não há pessoas suficientes")
        api.update_status(status = "Preciso de pelo menos 6 pessoas pra rodar o evento :( \n #NaoVaiTerHG")
        return None
    statusText = '''
Conheça os participantes do próximo HungerGames:\n
'''
    i = 0
    for linha in participantesVivos:
        statusText += f"\nD{i + 1}:"
        for pessoa in linha:
            statusText += " @"+pessoa
        statusText += "\n"
    statusText += "\nO evento começará em 5 minutos!"
    print(f"Tweetando:\n{statusText}")
    api.update_status(status = statusText)
    time.sleep(300)
    while True:
        pass


def tweetToTwitter():
    while True:
        #emotesUsar = list(random.sample(todosEmotes, random.randint(1, 4)))

        #qlPostar = 2
        qlPostar = random.randint(0, QTDEVENTOS - 1)
        # DNA Random
        if(qlPostar == 0):
            emotesUsar = list(random.sample(todosEmotes, random.randint(1, 4)))
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
        # DNA 2 emojis
        elif (qlPostar == 1):
            emotesUsar = list(random.sample(todosEmotes, 2))
            statusText = f'''{frases[random.randint(0, len(frases) - 1)]}
{emotesUsar[0]}⬜⬜⬜{emotesUsar[1]}
⬜{emotesUsar[0]}⬜{emotesUsar[1]}⬜
⬜⬜{emotesUsar[0]}⬜⬜
⬜{emotesUsar[1]}⬜{emotesUsar[0]}⬜
{emotesUsar[1]}⬜⬜⬜{emotesUsar[0]}
{emotesUsar[1]}⬜⬜⬜{emotesUsar[0]}
⬜{emotesUsar[1]}⬜{emotesUsar[0]}⬜
⬜⬜{emotesUsar[1]}⬜⬜
⬜{emotesUsar[0]}⬜{emotesUsar[1]}⬜
{emotesUsar[0]}⬜⬜⬜{emotesUsar[1]}
{emotesUsar[0]}⬜⬜⬜{emotesUsar[1]}
⬜{emotesUsar[0]}⬜{emotesUsar[1]}⬜
⬜⬜{emotesUsar[0]}⬜⬜
⬜{emotesUsar[1]}⬜{emotesUsar[0]}⬜
{emotesUsar[1]}⬜⬜⬜{emotesUsar[0]}
{emotesUsar[1]}⬜⬜⬜{emotesUsar[0]}
⬜{emotesUsar[1]}⬜{emotesUsar[0]}⬜
⬜⬜{emotesUsar[1]}⬜⬜
⬜{emotesUsar[0]}⬜{emotesUsar[1]}⬜
{emotesUsar[0]}⬜⬜⬜{emotesUsar[1]}
            '''
        # Guerra de emoji
        elif (qlPostar == 2):
            emotesUsar = list(random.sample(todosEmotes, 3))
            statusText = f'''
               QUEM GANHA??
        RT          |          FAV
{emotesUsar[0]}⬜⬜⬜🆚⬜⬜⬜{emotesUsar[2]}
⬜{emotesUsar[0]}⬜⬜🆚{emotesUsar[2]}⬜⬜⬜
⬜⬜{emotesUsar[0]}⬜🆚⬜⬜{emotesUsar[2]}⬜
{emotesUsar[0]}⬜⬜⬜🆚{emotesUsar[2]}⬜⬜⬜
⬜⬜⬜⬜🆚⬜{emotesUsar[2]}⬜⬜
⬜⬜{emotesUsar[0]}⬜🆚⬜{emotesUsar[2]}⬜⬜
⬜{emotesUsar[0]}⬜⬜🆚⬜⬜⬜⬜
⬜⬜⬜{emotesUsar[0]}🆚⬜⬜{emotesUsar[2]}⬜
⬜{emotesUsar[0]}⬜⬜🆚⬜{emotesUsar[2]}⬜⬜
⬜⬜⬜{emotesUsar[0]}🆚⬜⬜{emotesUsar[2]}⬜
⬜{emotesUsar[0]}⬜⬜🆚{emotesUsar[2]}⬜⬜⬜
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
    resp = input('''
    Escolha uma opção:
    1 - Tweetar
    2 - Testar tweet específico
    S - sair
    ''')
    if(resp == "1"):
        tweetToTwitter()
    elif (resp == "2"):
        hungerGamesEvent()
    else:
        print('flw enton')
if __name__ == "__main__":
    main()