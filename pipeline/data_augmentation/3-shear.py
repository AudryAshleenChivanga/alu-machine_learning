#!/usr/bin/env python3
import tensorflow as tf

def shear_image(image, intensity):
    """
    Function to randomly shear the given image based on the intensity.
    
    Args:
    image (tf.Tensor): The input image as a 3D Tensor (height, width, channels).
    intensity (int): The intensity with which to shear the image. Higher values result in stronger shearing.
    
    Returns:
    tf.Tensor: The sheared image.
    """
    # Generate random shear angles within the given intensity range
    shear_x = tf.random.uniform([], -intensity, intensity, dtype=tf.float32)
    shear_y = tf.random.uniform([], -intensity, intensity, dtype=tf.float32)
    
    # Create the shear transformation matrix
    shear_matrix = tf.convert_to_tensor([
        [1.0, shear_x, 0.0],
        [shear_y, 1.0, 0.0]
    ], dtype=tf.float32)
    
    # Perform the shear transformation using tf.image.transform
    sheared_image = tf.image.transform(image, shear_matrix, interpolation='BILINEAR')
    
    return sheared_image
