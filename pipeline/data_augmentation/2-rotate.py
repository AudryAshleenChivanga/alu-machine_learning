#!/usr/bin/env python3
import tensorflow as tf

def rotate_image(image):
    """
    Function to rotate the given image by 90 degrees counter-clockwise.
    
    Args:
    image (tf.Tensor): The input image as a 3D Tensor (height, width, channels).
    
    Returns:
    tf.Tensor: The rotated image.
    """
    # Rotate the image by 90 degrees counter-clockwise using TensorFlow
    rotated_image = tf.image.rot90(image, k=1)
    
    return rotated_image
