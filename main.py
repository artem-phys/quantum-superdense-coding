import json

from qsdc import qsdc

with open('input.json') as fin:
    input_data = json.load(fin)

    mes = input_data['mes']
    shots = input_data['shots']
    probs = input_data['probs']
    transfer_qubits = input_data['transfer_qubits']
    qasm_circs_name_prefix = input_data['qasm_circs_name_prefix']

    result, mut_info = qsdc(mes, shots, probs, transfer_qubits,
                                       qasm_circs_name_prefix)

    print(result, mut_info)

with open('output.json', 'w') as fout:
    json.dump({'result': result, 'mut_info': mut_info}, fout)