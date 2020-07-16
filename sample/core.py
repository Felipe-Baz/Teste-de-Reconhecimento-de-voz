# -*- coding: utf-8 -*-
from .funcoes import ouvirFrase, ouvirLingua, traducao


def srTradutor():
    while True:
        frase = ouvirFrase()
        if frase != -1:
            resposta = str(input('A frase está correta? [S ou N]: \n')).strip().upper()
            if resposta[0] == 'S':
                break
        lingua = ouvirLingua()
        if lingua != -1:
            resposta = str(
                input('A frase está correta? [S ou N]: \n')).strip().upper()
            if resposta[0] == 'S':
                break
    traducao(frase, lingua)
