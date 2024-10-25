#!/usr/bin/env python3
"""Convolves images using multiple kernels"""

import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Convolves images using multiple kernels
    Args:
        images: `numpy.ndarray` (m, h, w, c) - images to convolve
        kernels: `numpy.ndarray` (kh, kw, c, nc) - convolution kernels
        padding: `tuple`, 'same', or 'valid'
        stride: `tuple` (sh, sw) - stride of convolution
    Returns:
        `numpy.ndarray` with convolved images
    """
    m, h, w = images.shape[0], images.shape[1], images.shape[2]
    kh, kw, nc = kernels.shape[0], kernels.shape[1], kernels.shape[3]
    sh, sw = stride[0], stride[1]
    if padding == 'same':
        pw = int(((w - 1) * sw + kw - w) / 2) + 1
        ph = int(((h - 1) * sh + kh - h) / 2) + 1
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        pw, ph = padding[1], padding[0]
    nw, nh = int(((w - kw + 2 * pw) / sw) + 1), int(((h - kh + 2 * ph) / sh) + 1)
    convolved = np.zeros((m, nh, nw, nc))
    imagesp = np.pad(images, pad_width=((0, 0), (ph, ph), (pw, pw), (0, 0)),
                     mode='constant', constant_values=0)
    for i in range(nh):
        x = i * sh
        for j in range(nw):
            y = j * sw
            for k in range(nc):
                image = imagesp[:, x:x + kh, y:y + kw, :]
                kernel = kernels[:, :, :, k]
                convolved[:, i, j, k] = np.sum(np.multiply(image, kernel),
                                               axis=(1, 2, 3))
    return convolved
