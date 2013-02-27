INSTRUCTION_FORMAT = "A"

ASM_NAME = "IfDone"

def commandExec(param):
    if (emu.loadReg(3) >= 48):
        emu.setProgramCounter(14)
    else:
        emu.incrementProgramCounter(1)
