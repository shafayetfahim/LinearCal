import traceback

from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "Flask backend is running!"


# Route for matrix addition
@app.route('/add', methods=['POST'])
def add_matrices():
    try:
        data = request.get_json()
        matrix1 = np.array(data['matrix1'])
        matrix2 = np.array(data['matrix2'])

        if matrix1.shape != matrix2.shape:
            return jsonify({"error": "Matrices must have the same dimensions!"}), 400

        result = matrix1 + matrix2
        return jsonify({"result": result.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route for matrix subtraction
@app.route('/subtract', methods=['POST'])
def subtract_matrices():
    try:
        data = request.get_json()
        matrix1 = np.array(data['matrix1'])
        matrix2 = np.array(data['matrix2'])

        if matrix1.shape != matrix2.shape:
            return jsonify({"error": "Matrices must have the same dimensions!"}), 400

        result = matrix1 - matrix2
        return jsonify({"result": result.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling
@app.errorhandler(Exception)
def handle_exception(e):
    # Return a JSON response for any unhandled exceptions
    return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500


# Route for matrix multiplication
@app.route('/multiply', methods=['POST'])
def multiply_matrices():
    try:
        data = request.get_json()
        matrix1 = np.array(data['matrix1'])
        matrix2 = np.array(data['matrix2'])

        if matrix1.shape[1] != matrix2.shape[0]:
            return jsonify({"error": "Number of columns in Matrix 1 must equal the number of rows in Matrix 2!"}), 400

        result = np.dot(matrix1, matrix2)
        return jsonify({"result": result.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route for RREF (Reduced Row Echelon Form)
@app.route('/rref', methods=['POST'])
def rref_matrix():
    try:
        data = request.get_json()
        matrix = np.array(data['matrix'])

        # RREF calculation
        mat = matrix.astype(float)
        rows, cols = mat.shape
        for i in range(min(rows, cols)):
            # Make the pivot 1
            if mat[i, i] != 0:
                mat[i] = mat[i] / mat[i, i]
            for j in range(rows):
                if j != i:
                    mat[j] = mat[j] - mat[j, i] * mat[i]

        return jsonify({"result": mat.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
