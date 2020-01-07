from google.cloud import vision
import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client-secret.json"


def detect_text_uri(path):
	client = vision.ImageAnnotatorClient()
	
	with io.open(path, 'rb') as image_file:
		content = image_file.read()
	image = vision.types.Image(content=content)
	response = client.text_detection(image=image)
	texts = response.text_annotations
	return texts[0].description
	

#detect_text_uri("./IMG-0092.jpg")
#detect_text_uri("https://media.npr.org/assets/img/2016/04/17/handwritten-note_wide-941ca37f3638dca912c8b9efda05ee9fefbf3147.jpg?s=1400")
print("text message twilio")