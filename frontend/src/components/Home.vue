<template>
  <div>
    <p>Home page</p>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button @click="getRandom">New random number</button>
    <h1></h1>
    <table>
    <form id="inputbox">
      <tr>
      <th></th>
      <td><input type="text" required placeholder="" id="input_nen"/></td>
      <td class="soe"></td>
      </tr>
      <tr>
      <th></th>
      <td><input type="text" required placeholder="5000���~�H" id="input_money"/></td>
      <td class="soe"></td>
      </tr>
      <tr>
      <th></th>
      <td><input type="text" required placeholder="�����H" id="input_rest"/></td>
      <td class="soe"></td>
      </tr>
      <tr>
      <th></th>
      <td><input type="text" required placeholder="�����ԁH" id="input_dotime"/></td>
      <td class="soe"></td>
      </tr>
      <tr>
      <th></th>
      <td><input type="text" required placeholder="�����ԁH" id="input_overtime"/></td>
      <td class="soe"></td>
      </tr>
      <tr>
      <th></th>
      <td><input type="text" required placeholder="�����H" id="input_rostime"/></td>
      <td class="soe"></td>
      </tr>
      <tr>
      <th></th>
      <td><input type="text" required placeholder="���~�H" id="input_rosmoney"/></td>
      <td class="soe"></td>
      </tr>
    </form>
    </table>
    <input type="submit" value="�v�Z" id="zikko" onclick="simulate();return false;"/>
    <div id="result"><div>
    <table id="data_list"></table>
    <footer>
      <p>
        Copyright (C)&nbsp; 2020 yamaP
      </p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getRandom()
  }
}
</script>

<style lang="scss">
body {
  background-color: rgb(240,240,255);
  width: 100%;
  padding: 0px;
  margin: 3% 0px;
  position: center;
}

table {
  margin: 20px 0px 0px 0px;
}

th {
  background-color: rgb(255,255,255);
}

tr {
  background-color: rgb(255,255,225);
}

td text {
  box-sizing:border-box;
  width: 100%;
}

td input {
  box-sizing:border-box;
  width: 100%;
}

#zikko {
  margin: 20px;
}

.soe {
  background-color: rgb(255,255,255);
}

h1 {
  font-size: 50px;
  background-color: rgb(255,200,200);
  margin: auto;
  opacity: 0.8;
}

footer p {
  margin: 20px 0px 0px 0px;
  font-size: 15px;
  background-color: rgb(255,255,255);
}
</style>
