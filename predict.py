import numpy as np
from PIL import Image
import cv2
import tensorflow as tf

class model:
    def __init__(self, filename):
        self.filename = filename

    def model_prediction(self):

        model_path = "Model/imageclassifier.h5"
        load_model = tf.keras.models.load_model(model_path)

        imagename = self.filename
        image = cv2.imread(imagename)

        image_fromarray = image.fromarray(image, "RGB")
        resize_image = image_fromarray.resize((256, 256))
        expand_input = np.expand_dims(resize_image, axis=0)
        input_data = np.array(expand_input)
        input_data = input_data/255
        predict = load_model.predict(input_data)
        result = pred.argmax()

        if result >= 0.5:
            prediction = "Predicted class is Normal"
            return [{'image': prediction}]
        elif result < 0.5:
            prediction = "Predicted class is Drowsy"
            return [{'image': prediction}]
        else:
            return [{"Error: Please select another image !!!"}]




print('Successfully Run')