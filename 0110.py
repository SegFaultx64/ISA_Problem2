INSTRUCTION_FORMAT = "B"

ASM_NAME = "ifDone"

def commandExec(param):
    if (emu.loadReg(3) >= 144):
        emu.setProgramCounter(11)
    emu.incrementProgramCounter(1)