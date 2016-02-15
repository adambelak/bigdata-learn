import sys


class Reducer:
    def __init__(self):
        self.actual_number = None
        self.counter = 0

    def getNumber(self, line):
        try:
            return int(line.strip().split('\t')[0])
        except Exception:
            return 0

    def initNumber(self, number):
        self.actual_number = number
        self.counter = 1

    def isActual(self, number):
        return self.actual_number == number

    def isFirst(self):
        return self.actual_number is None

    def isZero(self, number):
        return number == 0

    def increment(self):
        self.counter += 1

    def printResult(self, out):
        out.write(str(self.actual_number))
        out.write('\t')
        out.write(str(self.counter))
        out.write('\n')
        out.flush()

    def processInput(self, lines, out):
        for line in lines:
            number = self.getNumber(line)
            if not self.isZero(number):
                if self.isActual(number):
                    self.increment()
                else:
                    if not self.isFirst():
                        self.printResult(out)
                    self.initNumber(number)
        self.printResult(out)


def main(argv):
    Reducer().processInput(argv[0] if len(argv) > 2 else sys.stdin, argv[1] if len(argv) > 2 else sys.stdout)


if __name__ == "__main__":
    main(sys.argv)
