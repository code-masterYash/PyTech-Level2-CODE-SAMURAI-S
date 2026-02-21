from model import PassFailPredictor

predictor = PassFailPredictor()

while True:
    print("\n===== Pass / Fail Predictor =====")
    print("1. Train Model")
    print("2. Predict Result")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print(" Invalid input! Enter a number.")
        continue

    if choice == 1:
        accuracy = predictor.train_model()
        if accuracy is None:
            print(" Dataset must contain both PASS and FAIL students.")
        else:
            print(f" Model Trained Successfully")
            print(f" Accuracy: {accuracy:.2f}")

    elif choice == 2:
        try:
            math = int(input("Enter Math marks: "))
            science = int(input("Enter Science marks: "))
            english = int(input("Enter English marks: "))

            result = predictor.predict_result(math, science, english)
            print(f" Prediction Result: {result}")

        except ValueError:
            print(" Enter valid numeric marks.")

    elif choice == 3:
        print("Exiting Program")
        break

    else:

        print(" Invalid choice. Select 1–3.")
