OPENQASM 2.0;
include "qelib1.inc";
qreg q66[1];
qreg q67[3];
qreg q68[2];
creg c3[2];
u2(0,pi) q68[0];
cx q68[0],q68[1];
barrier q66[0],q67[0],q67[1],q67[2],q68[0],q68[1];
cx q68[0],q67[2];
cx q67[2],q68[0];
cx q68[0],q67[2];
cx q67[2],q67[1];
cx q67[1],q67[2];
cx q67[2],q67[1];
cx q67[1],q67[0];
cx q67[0],q67[1];
cx q67[1],q67[0];
cx q67[0],q66[0];
cx q66[0],q67[0];
cx q67[0],q66[0];
u3(pi,0,pi) q66[0];
u1(pi) q66[0];
cx q66[0],q67[0];
cx q67[0],q66[0];
cx q66[0],q67[0];
cx q67[0],q67[1];
cx q67[1],q67[0];
cx q67[0],q67[1];
cx q67[1],q67[2];
cx q67[2],q67[1];
cx q67[1],q67[2];
cx q67[2],q68[0];
cx q68[0],q67[2];
cx q67[2],q68[0];
barrier q66[0],q67[0],q67[1],q67[2],q68[0],q68[1];
cx q68[0],q68[1];
u2(0,pi) q68[0];
barrier q66[0],q67[0],q67[1],q67[2],q68[0],q68[1];
measure q68[0] -> c3[0];
measure q68[1] -> c3[1];
