import tensorflow as tf
from keras import datasets
from matplotlib import pyplot as plt
data = datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = data.load_data()
training_images, test_images = training_images / 255.0, test_images / 255.0

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ]
)

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(training_images, training_labels, epochs=5)

classification = model.predict(test_images)
print(classification[0])
print(test_labels[0])

plt.imshow(test_images[0])
plt.show()