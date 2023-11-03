#!/usr/bin/env python3

from imutils.video import VideoStream
import imutils
import time
import cv2
import sys


# Define o tipo de Aruco
ARUCO_TYPE = "DICT_5X5_50"

# Tipos de aruco suportados pela biblioteca OpenCV
ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

# verifica se o tipo de aruco existe e eh suportado pelo OpenCV
	# diciopnario.get(str) -> se nao encontrado no dicionario, retorna None por padrao
	# Caso queira adicionar um retorno especifico, basta adiciona-lo com virgula apos a str
if ARUCO_DICT.get(ARUCO_TYPE) is None:
	print(f"[INFO] O tipo de aruco {ARUCO_TYPE} nao eh suportado")
	sys.exit(0)

print(f"[INFO] Detectando o tipo {ARUCO_TYPE}...")
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[ARUCO_TYPE]) # 1 - Seleciona o tipo de aruco do dicionario
arucoParams = cv2.aruco.DetectorParameters_create()  # 2 - Define os parametros de deteccao

# Inicializa o video e prepara a camera
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# Roda os frames em loop para streamar o video da camera
while True:
	# Le os frames da camera e redimensiona
	frame = vs.read()  # cv2.imread()
	frame = imutils.resize(frame, width=1000)

	# detect ArUco markers in the input frame 
	# 3 - Detecta os marcadores aruco 
		# corners => lista das coordenadas (x,y) 
		# ids => "numero" do aruco dentro da biblioteca 
		# rejected => NAO ENTENDI
	(corners, ids, rejected) = cv2.aruco.detectMarkers(frame,
		arucoDict, parameters=arucoParams)
	
    
	if len(corners) > 0:  # Uma forma de confirmar que o aruco foi detectado

		ids = ids.flatten()  # (achata lista de id's) Nao encontrei funcao pratica pra essa linha
		
		for (markerCorner, markerID) in zip(corners, ids):  # estudar depois

			# retorna as coordenadas dos cantos do aruco nessa ordem:
				# top-left, top-right, bottom-right, and bottom-left
			
			corners = markerCorner.reshape((4, 2))  # Transforma um vetor em matriz, pegando os valores em ordem
			(topLeft, topRight, bottomRight, bottomLeft) = corners  # Separa os valores da matriz em variáveis

			# converte os pares de coordenadas em iteiros, para serem usados pelo OpenCV
			topRight = (int(topRight[0]), int(topRight[1]))
			bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
			bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
			topLeft = (int(topLeft[0]), int(topLeft[1]))

        	# Desenha a caixa em volta do aruco
				# line(imagem, ponto1, ponto2, (rgb), espessura)
			cv2.line(frame, topLeft, topRight, (255, 0, 0), 2)
			cv2.line(frame, topRight, bottomRight, (255, 0, 0), 2)
			cv2.line(frame, bottomRight, bottomLeft, (255, 0, 0), 2)
			cv2.line(frame, bottomLeft, topLeft, (255, 0, 0), 2)

			# "Desenha o centro" do aruco 
				# circle(imagem, (coordenadas_centro), raio, (cor), espessura)
			cX = int((topLeft[0] + bottomRight[0]) / 2.0)
			cY = int((topLeft[1] + bottomRight[1]) / 2.0)
			cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)

			# Desenha o ids do aruco detectado na tela.
				# (imagem, texto, org, font_texto, escala_texto, (cor), espessura)
			cv2.putText(frame, str(markerID), (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	
	# Mostra os frames em sequencia para mostrar o vídeo
	cv2.imshow("Frame", frame) 
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
    
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

