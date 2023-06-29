import random
import numpy as np

from qiskit import QuantumCircuit, Aer, transpile, QuantumRegister, ClassicalRegister

from mutual_information import mutual_information


def superdense_coding_qc(message, transfer_qubits=0):
    alice_reg = QuantumRegister(1)

    transfer_reg = QuantumRegister(transfer_qubits)

    both_reg = QuantumRegister(2)

    cl_reg = ClassicalRegister(2)

    qc = QuantumCircuit(alice_reg, transfer_reg, both_reg, cl_reg)

    # Bell pair creation
    qc.h(both_reg[0])
    qc.cx(both_reg[0], both_reg[1])

    qc.barrier()

    transfer_qs = [transfer_reg[i] for i in range(transfer_qubits - 1, -1, -1)]

    qubits_to_do_swaps = [both_reg[0], *transfer_qs, alice_reg[0]]

    for i in range(len(qubits_to_do_swaps) - 1):
        qc.swap(qubits_to_do_swaps[i], qubits_to_do_swaps[i + 1])

    # Encoding
    if message[0] == "1":
        qc.x(alice_reg[0])
    if message[1] == "1":
        qc.z(alice_reg[0])

    for i in range(len(qubits_to_do_swaps) - 1, 0, -1):
        qc.swap(qubits_to_do_swaps[i], qubits_to_do_swaps[i - 1])

    qc.barrier()

    # Bell measurement:
    qc.cx(both_reg[0], both_reg[1])
    qc.h(both_reg[0])
    qc.barrier()
    qc.measure(both_reg[0], cl_reg[0])
    qc.measure(both_reg[1], cl_reg[1])

    return qc


def qsdc(mes, shots, probs, transfer_qubits, qasm_circs_name_prefix):

    backend = Aer.get_backend('aer_simulator')
    messages_to_sent = random.choices(mes, weights=probs, k=shots)

    possible_messages = ['00', '01', '10', '11']

    result = {message: dict(zip(possible_messages, [0] * len(possible_messages))) for message in possible_messages}

    for message in possible_messages:
        num_of_messages = messages_to_sent.count(message)
        qc = superdense_coding_qc(message, transfer_qubits)
        job = backend.run(transpile(qc, backend), shots=num_of_messages)
        counts = job.result().get_counts()
        for outcome in counts:
            result[message][outcome] += counts[outcome]

        if qasm_circs_name_prefix is not None:
            qasm_code = qc.decompose().qasm()
            qasm_fname = qasm_circs_name_prefix + message + ".qasm"
            with open(qasm_fname, 'w') as fout2:
                fout2.write(qasm_code)

    counts_matrix = np.array([[count for count in message_results.values()] for message_results in result.values()])

    mut_info = mutual_information(counts_matrix)

    

    return result, mut_info
