INSTRUCTION_FORMAT = "B"

ASM_NAME = "Result"

def commandExec(param):
    if (param[0] == 1):
        emu.storeWord(10, emu.loadReg(3))
    elif (param[0] == 2):
        emu.storeWord(10, emu.loadReg(3) - 1)
    elif (param[0] == 3):
        emu.storeWord(10, -1)
    emu.incrementProgramCounter(1)
