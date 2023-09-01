class KatVM:
    tape: list[str] = [""]
    memory: list[str] = []
    pointer: int = 0

    def left(self, value: str | int):
        val = int(value)
        for _ in range(val):
            if self.pointer == 0:
                self.tape.insert(0, "")
            else:
                self.pointer -= 1

    def right(self, value: str | int):
        val = int(value)
        for _ in range(val):
            if self.pointer == len(self.tape) - 1:
                self.tape.append("")
            self.pointer += 1

    def store(self, string: str):
        for i in range(len(string)):
            self.tape[self.pointer] = string[i]
            self.right(1)
        self.tape[self.pointer] = ""

    def print(self):
        while c := self.tape[self.pointer]:
            print(c, end="", flush=True)
            self.right(1)
        print(flush=True)

    def input(self):
        self.store(input())

    def push(self):
        self.memory.append(self.tape[self.pointer])

    def popeq(self, value: str):
        return self.memory.pop() == value
