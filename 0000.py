INSTRUCTION_FORMAT = "B"

ASM_NAME = "result"

def commandExec(param):
    emu.storeWord(10, emu.loadReg(15))
    if (param[0] == 1):
        emu.storeReg(15, emu.loadReg(3))
    elif (param[0] == 2):
        emu.storeReg(15, emu.loadReg(3) - 1)
    elif (param[0] == 3):
        emu.storeReg(15, -1)
    elif (param[0] == 4):
        emu.incrementProgramCounter(200)
    emu.incrementProgramCounter(1)
