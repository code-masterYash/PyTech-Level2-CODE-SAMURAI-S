class PassFailPredictor:
    def __init__(self, filename="data.txt"):
        self.filename = filename
        self.data = []
        self.trained = False

    def load_data(self):
        self.data = []
        with open(self.filename, "r") as file:
            next(file)
            for line in file:
                try:
                    math, science, english = map(int, line.strip().split(","))
                    avg = (math + science + english) / 3
                    result = 1 if avg >= 40 else 0
                    self.data.append(([math, science, english], result))
                except:
                    continue

    def train_model(self):
        self.load_data()
        if len(self.data) == 0:
            return None

        split = int(0.8 * len(self.data))
        train = self.data[:split]
        test = self.data[split:]

        correct = 0
        for features, actual in test:
            avg = sum(features) / 3
            predicted = 1 if avg >= 40 else 0
            if predicted == actual:
                correct += 1

        self.trained = True
        accuracy = correct / len(test) if test else 0
        return accuracy

    def predict_result(self, math, science, english):
        if not self.trained:
            return "Train model first"

        avg = (math + science + english) / 3
        return "PASS" if avg >= 40 else "FAIL"