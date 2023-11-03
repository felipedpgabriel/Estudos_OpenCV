# Felipe de Paula Gabriel

# VideoCapture('path do arquivo'*)
    # * video = 'path do arquivo de video'
    # * sequencia de imagens = seguir um padrao e usar %0n --> n = numero de digitos do padrão
        # * ex: '/home/eu/Documentos/imagem%04.jpg' --> imagem0001, imagem0002, imagem0003 ...
    # isOpened() -> bool
    # get() -> enumeracao dos argumentos e suas funcoes:
        # https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
    # read() -> tupla () -> bool, frame(imagem)
    # release() -> Fecha o arquivo de vídeo ou dispositivo de captura.

import cv2

# Cria um objeto de captura de vídeo, nesse caso, estamos lendo um vídeo de um arquivo
vid_capture = cv2.VideoCapture('//home/felipe/Hawkings/OpenCV/OpenCv_testes/LearningOpenCV/2-video/narutoCorrendo.mp4')

# Verifica se o vídeo foi aberto corretamente
if(vid_capture.isOpened() == False):
    print("Deu ruim!")
else:
    # Recolhe a taxa de frames
    fps = int(vid_capture.get(5)) # 5 - CAP_PROP_FPS
    print("Frame Rate: ", fps, "frames por segundo")

    # Recolhe o número de frames
    frame_count = vid_capture.get(7) # 7 - CAP_PROP_FRAME_COUNT
    print("Frame Count: ", frame_count)


while(vid_capture.isOpened()):
    # O método vCapture.read() retorna uma tupla, o primeiro elemento é um booleano e o segundo é um frame
    ret, frame = vid_capture.read()

    #Verifica se o frame está ou não presente e o exibe caso esteja
    if ret == True:
        cv2.imshow("Frame", frame)
        # Espera 43ms entre dois frames consecutivos e quebra o loop se a tecla q for pressionada
        k = cv2.waitKey(int(1000/fps))
        # 113 é um código ASCII para a letra "q"
        if k == ord('q'):   
            break
    else:
        break

# Libera os objetos
vid_capture.release()
cv2.destroyAllWindows()