import functools

import numpy as np
import tensorflow as tf
from tensorflow import keras

tf.enable_eager_execution()

TRAIN_DATA_URL = 'file:./data/counting-in-order.csv'
TEST_DATA_URL = 'file:./data/counting-with-small-numbers.csv'

train_file_path = tf.keras.utils.get_file('counting-in-order.csv', TRAIN_DATA_URL)
test_file_path = tf.keras.utils.get_file('counting-with-small-numbers.csv', TEST_DATA_URL)

LABEL_COLUMN = 'score'

# Increase epochs later
def get_dataset(file_path, **kwargs):
    dataset = tf.data.experimental.make_csv_dataset(
        file_path,
        batch_size=100,
        label_name=LABEL_COLUMN,
        na_value='?',
        num_epochs=1,
        ignore_errors=True,
        **kwargs
    )
    return dataset

raw_train_data = get_dataset(train_file_path)
raw_test_data = get_dataset(test_file_path)

def show_batch(dataset):
    for batch, label in dataset.take(1):
        for key, value in batch.items():
            print('{:20s}: {}'.format(key, value.numpy()))

show_batch(raw_train_data)

# Encode the text as numbers

# Build vocabulary
tokenizer = tfds.features.txt.Tokenizer()

vocabulary_set = set()
for text_tensor, _ in
