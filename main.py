import json

from qsdc import qsdc

with open('input.json') as fin:
    # Открытие файла с входными данными в формате json
    input_data = json.load(fin)

    # Чтение входных данных
    mes = input_data['mes']
    shots = input_data['shots']
    probs = input_data['probs']
    transfer_qubits = input_data['transfer_qubits']
    qasm_circs_name_prefix = input_data['qasm_circs_name_prefix']

    # Подсчёт взаимной информации и генерация кода на QASM с помощью основной функции алгоритма
    result, mut_info = qsdc(mes, shots, probs, transfer_qubits,
                                       qasm_circs_name_prefix)

    print(result, mut_info)

# Запись выходных данных в формате json
with open('output.json', 'w') as fout:
    json.dump({'result': result, 'mut_info': mut_info}, fout)