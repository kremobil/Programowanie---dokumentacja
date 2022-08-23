import tensorflow as tf
import urllib.request
import zipfile
import numpy as np
from PIL import Image
from keras.preprocessing import image

from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras import models, layers

url = "https://storage.googleapis.com/laurencemoroney-blog.appspot.com/horse-or-human.zip"
file_name = "horse_or_human.zip"
training_dir = 'horse-or-human/training/'

validation_url = 'https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip'
validation_filename = 'validation-horse-or-human.zip'
validation_dir = 'horse-or-human/validation'

train_datagen = ImageDataGenerator(rescale=1/255)
train_generator = train_datagen.flow_from_directory(training_dir, (300, 300), class_mode='binary')
validation_generator = train_datagen.flow_from_directory(validation_dir, target_size=(300, 300), class_mode='binary')

model = models.Sequential([
    layers.Conv2D(16, (3, 3), activation='relu', input_shape=(300, 300, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(RMSprop(0.001), 'binary_crossentropy', ['accuracy'])

history = model.fit_generator(train_generator, epochs=15, validation_data=validation_generator)

# images = ['test1.jpg', 'test2.jpg']
#
# for image in images:
#
#
#
#
#     test = Image.open(f'test/{image}').resize((300, 300))
#     print(test.format)
#     print(test.size)
#     print(test.mode)
#     img_as_array = np.asarray(test)
#     # img_as_array = np.expand_dims(img_as_array, axis=0)
#     classes = model.predict(img_as_array, 10)
#     print(classes)



