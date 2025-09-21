import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Load pretrained MobileNetV2
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Load and preprocess a fire image
# img_path = "/Users/hpoduri/Downloads/test_fire.jpeg"  # Replace with your image path
img_path = "shirt.jpeg"
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

# Make prediction
predictions = model.predict(img_array)
decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]

# Print top predictions
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i + 1}: {label} ({score * 100:.2f}%)")
