import speech_recognition
import speech_recognition as sr
import pyttsx3
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
blocos = ['areia vermelha',
          'areia',
          'areia das almas',
          'grama',
          'andesito',
          'pedra',
          'madeira',
          'granito',
          'carvão',
          'terracota',
          'ouro',
          'cobre',
          'ferro',
          'lápis',
          'diamante',
          'água',
          'lava',
          'neve',
          'portal',
          'fogo',
          'caverna',
          'gelo',
          'melancia',
          'bambu',
          'estante',
          'escada',
          'baú',
          'vaso',
          'mel',
          'esmeralda',
          'concreto',
          'tijolo',
          'argila',
          'arenito',
          'lanterna',
          'áborora',
          'cana',
          'vela',
          'tocha',
          'sino',
          'bigorna',
          'fornalha',
          'mesa',
          'ejetor',
          'tnt',
          'pistão',
          'para-raios',
          'placa',
          'bancada',
          'barril',
          'sinalizador',
          'poção',
          'slime',
          'porta',
          'porteira',
          'cerca',
          'esponja',
          'aldeão',
          'peixe',
          'cavalo',
          'burro',
          'coelho',
          'vaca',
          'gato',
          'galinha',
          'lula',
          'ovelha',
          'morcego',
          'papagaio',
          'porco',
          'raposa',
          'sapo',
          'tartaruga',
          'urso',
          'abelha',
          'aranha',
          'enderman',
          'golfinho',
          'golem',
          'lobo',
          'afogado',
          'zumbi',
          'blaze',
          'bruxa',
          'esqueleto',
          'dragão']
reco = sr.Recognizer()

while True:
    try:

        with speech_recognition.Microphone() as mic:

            reco.adjust_for_ambient_noise(mic, duration=0.2)
            audio = reco.listen(mic)
            text = reco.recognize_google(audio, language="pt-BR")
            text = text.lower()

            print(f"Texto reconhecido: {text}")

    except speech_recognition.UnknownValueError():
        reco = speech_recognition.Recognizer()
        continue

    ## IF'S PARA O TP ##

    for substring in blocos:
        if substring in text:
            mc.player.setTilePos(500, 10, 500)

    else:
        mc.postToChat(f"Você disse: {text}")
