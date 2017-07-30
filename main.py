from keras.applications.vgg16 import VGG16, preprocess_input,decode_predictions
from keras.preprocessing import image
import numpy as np
import webbrowser
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

vid = cv2.VideoCapture(0)
while(True):
	_, frame = vid.read()
	cv2.imshow('frame', frame)
	cv2.putText(frame,'Press (s) to search',(10,500), font, 1,(255,255,255),2)
	if cv2.waitKey(1) & 0xFF == ord('s'):
		cv2.imwrite("frame.jpg",frame)
		break
vid.release()
cv2.destroyAllWindows()




imageModel = VGG16(include_top=True, weights='imagenet')

image_to_use = "frame.jpg"

#The default input size for this model is 224x224
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
#Initiate the highest value and the iterator to zero
highest = 0
i = 0

check = -1000#Dummy variable to initiate iteration
previous = 0#Variable to obtain the previous number in the loop.

for (x,y,z) in scores:
	previous = z
	if z > check:
		highest = z #Set the highest to the score
		check = z #Compare with highest value
		name = y #Obtain the name
	else:
		highest = previous #compare with the previous value
#what would you like google to search
name_to_search = name

url = webbrowser.open("https://www.google.ca/search?q="+name_to_search+"&source=lnms&tbm=isch&sa=X&ved")#Tweak for own needs.
#open the web browser				
webbrowser.open(url)



