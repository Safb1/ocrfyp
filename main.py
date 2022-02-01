#Importing Relevant Libraries
import os
from flask import Flask, render_template, request, redirect, url_for
from OCR import ocr_core

UPLOAD_FOLDER = '/Users/safabutt/PycharmProjects/OCRfyp/static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            return render_template('output.html', msg='No file selected')
        file = request.files['file']
        if file.filename == '':
            return render_template('output.html', msg='No file selected')

        if file and allowed_file(file.filename):
            file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))

        extracted_text = ocr_core(file)

        return render_template('output.html',
                        msg='Successfully processed',
                        extracted_text=extracted_text,
                        img_src=UPLOAD_FOLDER + file.filename)

    elif request.method == 'GET':
        return render_template('output.html')

if __name__ == '__main__':
    app.run()

# photo = "/Users/safabutt/PycharmProjects/OCRfyp/images/demo.png"
#
# app.config['DEBUG'] = False
# app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'
#
# # Class for Image to Text
# class GetText(object):
#     def __init__(self, file):
#         self.file = pytesseract.image_to_string(Image.open())
#
#
# def home():
#     if request.method == 'POST':
#         # Check if the form is empty
#         if 'photo' not in request.files:
#             return 'there is no photo in form'
#
#         photo = request.files['images']
#         path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
#         # Save the photo in the upload folder
#         photo.save(path)
#
#         # Class instance
#         textObject = GetText(photo.filename)
#         result = textObject.file
#
#         # Send the result text as a session to the /result route
#         return redirect(url_for('result', result=result))
#     return render_template('index.html')
#
#
# # Result page
# @app.route('/result', methods=['GET', 'POST'])
# def result():
#     result = request.args.get('result', None)
#     return render_template('result.html', result=result)


#---EXTRA NOTES---
#img = Image.open('demo.png')
#img = cv2.imread('demo.png')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 11)
#config = "--psm 3"


#text = pytesseract.image_to_string(adaptive_threshold, config=config)
#text = pytesseract.image_to_string(img)
#print(text)

#cv2.imshow(img)
#cv2.imshow("gray", gray)
#cv2.imshow("adaptive threshold", adaptive_threshold)
#cv2.waitKey(0)