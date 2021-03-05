import io
from flask import Flask, render_template, request, send_from_directory, send_file, Response
from PIL import Image
import requests
import os

app = Flask(__name__)

# function to load img from url
def load_image_url(url):
	response = requests.get(url)
	img = Image.open(io.BytesIO(response.content))
	return img

@app.route("/")
def index():
	return render_template('index.html')


@app.route("/detect", methods=['POST', 'GET'])
def upload():
	if request.method == 'POST':
		try:
			# open image
			file = Image.open(request.files['file'].stream)

			# remove alpha channel
			rgb_im = file.convert('RGB')
			rgb_im.save('file.jpg')
		
		# failure
		except:
			return render_template("failure.html")

	elif request.method == 'GET':

		# get url
		url = request.args.get("url")
		# save
		try:
			# save image as jpg
			# urllib.request.urlretrieve(url, 'file.jpg')
			rgb_im = load_image_url(url)
			rgb_im = rgb_im.convert('RGB')
			rgb_im.save('file.jpg')

		# failure
		except:
			return render_template("failure.html")

	# create file-object in memory
	file_object = io.BytesIO()

	# write PNG in file-object
	rgb_im.save(file_object, 'PNG')

	# move to beginning of file so `send_file()` it will read from start    
	file_object.seek(0)

	#return send_file(file_object, mimetype='image/PNG')

	render_template('index.html')

if __name__ == "__main__":
	# run app
	app.run(debug = True)