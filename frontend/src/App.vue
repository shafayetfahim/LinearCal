<script>
import axios from "axios";

export default {
  data() {
    return {
      rows: 2,
      cols: 2,
      matrix1: [],
      matrix2: [],
      result: null,
      error: null,
      selectedOperation: "add", // Default operation
    };
  },
  methods: {
    initializeMatrices() {
      this.matrix1 = Array.from({ length: this.rows }, () =>
        Array(this.cols).fill("")
      );
      if (["add", "subtract", "multiply"].includes(this.selectedOperation)) {
        this.matrix2 = Array.from({ length: this.rows }, () =>
          Array(this.cols).fill("")
        );
      } else {
        this.matrix2 = [];
      }
    },
    performOperation() {
      let endpoint = `http://127.0.0.1:5000/${this.selectedOperation}`;
      let payload =
        ["add", "subtract", "multiply"].includes(this.selectedOperation)
          ? { matrix1: this.matrix1, matrix2: this.matrix2 }
          : { matrix: this.matrix1 };

      axios
        .post(endpoint, payload)
        .then((response) => {
          this.result = response.data.result;
          this.error = null;
        })
        .catch((error) => {
          console.error("Error:", error.response?.data || error.message);
          this.error = error.response?.data?.error || "An error occurred.";
        });
    },
    handleOperationChange() {
      this.result = null;
      this.error = null;
      this.initializeMatrices();
    },
  },
  mounted() {
    this.initializeMatrices();
  },
};
</script>

<template>
  <div class="full-container">
    <header class="header">
      <h1>Matrix Calculator</h1>
      <p>Effortlessly perform advanced matrix operations</p>
    </header>
    <div class="controls">
      <label>Rows:</label>
      <input type="number" v-model="rows" @change="initializeMatrices" min="1" />
      <label>Columns:</label>
      <input type="number" v-model="cols" @change="initializeMatrices" min="1" />
      <label>Operation:</label>
      <select v-model="selectedOperation" @change="handleOperationChange">
        <option value="add">Add</option>
        <option value="subtract">Subtract</option>
        <option value="multiply">Multiply</option>
        <option value="rref">RREF</option>
        <option value="inverse">Inverse</option>
        <option value="rank">Rank</option>
        <option value="nullity">Nullity</option>
      </select>
    </div>

    <h2>Matrix 1</h2>
    <table class="matrix">
      <tr v-for="(row, rowIndex) in matrix1" :key="rowIndex">
        <td v-for="(value, colIndex) in row" :key="colIndex">
          <input type="number" v-model="matrix1[rowIndex][colIndex]" class="no-arrows" />
        </td>
      </tr>
    </table>

    <h2 v-if="['add', 'subtract', 'multiply'].includes(selectedOperation)">Matrix 2</h2>
    <table class="matrix" v-if="['add', 'subtract', 'multiply'].includes(selectedOperation)">
      <tr v-for="(row, rowIndex) in matrix2" :key="rowIndex">
        <td v-for="(value, colIndex) in row" :key="colIndex">
          <input type="number" v-model="matrix2[rowIndex][colIndex]" class="no-arrows" />
        </td>
      </tr>
    </table>

    <button class="action-btn" @click="performOperation">Run Operation</button>

    <div v-if="result" class="result">
      <h2>Result:</h2>
      <table class="matrix" v-if="Array.isArray(result)">
        <tr v-for="(row, rowIndex) in result" :key="rowIndex">
          <td v-for="(value, colIndex) in row" :key="colIndex">{{ value }}</td>
        </tr>
      </table>
      <p v-if="!Array.isArray(result)">{{ result }}</p>
    </div>

    <div v-if="error" class="error">
      <p>Error: {{ error }}</p>
    </div>
  </div>
</template>

<style>
body {
  font-family: "Helvetica",sans-serif;
  text-align: center;
  background-color: #f4f4f4;
  color: #2c3e50;
  margin: 0;
  padding: 0;
}

.full-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: white;
}

.header {
  background: #0c2340;
  color: white;
  padding: 20px;
  text-align: center;
  width: 100%;
}

.controls {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-bottom: 20px;
  margin-top: 20px;
}

.matrix {
  margin: 10px auto;
  border-collapse: collapse;
}

.matrix td {
  padding: 10px;
  border: 1px solid #ddd;
}

.matrix input {
  width: 50px;
  padding: 5px;
  text-align: center;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.no-arrows::-webkit-outer-spin-button,
.no-arrows::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.no-arrows {
  -moz-appearance: textfield;
}

.action-btn {
  background: #0c2340;
  color: white;
  border: none;
  padding: 12px 25px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s;
  margin-top: 20px;
}

.action-btn:hover {
  background: #1d4f91;
}

.result {
  margin-top: 20px;
  padding: 10px;
  background: #e3fcef;
  border-radius: 5px;
}

.error {
  color: red;
  margin-top: 10px;
}
</style>