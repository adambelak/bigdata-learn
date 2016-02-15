import sys


class Mapper:
    def __init__(self):
        self.ones = [1] * 5
        pass

    def getNumbers(self, csv_line=''):
        try:
            numbers = csv_line.strip().split(';')[-5:]
            return zip(map(int, numbers), self.ones)
        except ValueError:
            return []

    def processInput(self, lines, out):
        for line in lines:
            for number in self.getNumbers(line):
                out.write(str(number[0]))
                out.write('\t')
                out.write(str(number[1]))
                out.write('\n')
            out.flush()


def main(argv):
    Mapper().processInput(argv[0] if len(argv) > 2 else sys.stdin, argv[1] if len(argv) > 2 else sys.stdout)


if __name__ == "__main__":
    main(sys.argv)
