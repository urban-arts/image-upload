from flask import Flask, jsonify
from PIL import Image
import numpy as np
from tkinter import filedialog, Tk, Button
import os
import threading

app = Flask(__name__)

@app.route('/image_data', methods=['GET'])
def get_image_data():
    img = Image.open('upload.png')

    # Calculate aspect ratio
    aspect_ratio = img.width / img.height

    if img.width > img.height:
        new_width = 128
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = 128
        new_width = int(new_height * aspect_ratio)

    img = img.resize((new_width, new_height))

    image_data = np.array(img).tolist()

    return jsonify(image_data)

def request_img_upload():
    file_path = filedialog.askopenfilename()

    if file_path:
        img = Image.open(file_path)

        # Calculate aspect ratio
        aspect_ratio = img.width / img.height

        if img.width > img.height:
            new_width = 128
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = 128
            new_width = int(new_height * aspect_ratio)

        img = img.resize((new_width, new_height))

        if os.path.exists('upload.png'):
            os.remove('upload.png')
        
        img.save('upload.png')

def run_flask_app():
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    threading.Thread(target=run_flask_app).start()

    root = Tk()
    Button(root, text='Update', command=request_img_upload).pack()
    root.mainloop()
