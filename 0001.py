INSTRUCTION_FORMAT = "A"

ASM_NAME = "setImmediate"

def commandExec(param):
    emu.storeReg(param[0], param[1])
    emu.incrementProgramCounter(1)
