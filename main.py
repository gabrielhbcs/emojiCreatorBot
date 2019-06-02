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

def tweetarXmin(texto, tempo):
    print(f"\tTweetando: \n{texto}")
    api.update_status(status = texto)
    print(f"\tAguardando {tempo} segundos\n")
    time.sleep(30)


def removeDaListaVivos(lista1, lista2, morre):
    for linha in lista1:
        if (morre in linha):
            linha.remove(morre)
    lista2.remove(morre)
    return lista1, lista2

def hungerGamesEvent():
    statusText = '''
QUE COMECEM OS JOGOS VORAZES
Para participar comente algo nesse status, deixe seu grito de guerra, seu texto motivacional, qlqr coisa.
Você será notificado da sua participação
Se ganhar vc será reconhecido ;)

RT/Fav pra fortalecer o bot <3
As inscrições terminam em 10 minutos
'''
    tweetarXmin(statusText, 600)

    print("Pegando nomes do último status")
    #tweet = api.user_timeline(screen_name=api.me().screen_name, count=1, tweet_mode='extended')[0]
    #replies = tweepy.Cursor(api.search, q=f'to:@{api.me().screen_name}', since_id=tweet.id, tweet_mode='extended').items()
    participantesVivos = [[]]
    participantesVivosLista = []
    cont = 0
    i = 0
    while True and cont < 12:
        '''
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
            participantesVivosLista.append(reply.user.screen_name)
            cont += 1
        except:
            break
        '''
        '''
        for _ in range(4):
            for _ in range(2):
                participante = input("Digite um nome: ")
                if (cont % 2 == 0):
                    participantesVivos[i].append(participante)
                else:
                    participantesVivos[i].append(participante)
                    participantesVivos.append([])
                    i += 1
                participantesVivosLista.append(participante)
                cont += 1
        '''
        participantesVivos = [['Gabriel','Werneck'],['Yasmin','Mayara'],['Luciano','Tut'],['Gustavo','Amanda'],['Pedro','Mary'],['Douglas','Caio'],[]]
        participantesOriginais = [['Gabriel', 'Werneck'], ['Yasmin', 'Mayara'], ['Luciano', 'Tut'], ['Gustavo', 'Amanda'],
                              ['Pedro', 'Mary'], ['Douglas', 'Caio'], []]
        participantesVivosLista = ['Gabriel','Werneck','Yasmin','Mayara','Luciano','Tut','Gustavo','Amanda','Pedro','Mary','Douglas','Caio']
        cont = 10
        break


    if (cont < 6):
        statusText = "Preciso de pelo menos 6 pessoas pra rodar o evento :( \n#NaoVaiTerHG"
        tweetarXmin(statusText, 600)
        return None

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

    eventoSemTiro = ['Sem tiros de canhão hoje\n\nsó isso mesmo','Não houveram mortes hoje','Ninguém morreu hoje\nimpressionante, mas o jogo tem que continuar :)','Não houveram tiros de canhão hoje\nserá que hoje os tributos dormem mais tranquilos?', 'Nenhum tiro de canhão foi dado hoje']
    eventoSemTiro = random.sample(eventoSemTiro, len(eventoSemTiro))
    cEST = 0

    eventoCombatesDiretos = ['Os tributos não se encontraram no soco hoje\nsorte? acho que não\ncoincidência? talvez\nhotel? trivago','Ninguém encontrou ninguém\nNinguém matou ninguém\nsem combates diretos hoje','Não houveram mano a mano hoje\nmas aposto que amanhã vai ter ;)','Vem pro x1! não?\nta, hoje não teve x1']
    eventoCombatesDiretos = random.sample(eventoCombatesDiretos, len(eventoCombatesDiretos))
    cECD = 0


    statusText = '''
Conheça os participantes do próximo HungerGames:
'''
    i = 0
    participantesVivos.pop()
    for linha in participantesVivos:
        statusText += f"\nD{i + 1}:"
        for pessoa in linha:
            statusText += " @"+pessoa+" e"
        statusText = statusText[:-1]+""
        i += 1
    statusText += "\nO evento começará em 5 minutos!"
    tweetarXmin(statusText, 300)

    acabou = False
    primeiroMomento = True
    dia = 1
    while not acabou:
        aindaNaoMataram = participantesVivosLista.copy()
        mortesDoDia = []
        # primeiro momento
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
                    break


            tweetarXmin(statusText, 300)

        if (acabou):
            break

        # while de X mata Y com mais de 12 sobreviventes
        if(len(participantesVivosLista) > 12):
            addSorte = 0
            sorte = random.randint(0, 100)
            statusText = f"Dia {dia}:"
            if (sorte > 90):
                statusText += "\n" + eventoCombatesDiretos[cECD]
                cECD += 1
            while sorte <= 90:
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

                addSorte += random.randint(15, 20)
                sorte = random.randint(0, 100) + addSorte
                if (len(participantesVivosLista) == 1):
                    acabou = True
                    break

            tweetarXmin(statusText, 300)

            if (acabou):
                break

        # while de X mata Y
        addSorte = 0
        sorte = random.randint(0,100)
        statusText = f"Dia {dia}:"
        if (sorte > 90):
            statusText += "\n" + eventoCombatesDiretos[cECD]
            cECD += 1
        while sorte <= 90:
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

            addSorte += random.randint(15, 20)
            sorte = random.randint(0, 100) + addSorte
            if (len(participantesVivosLista) == 1):
                acabou = True
                break

        tweetarXmin(statusText, 300)


        if(acabou):
            break


        # Evento morrer sozinho
        addSorte = 0
        sorte = random.randint(0,100)
        statusText = f"Dia {dia}:"
        if (sorte > 50):
            statusText = ""
        while sorte <= 50:
            addSorte += random.randint(15,20)
            sorte = random.randint(0,100) + addSorte
            morre = random.sample(participantesVivosLista, 1)[0]
            participantesVivos, participantesVivosLista = removeDaListaVivos(participantesVivos, participantesVivosLista, morre)
            mortesDoDia.append(morre)

            statusText += f"\n@{morre} {causasNaturais[cCN]}"
            cCN += 1
            if(len(participantesVivosLista) == 1):
                acabou = True
                break
        if(statusText):
            tweetarXmin(statusText, 300)

        # patrocinador ajudando
        addSorte = 0
        sorte = random.randint(0,100)
        statusText = f"Dia {dia}:"
        if (sorte <= 10):
            sortudo = random.sample(participantesVivosLista, 1)[0]
            statusText += f"\nolha que sorte\nparece que os patrocinadores estão de olho em @{sortudo} e lhe deram {items[cI]}\nesperamos que saiba como utilizar"
            cI += 1
            tweetarXmin(statusText, 300)

        # Anunciar mortos do dia
        if(len(mortesDoDia) > 0):
            if(len(mortesDoDia) == 1):
                i = 1
                for linha in participantesOriginais:
                    if(mortesDoDia[0] in linha):
                        statusText = f"hoje fora ouvido apenas um tiro de canhão: \n@{mortesDoDia[0]} do distrito {i}\nserá bom ou ruim?"
                        break
                    i += 1
            else:
                statusText = f'''
Hoje foram ouvidos {len(mortesDoDia)} tiros de canhão na distância:
'''
                for morto in mortesDoDia:
                    statusText += f"\n@{morto} "
                    i = 1
                    for linha in participantesOriginais:
                        if (morto in linha):
                            statusText += f"do distrito {i}"
                            break
                        i += 1
            tweetarXmin(statusText, 300)
        else:
            statusText = eventoSemTiro[cEST]
            cEST += 1
            tweetarXmin(statusText, 300)


        #Evento da noite
        addSorte = 0
        sorte = random.randint(0, 100)
        statusText = f"Noite {dia}:"
        listaNoite = random.sample(participantesVivosLista, len(participantesVivosLista)-1)
        while sorte <= 100:
            addSorte += random.randint(10,20)
            sorte = random.randint(0, 60)
            dado = random.randint(0,4)
            if(dado):
                pessoa = listaNoite.pop()
                statusText += f"\n@{pessoa} {noite[cN]}"
                cN += 1
            elif(len(listaNoite) >= 2):
                pessoa, dupla = listaNoite.pop(), listaNoite.pop()
                statusText += f"\n@{pessoa} e @{dupla} {noiteEmDupla[cNED]}"
                cNED += 1
            else:
                pessoa = listaNoite.pop()
                statusText += f"\n@{pessoa} verifica {items[cI]}"
                cI += 1
            if(not listaNoite):
                break

        tweetarXmin(statusText, 300)


        dia += 1



        # Evento para os 2 útilmos participantes
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


    # 1 sobreviveu
    vencedor = participantesVivosLista[0]
    statusText = f'''
Depois de muita luta, fuga, camuflagem e esperteza
quem sobreviveu foi @{vencedor}

Parabéns, merecidamente

Sigam a página para mais eventos, Fav+RT = Humilde :]
'''
    tweetarXmin(statusText, 0)



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