
# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

from model import OpenNsfwModel, InputType
from image_utils import create_tensorflow_image_loader
from image_utils import create_yahoo_image_loader

from tools.download import deal_images
from frame import config


def yahoo_test(input_file, model_weights, image_loader=config.IMAGE_LOADER_YAHOO, input_type=InputType.TENSOR.name.lower()):
    # parser = argparse.ArgumentParser()

    # parser.add_argument("input_file", help="Path to the input image.\
    #                     Only jpeg images are supported.")
    # parser.add_argument("-m", "--model_weights", required=True,
    #                     help="Path to trained model weights file")

    # parser.add_argument("-l", "--image_loader",
    #                     default=IMAGE_LOADER_YAHOO,
    #                     help="image loading mechanism",
    #                     choices=[IMAGE_LOADER_YAHOO, IMAGE_LOADER_TENSORFLOW])

    # parser.add_argument("-t", "--input_type",
    #                     default=InputType.TENSOR.name.lower(),
    #                     help="input type",
    #                     choices=[InputType.TENSOR.name.lower(),
    #                              InputType.BASE64_JPEG.name.lower()])

    # args = parser.parse_args()

    ret = {}

    model = OpenNsfwModel()

    with tf.Session() as sess:
        input_type = InputType[input_type.upper()]
        model.build(weights_path=model_weights, input_type=input_type)
        
        for url, file in input_file.items():
            fn_load_image = None

            if input_type == InputType.TENSOR:
                if image_loader == config.IMAGE_LOADER_TENSORFLOW:
                    fn_load_image = create_tensorflow_image_loader(sess)
                else:
                    fn_load_image = create_yahoo_image_loader()
            elif input_type == InputType.BASE64_JPEG:
                import base64
                fn_load_image = lambda filename: np.array([base64.urlsafe_b64encode(open(filename, "rb").read())])

            sess.run(tf.global_variables_initializer())

            image = fn_load_image(file)

            predictions = \
                sess.run(model.predictions, feed_dict={model.input: image})

            # max_index = np.argmax(predictions)
                # print("Results for '{}'".format(new_file))
                # print("\tSFW score:\t{}\n\tNSFW score:\t{}".format(*predictions[0]))
            ret[url] = {'se': round((predictions[0][1]), 2)}
    return ret


def check_images(urls):
    files = deal_images(urls)
    return yahoo_test(files, config.MOD_DIR + 'yahoo/open_nsfw-weights.npy')
