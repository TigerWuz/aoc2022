class InputReader():
    @staticmethod
    def get(filepath, split = None):
        with open(filepath, "r") as f:
            data = [line.rstrip() for line in f]

        if split:
            result = []
            for elem in data:
                result = result + elem.split(split)
            data = result
        return data

    @staticmethod
    def getInt(filepath):
        data = InputReader.get(filepath)
        return  [int(x) for x in data]

