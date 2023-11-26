# Create a test harness for evaluating a model
from generate_dataset import prepare_dataset
from keras_model import define_model
import tensorflow as tf


def test_harness():
    # prepare dataset
    data = prepare_dataset()
    train_x, train_y, test_x, test_y = data.load_dataset()

    # prepare pixel data
    train_x, test_x = data.preprocess_pixels(train_x, test_x)

    # define model
    model = define_model()

    # fit model
    model.fit(train_x, train_y, epochs=100, batch_size=64, verbose=0)

    # save model
    model.save("model.h5")


if __name__ == "__main__":
    test_harness()
