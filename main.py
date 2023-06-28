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
    img = img.resize((128, 128))  # Ensure the image is 32x32

    image_data = np.array(img).tolist()

    return jsonify(image_data)

def request_img_upload():
    file_path = filedialog.askopenfilename()

    if file_path:
        img = Image.open(file_path)
        img.resize((128, 128))

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
