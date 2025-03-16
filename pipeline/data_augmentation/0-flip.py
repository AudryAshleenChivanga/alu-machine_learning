#!/usr/bin/env python3

import tensorflow as tf

def flip_image(image):
    """
    Flips the input image horizontally.

    Args:
        image: A 3D TensorFlow tensor (height, width, channels) representing the image to flip.

    Returns:
        A 3D TensorFlow tensor (height, width, channels) representing the flipped image.
    """
    return tf.image.flip_left_right(image)
