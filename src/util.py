import matplotlib.image as im
import numpy as np


def img_to_matrix(nome_file: str) -> np.array:
    return im.imread(nome_file)


def img_rgb_to_cinza(matrix_img_rgb: np.array) -> np.array:

    matrix_cinza = np.zeros(matrix_img_rgb[:, :, 0].shape, dtype=int)

    for i in range(matrix_cinza.shape[0]):
        for j in range(matrix_cinza.shape[1]):
            matrix_cinza[i, j] = int((int(matrix_img_rgb[i, j, 0]) +
                                      int(matrix_img_rgb[i, j, 1]) +
                                      int(matrix_img_rgb[i, j, 2])) / 3.0)


    matrix_gray_rgb = np.zeros(matrix_img_rgb.shape, dtype=int)

    for i in range(matrix_cinza.shape[0]):
        for j in range(matrix_cinza.shape[1]):
            matrix_gray_rgb[i, j, 0] = matrix_cinza[i, j]
            matrix_gray_rgb[i, j, 1] = matrix_cinza[i, j]
            matrix_gray_rgb[i, j, 2] = matrix_cinza[i, j]

    return matrix_gray_rgb


def img_rgb_to_cinza_1_canal(matrix_img_rgb: np.array) -> np.array:

    matrix_cinza = np.zeros(matrix_img_rgb[:, :, 0].shape, dtype=int)

    for i in range(matrix_cinza.shape[0]):
        for j in range(matrix_cinza.shape[1]):
            matrix_cinza[i, j] = int((int(matrix_img_rgb[i, j, 0]) +
                                      int(matrix_img_rgb[i, j, 1]) +
                                      int(matrix_img_rgb[i, j, 2])) / 3.0)

    return matrix_cinza



def img_1_canal_to_3_canais(matrix_img_1_canal: np.array) -> np.array:

    matrix_cinza_3_canais = np.zeros(tuple(list(matrix_img_1_canal.shape) + [3]), dtype=int)

    for i in range(matrix_cinza_3_canais.shape[0]):
        for j in range(matrix_cinza_3_canais.shape[1]):
            matrix_cinza_3_canais[i, j, 0] = matrix_img_1_canal[i, j]
            matrix_cinza_3_canais[i, j, 1] = matrix_img_1_canal[i, j]
            matrix_cinza_3_canais[i, j, 2] = matrix_img_1_canal[i, j]

    return matrix_cinza_3_canais


def calc_histograma(matrix_cinza: np.array) -> np.array:
    histograma = np.zeros(256, dtype=int)
    for i in range(matrix_cinza.shape[0]):
        for j in range(matrix_cinza.shape[1]):
            histograma[int(matrix_cinza[i, j, 0])] = histograma[int(matrix_cinza[i, j, 0])] + 1.0
    return histograma

