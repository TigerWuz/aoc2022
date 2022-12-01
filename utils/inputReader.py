class InputReader():
    @staticmethod
    def get(filepath):
        with open(filepath, "r") as f:
            data = [line.rstrip() for line in f]
        return data

    @staticmethod
    def getInt(filepath):
        data = InputReader.get(filepath)
        return  [int(x) for x in data]
