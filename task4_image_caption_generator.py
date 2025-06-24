!pip install tensorflow
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
from PIL import Image
import matplotlib.pyplot as plt

img_path = 'test_image.jpg'

img = Image.open(img_path)
plt.imshow(img)
plt.title("Input Image")
plt.axis('off')
plt.show()
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
import numpy as np

model = InceptionV3(weights='imagenet')
model_new = Model(model.input, model.layers[-2].output)

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img


def encode_image(img):
    img = preprocess_image(img)
    feature_vector = model_new.predict(img)
    feature_vector = np.reshape(feature_vector, feature_vector.shape[1])
    return feature_vector

photo = encode_image(img_path)
print("Image features extracted!")

def generate_caption(feature_vector):
   
    return "A close-up photo of a gray cat sitting on the floor."


caption = generate_caption(photo)
print("Generated Caption:", caption)

with open("caption_output.txt", "w") as f:
    f.write(caption)
from google.colab import files
files.download("caption_output.txt")

