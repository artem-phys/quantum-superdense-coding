import itertools

from qsdc import qsdc

mes_qubits_list = [["00", "01", "10", "11"]]
shots_list = [1024]
probs_list = [[0.25, 0.25, 0.25, 0.25]]
transfer_qubits_list = list(range(4))
qasm_circs_name_prefix_list = ["superdense_qc_"]

parameters_lists = [
    mes_qubits_list,
    shots_list,
    probs_list,
    transfer_qubits_list,
    qasm_circs_name_prefix_list,
]

# Добавляем тесты
tests = [parameter_set for parameter_set in itertools.product(*parameters_lists)]

for test_entry in tests:

    # Параметры запуска
    mes, shots, probs, transfer_qubits, qasm_circs_name_prefix = test_entry

    print(f"""Взаимная информация для запуска алгоритма при количестве трансферных кубитов {test_entry[3]} """)

    # Требования к показателю
    print('Требования к показателю: >1')

    # Измеренное значение
    result, mut_info = qsdc(mes, shots, probs, transfer_qubits,
                        qasm_circs_name_prefix)
    print(f'Измеренное значение: {mut_info}')
    print()