import matplotlib.image as im
import numpy as np

from util import img_rgb_to_cinza_1_canal, img_1_canal_to_3_canais


def blur(matrix_cinza: np.array) -> np.array:
    matriz_cinza_1_canal = img_rgb_to_cinza_1_canal(matrix_cinza)
    matriz_resultado = np.zeros(matriz_cinza_1_canal.shape, dtype=int)

    for l in range(matriz_cinza_1_canal.shape[0]):
        for c in range(matriz_cinza_1_canal.shape[1]):
            if l == 0 or c == 0 or l == matriz_cinza_1_canal.shape[0] - 1 or c == matriz_cinza_1_canal.shape[1] - 1:
                continue
            matriz_resultado[l, c] = matriz_cinza_1_canal[l - 1, c - 1] + \
                                     matriz_cinza_1_canal[l - 1, c] + \
                                     matriz_cinza_1_canal[l - 1, c + 1] + \
                                     matriz_cinza_1_canal[l, c - 1] + \
                                     matriz_cinza_1_canal[l, c] + \
                                     matriz_cinza_1_canal[l, c + 1] + \
                                     matriz_cinza_1_canal[l + 1, c - 1] + \
                                     matriz_cinza_1_canal[l + 1, c] + \
                                     matriz_cinza_1_canal[l + 1, c + 1]
            matriz_resultado[l, c] = matriz_resultado[l, c] / 9
    matriz_cinza_3_canais = img_1_canal_to_3_canais(matriz_resultado)

    return matriz_cinza_3_canais


def mascara_3_por_3(matrix_cinza: np.array, mascara: np.array, fator_divisao: float) -> np.array:
    matriz_cinza_1_canal = img_rgb_to_cinza_1_canal(matrix_cinza)
    matriz_resultado = np.zeros(matriz_cinza_1_canal.shape, dtype=int)

    for l in range(matriz_cinza_1_canal.shape[0]):
        for c in range(matriz_cinza_1_canal.shape[1]):
            if l == 0 or c == 0 or l == matriz_cinza_1_canal.shape[0] - 1 or c == matriz_cinza_1_canal.shape[1] - 1:
                continue
            matriz_resultado[l, c] = matriz_cinza_1_canal[l - 1, c - 1] * mascara[0, 0] + \
                                     matriz_cinza_1_canal[l - 1, c    ] * mascara[0, 1] + \
                                     matriz_cinza_1_canal[l - 1, c + 1] * mascara[0, 2] + \
                                     matriz_cinza_1_canal[l    , c - 1] * mascara[1, 0] + \
                                     matriz_cinza_1_canal[l    , c    ] * mascara[1, 1] + \
                                     matriz_cinza_1_canal[l    , c + 1] * mascara[1, 2] + \
                                     matriz_cinza_1_canal[l + 1, c - 1] * mascara[2, 0] + \
                                     matriz_cinza_1_canal[l + 1, c    ] * mascara[2, 1] + \
                                     matriz_cinza_1_canal[l + 1, c + 1] * mascara[2, 2]
            matriz_resultado[l, c] = max(0, matriz_resultado[l, c])
            matriz_resultado[l, c] = min(255, matriz_resultado[l, c])
            matriz_resultado[l, c] = matriz_resultado[l, c] / fator_divisao
    matriz_cinza_3_canais = img_1_canal_to_3_canais(matriz_resultado)

    return matriz_cinza_3_canais
