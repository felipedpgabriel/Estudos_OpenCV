#!/usr/bin/env python3


# Realiza a conexao com o Tello sem decolagem, para testar o funcionamento da camera antes das decolagens
# Recomendado utilziar quando conectar pela primeira vez o pc ao Tello apos ligar

import cv2
from djitellopy import Tello

tello = Tello()
tello.connect(False)
tello.streamon()  # Inicia a camera
imagem = tello.get_frame_read()  # Thread que atualiza os frames da camera
while True:
    img = imagem.frame  # Armazena o frame capturado
    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF  # Retorna apeas o ultimo byte da tecla pressionada -> Ver operacoes bit a bit em python
    if key == ord('q'): # Define a tecla q como parada da câmera
	    break 