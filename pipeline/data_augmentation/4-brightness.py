import tensorflow as tf

def change_brightness(image, max_delta):
    """
    Function to randomly change the brightness of the given image.
    
    Args:
    image (tf.Tensor): The input image as a 3D Tensor (height, width, channels).
    max_delta (float): The maximum amount by which to change the brightness. Positive values brighten the image, 
                       and negative values darken it.
    
    Returns:
    tf.Tensor: The brightness-altered image.
    """
    # Randomly change the brightness of the image within the range [-max_delta, max_delta]
    brightness_delta = tf.random.uniform([], -max_delta, max_delta, dtype=tf.float32)
    
    # Adjust the image brightness using tf.image.adjust_brightness
    brightened_image = tf.image.adjust_brightness(image, brightness_delta)
    
    return brightened_image
