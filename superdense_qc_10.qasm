OPENQASM 2.0;
include "qelib1.inc";
qreg q43[1];
qreg q44[3];
qreg q45[2];
creg c2[2];
u2(0,pi) q45[0];
cx q45[0],q45[1];
barrier q43[0],q44[0],q44[1],q44[2],q45[0],q45[1];
cx q45[0],q44[2];
cx q44[2],q45[0];
cx q45[0],q44[2];
cx q44[2],q44[1];
cx q44[1],q44[2];
cx q44[2],q44[1];
cx q44[1],q44[0];
cx q44[0],q44[1];
cx q44[1],q44[0];
cx q44[0],q43[0];
cx q43[0],q44[0];
cx q44[0],q43[0];
u3(pi,0,pi) q43[0];
cx q43[0],q44[0];
cx q44[0],q43[0];
cx q43[0],q44[0];
cx q44[0],q44[1];
cx q44[1],q44[0];
cx q44[0],q44[1];
cx q44[1],q44[2];
cx q44[2],q44[1];
cx q44[1],q44[2];
cx q44[2],q45[0];
cx q45[0],q44[2];
cx q44[2],q45[0];
barrier q43[0],q44[0],q44[1],q44[2],q45[0],q45[1];
cx q45[0],q45[1];
u2(0,pi) q45[0];
barrier q43[0],q44[0],q44[1],q44[2],q45[0],q45[1];
measure q45[0] -> c2[0];
measure q45[1] -> c2[1];
