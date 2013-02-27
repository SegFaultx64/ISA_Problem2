INSTRUCTION_FORMAT = "A"

ASM_NAME = "Result"

def commandExec(param):
    if (param[1] == 1):
        emu.storeWord(10, emu.loadReg(3))
    elif (param[1] == 2):
        emu.storeWord(10, emu.loadReg(3) - 1)
    elif (param[3] == 1):
        emu.storeWord(10 , -1)
    emu.incrementProgramCounter(1)
