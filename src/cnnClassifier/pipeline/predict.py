import numpy as np
from tensorflow import keras
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = keras.models.load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = keras.utils.load_img(imagename, target_size = (224,224))
        test_image = keras.utils.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        preprocessed_image = keras.applications.vgg16.preprocess_input(test_image)
        result = np.argmax(model.predict(preprocessed_image), axis=1)
        print('Raw model output:', model.predict(preprocessed_image))
        print('Argmax:', result)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{ "image" : prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{ "image" : prediction}]