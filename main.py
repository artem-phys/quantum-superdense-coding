import json

from qsdc import qsdc

with open('input.json') as fin:
    input_data = json.load(fin)

    mes = input_data['mes']
    shots = input_data['shots']
    probs = input_data['probs']

    result = qsdc(mes, shots, probs)

    print(result)

with open('output.json', 'w') as fout:
    json.dump({'result': result}, fout)
