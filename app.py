from flask import Flask, request, jsonify
from rasa.nlu.model import Interpreter

app = Flask(__name__)

# Load the Rasa model
model_path = "models/nlu"  # Adjust this path to your actual model location
interpreter = Interpreter.load(model_path)

def parse_message(message):
    result = interpreter.parse(message)
    return result

def get_top_intents(parsed_result, top_n=5):
    # Sort the intents by confidence and get the top N intents
    sorted_intents = sorted(parsed_result['intent_ranking'], key=lambda x: x['confidence'], reverse=True)
    # Format the confidence to 2 decimal places and exclude IDs
    top_intents = [
        {"name": intent["name"], "confidence": round(intent["confidence"], 2)}
        for intent in sorted_intents[:top_n]
    ]
    return top_intents

@app.route('/parse', methods=['GET'])
def parse():
    text = request.args.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = parse_message(text)
    top_intents = get_top_intents(result, top_n=5)

    response = {
        "text": text,
        "intents": top_intents,
        "entities": result.get('entities', [])
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
