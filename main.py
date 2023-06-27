import json

from qsdc import qsdc

with open('input.json') as fin:
    input_data = json.load(fin)

    mes = input_data['mes']
    shots = input_data['shots']
    probs = input_data['probs']
    transfer_qubits = input_data['transfer_qubits']

    result, mut_info, qasm_code = qsdc(mes, shots, probs, transfer_qubits)

    print(result, mut_info)

with open('output.json', 'w') as fout:
    json.dump({'result': result, 'mut_info': mut_info}, fout)

with open('superdense_qc.qasm', 'w') as fout2:
    fout2.write(qasm_code)
