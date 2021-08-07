# Import opencv
import cv2
# Import uuid
import uuid
# Import Operating System
# Biblioteca para interactuar con el sistema operativo
import os
import subprocess
# Import time
import time
# Biblioteca para crear clonar repositorios de git
from git import Repo

labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']
number_imgs = 5

IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')
print(IMAGES_PATH)

# Crear la carpeta si esta no existe
if not os.path.exists(IMAGES_PATH):
    # Detectar en que sistema operativo estoy trabajando
    if os.name == 'nt':
        # Crear el directorio. Se uso makedirs() debido a que mkdir solo crea una instancia de los directorios
        os.makedirs(IMAGES_PATH)
# Disgregar cada uno de los nombres de los labels
for label in labels:
    # Crear un path para la direccion de cada una de las carpetas
    path = os.path.join(IMAGES_PATH, label)
    # Crear una carpeta para cada uno de los labels
    if not os.path.exists(path):
        os.makedirs(path)

for label in labels:
    # Coneccion con el dispositivo de captura puede ser 0, 1 depende de los
    # dispositivos que tengas conectados
    cap = cv2.VideoCapture(0) #Connect to out webcam or capture device
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        # Guarda la imagen en un archivo local
        cv2.imwrite(imgname, frame)
        # Muestra la imagen tomada
        cv2.imshow('frame', frame)
        time.sleep(2)

        # https://stackoverflow.com/questions/53357877/usage-of-ordq-and-0xff
        # Presionar "q" para romper el proceso
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Dejar la captura
cap.release()
cv2.destroyAllWindows()

def labelimg_gen():
    # Generación de etiquetas
    LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')
    if not os.path.exists(LABELIMG_PATH):
        os.mkdir(LABELIMG_PATH)
        Repo.clone_from('https://github.com/tzutalin/labelImg', LABELIMG_PATH)
#   Intento fallido de replicar en código el acceso a la terminal
#     os.chdir('C:/Users/jorta/PycharmProjects/TFOD_Course/Tensorflow/labelimg')
#     subprocess.call('pyrcc5 -o libs/resources.py resources.qrc')
#     subprocess.run('python labelImg.py')
#       En la terminal
#       Ingresar al repositorio de github descargado pyrcc5 -o libs/resources.py resources.qrc
#       Ejecutar el programa para image labelling python labelImg.py