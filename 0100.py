INSTRUCTION_FORMAT = "A"

ASM_NAME = "Compare2"

def commandExec(param):
    curWord = emu.loadWord(96 + emu.loadReg(3))
    emu.storeReg(5, curWord)
    emu.incrementProgramCounter(1)
    binaryQuery = "{0:b}".format(emu.loadReg(4)).zfill(16)
    binaryCurWord = "{0:b}".format(emu.loadReg(5)).zfill(16)
    if (binaryQuery[-8:] == binaryCurWord[8:]):
        emu.incrementProgramCounter(6)
    elif (emu.loadReg(4) == emu.loadReg(5)):
        emu.incrementProgramCounter(4)
    elif (binaryQuery[8:] == binaryCurWord[-8:]):
        emu.incrementProgramCounter(-1)
    emu.incrementProgramCounter(1)
