#!/usr/bin/env python3
import tensorflow as tf

def crop_image(image, size):
    """
    Function to crop the given image randomly to the specified size.
    
    Args:
    image (tf.Tensor): The input image as a 3D Tensor (height, width, channels).
    size (tuple): The target crop size as a tuple (height, width, channels).
    
    Returns:
    tf.Tensor: The cropped image.
    """
    
    image_height, image_width, _ = image.shape
    
   
    crop_height, crop_width, _ = size
    
   
    max_y = image_height - crop_height
    max_x = image_width - crop_width
    y_offset = tf.random.uniform([], 0, max_y, dtype=tf.int32)
    x_offset = tf.random.uniform([], 0, max_x, dtype=tf.int32)
    
    
    cropped_image = image[y_offset:y_offset + crop_height, x_offset:x_offset + crop_width, :]
    
    return cropped_image
