// Initialize Reg 3 to 0
ImmediateIntoReg 3 0
// Load the Word from 9 into Reg 4
LoadQuery 0 0
Compare1 0 0
Increment 3 1
IfDone 0 0
IncrementProgramCounter 3
Compare2 0 0
Increment 3 1
IfDone 0 0
IncrementProgramCounter 7
// Success Full Word
Result 0 1
Result 0 0
// Success Half Word
Result 0 2
Result 0 0
// Fail
Result 0 3
Result 0 0