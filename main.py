import tweepy
import emojis
import random, io, time

QTDEVENTOS = 3
MAX_LINHAS = 5

arq = open("edicao.txt", "r")
for linha in arq:
    edicao = linha
arq.close()
todosEmotes = []
frasesTXT = open("frases.txt", "r")
frases = []
for linha in frasesTXT:
    frases.append(linha.strip())
frasesTXT.close()
desenhosTXT = io.open("desenhos.txt", "r")
desenhos = []
for linha in desenhosTXT:
    desenhos.append(linha.strip())
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

def esperar(tempo):
    print(f"\tAguardando {tempo} segundos")
    time.sleep(tempo)

def tweetarXmin(texto, tempo):
    print(f"\tTweetando: \n{texto}")
    api.update_status(status = texto)
    esperar(tempo)

def tweetarXminReply(texto, tempo, tweet):
    print(f"Respondendo o útlimo tweet:\n{texto}")
    api.update_status(status=texto, in_reply_to_status_id=tweet.id)
    esperar(tempo)

def removeDaListaVivos(lista1, lista2, morre):
    for linha in lista1:
        if (morre in linha):
            linha.remove(morre)
    lista2.remove(morre)
    return lista1, lista2

def anunciarMortos(mortesDoDia, participantesOriginais, participantesVivosLista, api):
    metade = False
    contador = 0
    statusText = ''
    if (len(mortesDoDia) > 0):
        if (len(mortesDoDia) == 1):
            i = 1
            for linha in participantesOriginais:
                if (mortesDoDia[0] in linha):
                    statusText = f"hoje fora ouvido apenas um tiro de canhão: \n@{mortesDoDia[0]} do distrito {i}\nserá isso bom ou ruim?"
                    break
                i += 1
        else:
            statusText = f'Hoje foram ouvidos {len(mortesDoDia)} tiros de canhão a distância:'
            for morto in mortesDoDia:
                statusText += f"\n@{morto} "
                i = 1
                for linha in participantesOriginais:
                    if (morto in linha):
                        statusText += f"do distrito {i}"
                        break
                    i += 1
                contador += 1
                if (contador % MAX_LINHAS == 0):
                    if (not metade):
                        metade = True
                        tweetarXmin(statusText, 10)
                    else:
                        tweet = api.user_timeline(screen_name=api.me().screen_name, count=1, tweet_mode='extended')[0]
                        tweetarXminReply(statusText, 30 * contador, tweet)
                    statusText = ""
            if (not contador % MAX_LINHAS == 0):
                if (metade):
                    tweet = api.user_timeline(screen_name=api.me().screen_name, count=1, tweet_mode='extended')[0]
                    if (len(participantesVivosLista) > 1):
                        tweetarXminReply(statusText, min(30 * contador, 300), tweet)
                    else:
                        tweetarXminReply(statusText, min(30), tweet)
                    statusText = ""
                else:
                    if (len(participantesVivosLista) > 1):
                        tweetarXmin(statusText, min(30 * contador, 300))
                    else:
                        tweetarXmin(statusText, 30)
                    statusText = ""

def hungerGamesEvent():

    #region Post de inscrição dos tributos (+600 segs)
    statusText = f'''
QUE COMECEM OS JOGOS VORAZES {edicao} 
Para participar comente algo nesse status, deixe seu grito de guerra, seu texto motivacional, qlqr coisa.
Você será notificado da sua participação

RT/Fav pra fortalecer o bot <3
As inscrições terminam em 30 minutos
#JogosVorazes
'''
    arq = open("edicao.txt", "w")
    arq.write(str(int(edicao) + 1))
    arq.close()
    tweetarXmin(statusText, 1800)
    # endregion

    print("Pegando nomes do último status")
    tweet = api.user_timeline(screen_name=api.me().screen_name, count=1, tweet_mode='extended')[0]
    replies = tweepy.Cursor(api.search, q=f'to:@{api.me().screen_name}',result_type="recent", since_id=tweet.id, tweet_mode='extended').items()
    #replies = tweepy.Cursor(api.search, q=f'to:@{api.me().screen_name}', since_id=tweet.id, tweet_mode='extended').items()
    participantesVivos = [[]]
    participantesOriginais = [[]]
    participantesVivosLista = []
    cont = 0
    i = 0
    '''
    while cont < 24:

        #region Juntando os participantes das respostas do ultimo tweet nos vetores de participantes
        try:
            for reply in replies:
                adicionado = False
                print(reply)
                for participante in participantesVivosLista:
                    if(participante == reply.user.screen_name):
                        adicionado = True
                        break
                if (not adicionado):
                    participantesVivosLista.append(reply.user.screen_name)
            reply = replies.next()
            # print(reply.user.screen_name)
            adicionado = False
            print(reply)
            for participante in participantesVivosLista:
                if(participante == reply.user.screen_name):
                    adicionado = True
                    break
            if(adicionado):
                continue
            participantesVivosLista.append(reply.user.screen_name)
            
            #cont += 1
        except:
            print("Não há mais replies")
            break
        #endregion
    '''
    for reply in replies:
        adicionado = False
        print(reply)
        for participante in participantesVivosLista:
            if (participante == reply.user.screen_name):
                print("Participante já adicionado")
                adicionado = True
                break
        if (not adicionado):
            participantesVivosLista.append(reply.user.screen_name)

    print(f"Participantes: {participantesVivosLista}")

    #region Juntando 24 pessoas aleatórias das que responderam o último tweet (pra não ser os primeiros)
    cont = 0
    i = 0
    if (len(participantesVivosLista) >= 24):
        participantesVivosLista = random.sample(participantesVivosLista, 24)
        for pessoa in participantesVivosLista:
            if (cont % 2 == 0):
                participantesVivos[i].append(pessoa)
                participantesOriginais[i].append(pessoa)
            else:
                participantesVivos[i].append(pessoa)
                participantesOriginais[i].append(pessoa)
                participantesVivos.append([])
                participantesOriginais.append([])
                i += 1
            cont += 1
            if (cont == 24):
                break
    else:
        for pessoa in participantesVivosLista:
            if (cont % 2 == 0):
                participantesVivos[i].append(pessoa)
                participantesOriginais[i].append(pessoa)
            else:
                participantesVivos[i].append(pessoa)
                participantesOriginais[i].append(pessoa)
                participantesVivos.append([])
                participantesOriginais.append([])
                i += 1
            cont += 1
    # endregion

    #region Adicionado listas predefinidas para testes
    #participantesVivos = [['Gabriel3wefsd','Werneckasfq'],['Yasminhtyhd','Mayaraffrewg'],['Lucianosdgvrth','Tutdasgwefgs'],['Gustavobtgym','Amandaikghd'],['Pedroryjfs','Maryyxjvfb'],['Douglasxhjxdh','Caiolmxzsdk'],['AGabriel3wefsd','AWerneckasfq'],['AYasminhtyhd','AMayaraffrewg'],['ALucianosdgvrth','ATutdasgwefgs'],['AGustavobtgym','AAmandaikghd'],['APedroryjfs','AMaryyxjvfb'],['ADouglasxhjxdh','ACaiolmxzsdk'],[]]
    #participantesOriginais = [['Gabriel3wefsd','Werneckasfq'],['Yasminhtyhd','Mayaraffrewg'],['Lucianosdgvrth','Tutdasgwefgs'],['Gustavobtgym','Amandaikghd'],['Pedroryjfs','Maryyxjvfb'],['Douglasxhjxdh','Caiolmxzsdk'],['AGabriel3wefsd','AWerneckasfq'],['AYasminhtyhd','AMayaraffrewg'],['ALucianosdgvrth','ATutdasgwefgs'],['AGustavobtgym','AAmandaikghd'],['APedroryjfs','AMaryyxjvfb'],['ADouglasxhjxdh','ACaiolmxzsdk'],[]]
    #participantesVivosLista = ['Gabriel3wefsd','Werneckasfq','Yasminhtyhd','Mayaraffrewg','Lucianosdgvrth','Tutdasgwefgs','Gustavobtgym','Amandaikghd','Pedroryjfs','Maryyxjvfb','Douglasxhjxdh','Caiolmxzsdk','AGabriel3wefsd','AWerneckasfq','AYasminhtyhd','AMayaraffrewg','ALucianosdgvrth','ATutdasgwefgs','AGustavobtgym','AAmandaikghd','APedroryjfs','AMaryyxjvfb','ADouglasxhjxdh','ACaiolmxzsdk']
    #cont = 24
    #endregion


    #region Não há pessoas suficientes pra prosseguir o evento, completando com bots!
    if (cont < 24):
        file = open("bots.txt", "r")
        bots = file.readlines()
        file.close()
        qtdBots = 24 - cont
        listaBots = random.sample(bots, qtdBots)
        while cont < 24:
            bot = listaBots.pop()
            num = str(random.randint(100,999))
            participantesVivos[i].append("Bot"+bot.strip()+str(num))
            participantesOriginais[i].append("Bot"+bot.strip()+str(num))
            participantesVivosLista.append("Bot"+bot.strip()+str(num))
            if (cont % 2 == 1):
                participantesVivos.append([])
                participantesOriginais.append([])
                i += 1
            cont += 1
        print(participantesOriginais)
    #endregion

    #region Carregando as frases de 'frases HG.txt' em seus respectivos vetores e misturando os vetores
    frasesHGTXT = open("frases HG.txt","r")
    momento = ""
    mataMata, causasNaturais, items, noite, noiteEmDupla = [], [], [], [], []
    for linha in frasesHGTXT:
        if(linha.strip().isupper()):
            momento = linha.strip()
            continue
        if(momento == "MATA MATA"):
            mataMata.append(linha.strip())
            continue
        elif(momento == "CAUSAS NATURAIS"):
            causasNaturais.append(linha.strip())
            continue
        elif(momento == "ITEMS"):
            items.append(linha.strip())
            continue
        elif(momento == "NOITE"):
            noite.append(linha.strip())
            continue
        elif(momento == "NOITE EM DUPLA"):
            noiteEmDupla.append(linha.strip())
            continue

    frasesHGTXT.close()
    cMM, cCN, cI, cN, cNED = 0, 0, 0, 0, 0
    mataMata = random.sample(mataMata,len(mataMata))
    causasNaturais = random.sample(causasNaturais, len(causasNaturais))
    items = random.sample(items, len(items))
    noite = random.sample(noite, len(noite))
    noiteEmDupla = random.sample(noiteEmDupla, len(noiteEmDupla))
    #endregion

    #region Carregando vetores com dizeres quando não acontece o evento
    eventoSemTiro = ['Sem tiros de canhão hoje\n\nsó isso mesmo','Não houveram mortes hoje','Ninguém morreu hoje\nimpressionante, mas o jogo tem que continuar :)','Não houveram tiros de canhão hoje\nserá que hoje os tributos dormem mais tranquilos?', 'Nenhum tiro de canhão foi dado hoje']
    eventoSemTiro = random.sample(eventoSemTiro, len(eventoSemTiro))
    cEST = 0

    eventoCombatesDiretos = ['Os tributos não se encontraram no soco hoje\nsorte? acho que não\ncoincidência? talvez\nhotel? trivago','Ninguém encontrou ninguém\nNinguém matou ninguém\nsem combates diretos hoje','Não houveram mano a mano hoje\nmas aposto que amanhã vai ter ;)','Vem pro x1! não?\nta, hoje não teve x1']
    eventoCombatesDiretos = random.sample(eventoCombatesDiretos, len(eventoCombatesDiretos))
    cECD = 0
    # endregion

    #region Apresentação dos tributos, pegar os tributos do vetor dos participantes que entraram no evento (+300 segs)
    statusText = '''Conheçam os tributos:'''
    i = 0
    participantesVivos.pop()
    metade = False
    for linha in participantesVivos:
        statusText += f"\nD{i + 1}:"
        for pessoa in linha:
            statusText += " @"+pessoa+" e"
        statusText = statusText[:-2]+""
        i += 1
        if (i % (len(participantesVivos)/2) == 0 and not metade):
            tweetarXmin(statusText, 30)
            statusText = ""
            metade = True
    statusText += "\nCom isso fecham os tributos selecionados"
    tweet = api.user_timeline(screen_name=api.me().screen_name, count=1, tweet_mode='extended')[0]
    tweetarXminReply(statusText,300,tweet)
    # endregion

    acabou = False
    dia = 1
    primeiroMomento = True
    while not acabou:
        aindaNaoMataram = participantesVivosLista.copy()
        mortesDoDia = []

        #region Primeiro momento, evento de abertura da cornucópia
        if (primeiroMomento):
            primeiroMomento = False
            addSorte = 0
            sorte = 0
            statusText = ""
            dado = random.randint(1,100)
            if (dado % 42 == 0):
                morre = participantesVivosLista[random.randint(0,len(participantesVivosLista) - 1)]
                participantesVivos, participantesVivosLista = removeDaListaVivos(participantesVivos, participantesVivosLista, morre)
                mortesDoDia.append(morre)
                statusText += f"\na plataforma de @{morre} explode pq começou se afobou"
            statusText += f"\ncomeça a corrida, alguns se escondem, outros tentam a sorte na cornucopia, sangue rola logo no início"
            while sorte <= 45:
                if (len(aindaNaoMataram) < 2):
                    break
                mata, morre = random.sample(aindaNaoMataram, 2)
                aindaNaoMataram.remove(mata)
                aindaNaoMataram.remove(morre)


                participantesVivos, participantesVivosLista = removeDaListaVivos(participantesVivos, participantesVivosLista, morre)
                statusText += f"\n@{mata} matou @{morre} {mataMata[cMM]}"
                cMM += 1
                mortesDoDia.append(morre)

                addSorte += random.randint(10,15)
                sorte = random.randint(0, 100) + addSorte
                if (len(participantesVivosLista) == 1):
                    acabou = True
                    anunciarMortos(mortesDoDia, participantesOriginais, participantesVivosLista, api)
                    break


            tweetarXmin(statusText, 150)
        # endregion

        if (acabou):
            break

        #region evento de x1 onde pessoa X mata pessoa Y (+30~300 segs)
        addSorte = 0
        sorte = random.randint(0,200)
        contador = 1
        metade = False
        statusText = f"Dia {dia}:"
        if (sorte > 180):
            statusText += "\n" + eventoCombatesDiretos[cECD]
            cECD += 1
        while sorte <= 180:
            if (len(aindaNaoMataram) < 2):
                break
            mata, morre = random.sample(aindaNaoMataram, 2)
            aindaNaoMataram.remove(mata)
            aindaNaoMataram.remove(morre)

            participantesVivos, participantesVivosLista = removeDaListaVivos(participantesVivos,
                                                                             participantesVivosLista, morre)
            statusText += f"\n@{mata} matou @{morre} {mataMata[cMM]}"
            cMM += 1
            mortesDoDia.append(morre)
            contador += 1


            addSorte += random.randint(30, 35)
            sorte = random.randint(0, 100) + addSorte
            if (len(participantesVivosLista) == 1):
                acabou = True
                anunciarMortos(mortesDoDia, participantesOriginais, participantesVivosLista, api)
                break
            if (contador % MAX_LINHAS == 0):
                if (not metade):
                    tweetarXmin(statusText, 10)
                    statusText = ''
                    metade = True
                else:
                    tweet = api.user_timeline(screen_name=api.me().screen_name, count=1, tweet_mode='extended')[0]
                    tweetarXminReply(statusText, 10, tweet)
        if(not contador % MAX_LINHAS == 0):
            if(metade):
                tweet = api.user_timeline(screen_name=api.me().screen_name, count=1, tweet_mode='extended')[0]
                tweetarXminReply(statusText, min(300, 15*contador), tweet)
            else:
                tweetarXmin(statusText, min(15*contador, 300))
                statusText = ''
        else:
            esperar(min(300, 15*contador))
        #endregion

        #region Evento morrer sozinho (+15~300 segs)
        addSorte = 0
        sorte = random.randint(0,100)
        contador = 1
        metade = False
        statusText = f"Dia {dia}:"

        if (sorte > 80):
            statusText = ""
        while sorte <= 75:
            addSorte += random.randint(15, 20)
            sorte = random.randint(0,100) + addSorte
            morre = random.sample(participantesVivosLista, 1)[0]
            participantesVivos, participantesVivosLista = removeDaListaVivos(participantesVivos, participantesVivosLista, morre)
            mortesDoDia.append(morre)
            contador += 1

            statusText += f"\n@{morre} {causasNaturais[cCN]}"
            cCN += 1
            if(len(participantesVivosLista) == 1):
                acabou = True
                anunciarMortos(mortesDoDia, participantesOriginais, participantesVivosLista, api)
                break
            if (contador % MAX_LINHAS == 0):
                if (not metade):
                    tweetarXmin(statusText, 10)
                    statusText = ''
                    metade = True
                else:
                    tweet = api.user_timeline(screen_name=api.me().screen_name, count=1, tweet_mode='extended')[0]
                    tweetarXminReply(statusText, 10, tweet)
        if(statusText):
            if(not metade):
                tweetarXmin(statusText, 15*contador)
            else:
                esperar(15*contador)
        #endregion

        #region Patrocinador ajudando (150 segs)
        addSorte = 0
        sorte = random.randint(0,100)
        statusText = f"Dia {dia}:"
        if (sorte <= 10):
            sortudo = random.sample(participantesVivosLista, 1)[0]
            statusText += f"\nolha que sorte\nparece que os patrocinadores estão de olho em @{sortudo} e lhe deram {items[cI]}\nesperamos que saiba como utilizar"
            cI += 1
            tweetarXmin(statusText, 150)
        #endregion

        #region Anunciar mortos do dia se não tiver terminado o evento
        if(len(mortesDoDia) == 0):
            statusText = eventoSemTiro[cEST]
            cEST += 1
            tweetarXmin(statusText, 180)
        else:
            anunciarMortos(mortesDoDia, participantesOriginais, participantesVivosLista, api)
        if (len(participantesVivosLista) == 1):
            acabou = True
            break
        #endregion

        #region Evento para os 2 útilmos participantes
        if (len(participantesVivosLista) == 2):
            statusText = ""
            dado = random.randint(1, 200)
            if (dado == 99):
                statusText = f'''
@{participantesVivosLista[0]} já não é a mesma pessoa de quando começou.
@{participantesVivosLista[1]} também não está nada bem
ambos se encontram na cornucopia
lágrimas escorrem
ambos se encaram
o destino é certo
...
ambos decidem se matar em protesto ao banho de sangue
'''
                tweetarXmin(statusText, 0)
                return None
            mata, morre = random.sample(participantesVivosLista, 2)

            statusText += f"Os ultimos sobreviventes se encontram\nUtilizam de todo seu potencial e\n@{mata} mata @{morre}\ntornando-se a última pessoa de pé em uma arena ensanguentada\nParabéns merecidamente!\nSigam a página, RT+Fav :]"

            tweetarXmin(statusText, 0)
            return None
        #endregion

        #region Evento da noite (30~300 segs)

        addSorte = 0
        sorte = random.randint(0, 100)
        statusText = f"Noite {dia}:"
        listaNoite = random.sample(participantesVivosLista, len(participantesVivosLista))
        contador = 1

        metade = False
        while sorte <= 100:
            addSorte += random.randint(15, 30)
            sorte = random.randint(0, 60)
            dado = random.randint(0, 4)
            if (dado):
                pessoa = listaNoite.pop()
                statusText += f"\n@{pessoa} {noite[cN]}"
                cN += 1
            elif (len(listaNoite) >= 2 and len(participantesVivosLista) >= 4):
                pessoa, dupla = listaNoite.pop(), listaNoite.pop()
                statusText += f"\n@{pessoa} e @{dupla} {noiteEmDupla[cNED]}"
                cNED += 1
            else:
                pessoa = listaNoite.pop()
                statusText += f"\n@{pessoa} achou {items[cI]}"
                cI += 1
            if (not listaNoite):
                break
            contador += 1
            if (contador % MAX_LINHAS == 0):
                if (not metade):
                    tweetarXmin(statusText, 10)
                    statusText = ''
                    metade = True
                else:
                    tweet = api.user_timeline(screen_name=api.me().screen_name, count=1, tweet_mode='extended')[0]
                    tweetarXminReply(statusText, 10, tweet)
                    statusText = ''
        if (not metade):
            tweetarXmin(statusText, 15 * contador)
        else:
            esperar(15 * contador)
        # endregion

        dia += 1

    #region 1 sobreviveu
    vencedor = participantesVivosLista[0]
    statusText = f'''
Depois de muita luta, fuga, camuflagem e esperteza
quem sobreviveu foi @{vencedor}

Parabéns, merecidamente

Sigam a página para mais eventos, Fav+RT = Humilde :]
'''
    tweetarXmin(statusText, 0)
    #endregion



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
    2 - Rodar HG
    S - sair
    ''')
    if(resp == "1"):
        tweetToTwitter()
    elif (resp == "2"):
        hungerGamesEvent()
    else:
        print('flw enton')
if __name__ == "__main__":
    hungerGamesEvent()
    #main()