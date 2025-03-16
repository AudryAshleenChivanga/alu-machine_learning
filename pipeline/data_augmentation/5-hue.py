#!/usr/bin/env python3
import tensorflow as tf

def change_hue(image, delta):
    """
    Function to change the hue of the given image.
    
    Args:
    image (tf.Tensor): The input image as a 3D Tensor (height, width, channels).
    delta (float): The amount by which to change the hue. Should be a float in the range [-1, 1], where:
                  - Positive values shift the hue towards the red end of the spectrum.
                  - Negative values shift the hue towards the blue end of the spectrum.
    
    Returns:
    tf.Tensor: The hue-altered image.
    """
    # Change the hue using tf.image.adjust_hue
    hue_changed_image = tf.image.adjust_hue(image, delta)
    
    return hue_changed_image
