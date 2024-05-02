class MacroProcessor:
    def __init__(self):
        self.mdt = {}
        self.mnt = {}
        self.intermediate_code = []

    def first_pass(self, code):
        macro_name = None
        for line in code:
            if line.startswith("MACRO"):
                macro_name = line.split()[1]
                self.mnt[macro_name] = len(self.mdt)
                self.mdt[macro_name] = []
            elif line.startswith("MEND"):
                macro_name = None
            elif macro_name:
                self.mdt[macro_name].append(line)

    def expand_macros(self, code):
        for line in code:
            parts = line.split()
            macro_name = parts[0]
            if macro_name in self.mnt:
                arguments = parts[1:]
                for i, arg in enumerate(arguments):
                    for j, mdt_line in enumerate(self.mdt[macro_name]):
                        arguments[i] = "ARG" + str(i + 1)
                        mdt_line = mdt_line.replace(f"${i + 1}", arguments[i])
                        self.intermediate_code.append(mdt_line)
            else:
                self.intermediate_code.append(line)

    def print_mdt(self):
        print("Macro Definition Table (MDT):")
        for name, lines in self.mdt.items():
            print(f"{name}:")
            for line in lines:
                print(line)

    def print_mnt(self):
        print("\nMacro Name Table (MNT):")
        for name, index in self.mnt.items():
            print(f"{name}\t{index}")

    def print_intermediate_code(self):
        print("\nIntermediate Code:")
        for line in self.intermediate_code:
            print(line)


input_code = [
    "LOAD A",
    "MACRO ABC",
    "LOAD p",
    "SUB q",
    "MEND",
    "STORE B",
    "MULT D",
    "MACRO ADD1 ARG",
    "LOAD X",
    "STORE ARG",
    "MEND",
    "LOAD B",
    "MACRO ADD5 A1, A2, A3",
    "STORE A2",
    "ADD1 5",
    "ADD1 10",
    "LOAD A1",
    "LOAD A3",
    "MEND",
    "ADD1 t",
    "ABC",
    "ADD5 D1, D2, D3",
    "END"
]

processor = MacroProcessor()
processor.first_pass(input_code)
processor.expand_macros(input_code)

processor.print_mnt()
processor.print_mdt()
processor.print_intermediate_code()
