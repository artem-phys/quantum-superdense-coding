import json

from qsdc import qsdc

with open('input.json') as fin:
    input_data = json.load(fin)

    mes = input_data['mes']
    shots = input_data['shots']
    probs = input_data['probs']

    result, mut_info = qsdc(mes, shots, probs)

    print(result, mut_info)

with open('output.json', 'w') as fout:
    json.dump({'result': result, 'mut_info': mut_info}, fout)
