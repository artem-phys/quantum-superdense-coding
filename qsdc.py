import random
import numpy as np

from qiskit import IBMQ, QuantumCircuit, Aer, transpile, QuantumRegister, ClassicalRegister

from mutual_information import mutual_information


def superdense_coding_qc(message):
    alice_reg = QuantumRegister(1, name='Alice')
    both_reg = QuantumRegister(2, name='Bob')

    cl_reg = ClassicalRegister(2, name='classical_bits')

    qc = QuantumCircuit(alice_reg, both_reg, cl_reg)

    # Bell pair creation
    qc.h(both_reg[0])
    qc.cx(both_reg[0], both_reg[1])

    qc.barrier()

    qc.swap(alice_reg[0], both_reg[0])

    # Encoding
    if message[0] == "1":
        qc.x(alice_reg[0])
    if message[1] == "1":
        qc.z(alice_reg[0])

    qc.swap(alice_reg[0], both_reg[0])

    qc.barrier()

    # Bell measurement:
    qc.cx(both_reg[0], both_reg[1])
    qc.h(both_reg[0])
    qc.barrier()
    qc.measure(both_reg[0], cl_reg[0])
    qc.measure(both_reg[1], cl_reg[1])

    # print(qc.decompose().qasm())

    return qc


def qsdc(mes, shots, probs):


    backend = Aer.get_backend('aer_simulator')
    messages_to_sent = random.choices(mes, weights=probs, k=shots)

    possible_messages = ['00','01', '10', '11']

    result = {message: dict(zip(possible_messages, [0] * len(possible_messages))) for message in possible_messages}

    for message in messages_to_sent:
        qc = superdense_coding_qc(message)
        job = backend.run(transpile(qc, backend), shots=1)
        count = next(iter(job.result().get_counts()))
        result[message][count] = result[message].get(count, 0) + 1

    counts_matrix = np.array([[count for count in message_results.values()] for message_results in result.values()])

    mut_info = mutual_information(counts_matrix)

    return result, mut_info

