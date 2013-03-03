// Initialize Reg 3 to 0
init 0
// Load the Word from 9 into Reg 4
init 1
compare 0
increment 3 1
ifDone 0
increment 3 1
compare 1
increment 3 1
ifDone 0
// Success Full Word
result 1
result 4
// Success Half Word
result 2
result 4
// Fail
result 3
result 4
