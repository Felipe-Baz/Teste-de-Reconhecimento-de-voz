# importa a Lib que fará o reconhecimento de voz
import speech_recognition as sr
# importa a Lib que fará a tradução dos textos
from googletrans import Translator

# Funcao responsavel por ouvir e reconhecer a fala
def ouvirFrase():
  '''
    Função para retornar a frase obtida pelo programa atravez da lib speech_recognition
    :return: Retornara a frase obtida pelo reconhecimento de voz ou -1 se houver algum erro
  '''
  # Habilita o microfone para ouvir o usuario
  ouvinte = sr.Recognizer()
  with sr.Microphone() as source:
    # Usa da função presente na speech_recognition para diminuir o ruido do microfone
    ouvinte.adjust_for_ambient_noise(source)
    # Avisa ao usuario que que esta pronto para ouvir
    print("Diga me o que devo traduzir: ")
    # Armazena o audio na variavel
    audio = ouvinte.listen(source)
    try:
      # Passa o audio para o reconhecedor de padroes do speech_recognition
      frase = ouvinte.recognize_google(audio, language='pt-BR')
      # Após alguns segundos, retorna a frase falada
      print("Você disse: " + frase)
      # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.UnkownValueError:
      print("Não entendi")
      return -1
  return frase

# Função que fará o reconhecimento da lingua desejada
def ouvirLingua():
  '''
    Função para retornar a lingua obtida pelo programa atravez da lib speech_recognition
    :return: Retornara a lingua obtida pelo reconhecimento de voz ou -1 se houver algum erro
  '''
  # Habilita o microfone para ouvir o usuario
  ouvinte = sr.Recognizer()
  with sr.Microphone() as source:
    # Usa da função presente na speech_recognition para diminuir o ruido do microfone
    ouvinte.adjust_for_ambient_noise(source)

    # Avisa ao usuario que que esta pronto para ouvir
    print("Diga me o que devo traduzir: ")
    # Armazena o audio na variavel
    audio = ouvinte.listen(source)
    try:
      # Passa o audio para o reconhecedor de padroes do speech_recognition
      frase = ouvinte.recognize_google(audio, language='pt-BR')
      # Após alguns segundos, retorna a frase falada
      print("Você disse: " + frase)
      # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.UnkownValueError:
      print("Não entendi")
      return -1
  if frase == 'português':
    return 'pt-br'


def traducao(frase, lingua):
  tradutor = Translator()
  linguaOrigem = tradutor.detect(frase)
  fraseTraduzida = tradutor.translate(frase, dest=lingua)
  print(f'A sua frase em {linguaOrigem}, foi traduzida para {lingua}. \n {frase} -> {fraseTraduzida}')
