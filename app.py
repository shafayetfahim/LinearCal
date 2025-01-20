from flask import Flask, request, jsonify
import calculator_service
app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Expects JSON in the format:
    {
        "operation": "add" | "subtract" | "multiply" | "divide" | "exponent",
        "a": <number>,
        "b": <number>
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    operation = data.get('operation')
    a = data.get('a')
    b = data.get('b')

    # Basic validation
    if operation not in ['add', 'subtract', 'multiply', 'divide', 'exponent']:
        return jsonify({"error": f"Operation '{operation}' not supported"}), 400

    if a is None or b is None:
        return jsonify({"error": "Operands 'a' and 'b' are required"}), 400

    try:
        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)
        elif operation == 'exponent':
            result = exponent(a, b)
        else:
            # Should not happen given validation above
            return jsonify({"error": f"Operation '{operation}' not supported"}), 400

        return jsonify({"result": result}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    # When running locally, Flask uses this entry point
    app.run(debug=True)
