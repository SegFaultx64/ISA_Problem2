INSTRUCTION_FORMAT = "A"

ASM_NAME = "Compare1"

def commandExec(param):
    curOffset = emu.loadReg(3)
    curWord = emu.loadWord(96 + curOffset)
    emu.storeReg(5, curWord)
    emu.incrementProgramCounter(1)
    reg4 = emu.loadReg(4)
    reg5 = emu.loadReg(5)
    binaryQuery = bin(reg4)[2:0]
    binaryQuery = binaryQuery.zfill(16)
    binaryCurWord = bin(reg5)[2:0]
    binaryCurWord = CurWord.zfill(16)
    if (emu.loadReg(4) == emu.loadReg(5)):
        emu.setProgramCounter(10)
    elif (binaryQuery[8:] == binaryCurWord[-8:]):
        emu.setProgramCounter(6)
    emu.incrementProgramCounter(1)
