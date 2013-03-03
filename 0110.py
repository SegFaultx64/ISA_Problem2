INSTRUCTION_FORMAT = "A"

ASM_NAME = "ifDone"

def commandExec(param):
    if (emu.loadReg(3) >= 48):
        emu.setProgramCounter(15)
    else:
        emu.setProgramCounter(3)
