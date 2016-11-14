from keras.applications.vgg16 import VGG16, preprocess_input,decode_predictions
from keras.preprocessing import image
import numpy as np
import json
import webbrowser
import firebase
import pygame.camera
import pygame.image
from PIL import Image


#Obtain image from webcam Camera

pygame.camera.init()
cam =  pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
img = cam.get_image()


def saveImage():
	pygame.image.save(img,"photo.bmp")
	pygame.camera.quit()


if pygame.KEYDOWN:
	saveImage()


def image():
	file_in = "photo.bmp"
	image_in = Image.open(file_in)
	file_out = "photo.png"
	image_out = image_in.save(file_out)
	return image_out




#The default input size for this model is 224x224.
imageModel = VGG16(include_top=True, weights='imagenet')

image_to_use = image()

#Convert the image to (L*W) 224*224
img = image.load_img(image_to_use, target_size=(224, 224))


x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

scores = []

preds = imageModel.predict(x)
prediction = decode_predictions(preds)#top = 3)[0]
for each in prediction:
	for tuple_ in each:
		scores.append(tuple_)

highest = 0
i = 0
check = -1000
high_list = []
previous = 0

len_ = len(scores)
for (x,y,z) in scores:
	previous = z
	if z > check:
		highest = z
		check = z
		name = y
	else:
		highest = previous

name_to_search = name

url = webbrowser.open("https://www.google.ca/search?q="+name_to_search+"&source=lnms&tbm=isch&sa=X&ved")
path_to_chrome = "'/usr/bin/google-chrome%s"
webbrowser.get(path_to_chrome).open(url)
