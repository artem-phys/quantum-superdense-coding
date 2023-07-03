import json
import numpy as np

# Чтение входных данных
with open('input.json') as fin:
    input_data = json.load(fin)

    mes = input_data['mes']
    shots = input_data['shots']
    probs = input_data['probs']
    transfer_qubits = input_data['transfer_qubits']

# Чтение выходных данных
with open('output.json') as fout:
    output_data = json.load(fout)
    mut_info = output_data['mut_info']

    print(f'mutual_info: {mut_info}')

    # Верификация того, что метрика попала в требуемый диапазон
    if mut_info > 1:
        print('Verification result: PASS')
    else:
        print('Verification result: FAIL')
