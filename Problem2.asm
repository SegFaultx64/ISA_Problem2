// Initialize Reg 3 to 0
jumpBackOrInit 0
// Load the Word from 9 into Reg 4
loadQuery 9
increment 3 1
ifDone 0
compare 0
increment 3 1
ifDone 0
compare 1
// Success Full Word
result 1
result 4
// Success Half Word
result 2
result 4
// Fail
result 3
result 4