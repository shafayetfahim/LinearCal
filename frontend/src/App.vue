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
    };
  },
  methods: {
    initializeMatrices() {
      // Initialize two empty matrices
      this.matrix1 = Array.from({ length: this.rows }, () =>
        Array(this.cols).fill("")
      );
      this.matrix2 = Array.from({ length: this.rows }, () =>
        Array(this.cols).fill("")
      );
    },
    submitMatrices() {
      // Send matrices to Flask for addition
      axios
        .post("http://127.0.0.1:5000/add", {
          matrix1: this.matrix1,
          matrix2: this.matrix2,
        })
        .then((response) => {
          this.result = response.data.result; // Store the result
          this.error = null;
        })
        .catch((error) => {
          console.error("Error:", error.response?.data || error.message);
          this.error = error.response?.data?.error || "An error occurred.";
        });
    },
  },
  mounted() {
    this.initializeMatrices();
  },
};
</script>

<template>
  <div>
    <h1>Matrix Addition</h1>
    <div>
      <label>Rows:</label>
      <input type="number" v-model="rows" @change="initializeMatrices" min="1" />
      <label>Columns:</label>
      <input type="number" v-model="cols" @change="initializeMatrices" min="1" />
    </div>

    <h2>Matrix 1</h2>
    <table border="1">
      <tr v-for="(row, rowIndex) in matrix1" :key="rowIndex">
        <td v-for="(value, colIndex) in row" :key="colIndex">
          <input
            type="number"
            v-model="matrix1[rowIndex][colIndex]"
            style="width: 50px;"
          />
        </td>
      </tr>
    </table>

    <h2>Matrix 2</h2>
    <table border="1">
      <tr v-for="(row, rowIndex) in matrix2" :key="rowIndex">
        <td v-for="(value, colIndex) in row" :key="colIndex">
          <input
            type="number"
            v-model="matrix2[rowIndex][colIndex]"
            style="width: 50px;"
          />
        </td>
      </tr>
    </table>

    <button @click="submitMatrices" style="margin-top: 20px;">
      Add Matrices
    </button>

    <div v-if="result">
      <h2>Result:</h2>
      <table border="1">
        <tr v-for="(row, rowIndex) in result" :key="rowIndex">
          <td v-for="(value, colIndex) in row" :key="colIndex">{{ value }}</td>
        </tr>
      </table>
    </div>

    <div v-if="error" style="color: red; margin-top: 20px;">
      <p>Error: {{ error }}</p>
    </div>
  </div>
</template>

<style>
body {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 20px;
}
table {
  margin: 10px auto;
}
button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>
