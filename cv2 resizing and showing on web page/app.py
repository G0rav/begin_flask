import os
import cv2
import matplotlib.pyplot as plt
from flask import Flask, render_template, request

upload_folder = "static"
app = Flask(__name__)

def load_img(image_location):
    img = cv2.imread(image_location)
    img = cv2.resize(img, (512,512), interpolation=cv2.INTER_AREA)
    return img

@app.route("/", methods=["GET", "POST"])
def upload_file():
    
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(upload_folder, image_file.filename)
            image_file.save(image_location)

            new_image = load_img(image_location)
            new_image_name = 'n'+image_file.filename
            new_image_location = os.path.join(upload_folder, new_image_name)
            cv2.imwrite(new_image_location, new_image)

            pred = load_img(image_location)
            pred_image_name = 'p'+image_file.filename
            pred_location = os.path.join(upload_folder, pred_image_name)
            cv2.imwrite(pred_location, pred)

            return render_template("index.html", test='File uploaded.', image_name = new_image_name, pred_image_name= pred_image_name)
        else:
            return render_template("index.html", test='Please select a file to upload.', 
                                    image_name = None, pred_image_name= None)
   
    return render_template("index.html", test='You are on Index.', image_name = None, pred_image_name= None)

if __name__ == "__main__":
    app.run(debug = True)
