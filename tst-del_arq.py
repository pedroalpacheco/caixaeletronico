# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:33:38 2015

@author: papacheco
"""

import os

#valordez = input("Digite quantidade A SER EXCLUIDA de notas R$ 10,00:")
#os.chdir("/home/papacheco/Dropbox/scripts/python/projetos-py/caixaeletronico/10")
#nota = "dez-reais"
#for i in range(valordez):
#    vl = "%s-%s" % (i,nota)
#    fo = open(vl, "wb")
    
#valorvinte = input("Digite a quantidade A SER EXCLUIDA de notas R$ 20,00:")
#os.chdir("/home/papacheco/Dropbox/scripts/python/projetos-py/caixaeletronico/20")
#nota = "vinte-reais"
#for i in range(valorvinte):
#    vl = "%s-%s" % (i,nota)
#    fo = open(vl, "wb")
    
#valorcinquenta = input("Digite a quantidade A SER EXCLUIDA de notas R$ 50,00:")
#os.chdir("/home/papacheco/Dropbox/scripts/python/projetos-py/caixaeletronico/50")
#nota = "cinquenta-reais"
#for i in range(valorcinquenta):
#    vl = "%s-%s" % (i,nota)
#    fo = open(vl, "wb")
    
#valorcem = input("Digite a quantidade A SER EXCLUIDA de notas  R$ 100,00:")
#os.chdir("/home/papacheco/Dropbox/scripts/python/projetos-py/caixaeletronico/100")
#nota = "cem-reais"
#for i in range(valorcem):
#    vl = "%s" % (i,nota)
#    print vl
#    fo = os.remove(vl)
    
for arquivo in os.walk("/home/papacheco/Dropbox/scripts/python/projetos-py/caixaeletronico/100"):
    print(arquivo)

#valorcem = input("Digite a quantidade A SER EXCLUIDA de notas  R$ 100,00:")
#os.chdir("/home/papacheco/Dropbox/scripts/python/projetos-py/caixaeletronico/100")
#nota = "cem-reais"
#for i in range(valorcem):
#    vl = "%s" % (i,nota)
#    print vl
#    fo = os.remove(vl)
