from rasa.nlu.model import Interpreter

def load_interpreter(model_path):
    return Interpreter.load(model_path)

def parse_message(interpreter, message):
    result = interpreter.parse(message)
    return result

def get_top_intents(parsed_result, top_n=5):
    # Sort the intents by confidence and get the top N intents
    sorted_intents = sorted(parsed_result['intent_ranking'], key=lambda x: x['confidence'], reverse=True)
    return sorted_intents[:top_n]

if __name__ == "__main__":
    model_path = "models/nlu"  # Adjust this path to your actual model location
    interpreter = load_interpreter(model_path)

    message = input("Enter a message: ")
    result = parse_message(interpreter, message)

    top_intents = get_top_intents(result, top_n=5)

    print(f"Message: {message}")
    print("Top Intents and their Confidence Scores:")
    for intent in top_intents:
        print(f"Intent: {intent['name']}, Confidence: {intent['confidence']}")
    print("Entities:", result.get('entities', []))
