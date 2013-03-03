INSTRUCTION_FORMAT = "A"

ASM_NAME = "increment"

def commandExec(param):
    if (param[1] == 1):
        emu.storeReg(param[0], emu.loadReg(param[0]) + 1)
    else:
        emu.storeReg(param[0], emu.loadReg(param[0]) - 1)
    emu.incrementProgramCounter(1)
