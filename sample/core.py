# -*- coding: utf-8 -*-
from . import funcoes


def srtradutor():
    while True:
        frase = funcoes.ouvirFrase()
        if frase != -1:
            resposta = str(input('A frase está correta? [S ou N]: \n')).strip().upper()
            if resposta[0] == 'S':
                break
        lingua = funcoes.ouvirLingua()
        if lingua != -1:
            resposta = str(
                input('A frase está correta? [S ou N]: \n')).strip().upper()
            if resposta[0] == 'S':
                break
    funcoes.traducao(frase, lingua)
