import numpy as np


def mutual_information(counts_matrix):
    """
    :param counts_matrix: Матрица 4 на 4, содержащая результаты полученных Бобом сообщений, в зависимости от изначально передаваемого Алисой
    :returns: mutual_information: взаимная информация
    """

    pxy = counts_matrix / np.sum(counts_matrix)
    px = np.sum(pxy, axis=1)
    py = np.sum(pxy, axis=0)
    px_py = px[:, None] * py[None, :]  # Broadcast to multiply marginals

    # Only non-zero pxy values contribute to the sum
    nonzeros = pxy > 0

    return np.sum(pxy[nonzeros] * np.log2(pxy[nonzeros] / px_py[nonzeros]))
