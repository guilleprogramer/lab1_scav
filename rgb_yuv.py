def rgb_to_yuv(R, G, B):
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    U = -0.14713 * R - 0.28886 * G + 0.436 * B
    V = 0.615 * R - 0.51499 * G - 0.10001 * B
    return Y, U, V

rgb_to_yuv(10, 20, 30)
