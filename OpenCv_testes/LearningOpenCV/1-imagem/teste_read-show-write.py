#!/usr/bin/env python

# Felipe de Paula Gabriel

# imread('path do arquivo', int(como_ler_a_imagem)) -> 1 e o padrao
# imshow('nome da janela', variavel_da_imagem)
    # waitKey(int(tempo_em_milissegundos)) -> se for 0, espera ate q uma tecla seja pressionada
# imwrite('nome do arquivo', variavel_da_imagem)

import cv2
import sys

# le a imagem escala de cinza
img = cv2.imread("/home/felipe/Hawkings/OpenCV/OpenCv_testes/LearningOpenCV/1-imagem/veneza.jpg",2)
if img is None: # verifica se foi possivel ler
    sys.exit("Could not read the image.")
else:
    cv2.imshow('Display window', img) # mostra em uma outra janela
    k = cv2.waitKey(0) # espera ate que uma tecla seja pressionada (e armazena em k)
    # cv2.destroyAllWindows() 
    if k == ord('s'): # se a tecla pressionada for 's'
        print("Salvando imagem em .png")
        cv2.imwrite('veneza.png', img) # gera um arquivo de imagem com a que foi lida
    else:
        print("A imagem nao sera salva")

cv2.destroyAllWindows()