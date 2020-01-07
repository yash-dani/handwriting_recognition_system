# Import statements
from google.cloud import vision
import os
import io

# Imports the JSON key required to call the API, which can be generated on the Google Cloud Console
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client-secret.json"

# Function to detect text using a local path
def detect_text_uri(path):
	# Creates the API client
	client = vision.ImageAnnotatorClient()
	
	with io.open(path, 'rb') as image_file:
		content = image_file.read()
		
	# Detects text and stores in JSON object 
	image = vision.types.Image(content=content)
	response = client.text_detection(image=image)
	texts = response.text_annotations
	
	# returns raw text data 
	return texts[0].description
	
# Quick example of usecase 
#detect_text_uri("./IMG-0092.jpg")
