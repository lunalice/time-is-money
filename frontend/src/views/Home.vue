<template>
  <div class="home">
    <h1>Time is Money</h1>
    <form>
      <table class="table table-dark">
        <tr>
          <th>年齢</th>
          <td>
            <input
              type="text"
              v-model="user.age"
              required
              placeholder="例：16"
            />
          </td>
          <td class="soe">才</td>
        </tr>
        <tr>
          <th>年収</th>
          <td>
            <input
              type="text"
              v-model="user.annual_income"
              required
              placeholder="例：500"
            />
          </td>
          <td class="soe">万</td>
        </tr>
        <tr>
          <th>労働時間</th>
          <td>
            <input
              type="text"
              required
              placeholder="例：8"
              v-model="user.working_hours"
            />
          </td>
          <td class="soe">時間</td>
        </tr>
        <tr>
          <th>平均残業時間（月）</th>
          <td>
            <input
              type="text"
              required
              placeholder="例：40"
              v-model="user.overtime"
            />
          </td>
          <td class="soe">時間</td>
        </tr>
        <tr>
          <th>通勤時間(片道)</th>
          <td>
            <input
              type="text"
              required
              placeholder="例：60"
              v-model="user.commuting_time"
            />
          </td>
          <td class="soe">分</td>
        </tr>
        <tr>
          <th>家賃（月額）</th>
          <td>
            <input
              type="text"
              required
              placeholder="例：50000"
              v-model="user.rent"
            />
          </td>
          <td class="soe">円</td>
        </tr>
      </table>

      <input
        type="button"
        value="シミュレート"
        id="zikko"
        @click="saveAsNew()"
      />
    </form>
    <Result :result="result" />
  </div>
</template>

<style lang="scss">
body {
  background-color: rgb(240, 240, 255);
  width: 100%;
  padding: 0px;
  margin: 3% 0px;
}

table {
  margin-left: 0px;
  margin-right: 0px;
  margin: auto;
}

th {
  background-color: rgb(255, 255, 255);
}

tr {
  background-color: rgb(255, 255, 225);
}

td {
  text {
    box-sizing: border-box;
    width: 100%;
  }

  input {
    box-sizing: border-box;
    width: 100%;
  }
}

#zikko {
  margin: 20px;
}

.soe {
  background-color: rgb(255, 255, 255);
}

h1 {
  font-size: 50px;
  background-color: rgb(255, 200, 200);
  margin: auto;
  opacity: 0.8;
}
</style>

<script>
// @ is an alias to /src
import Result from "@/components/Result.vue";
import axios from "axios";

// // 調整する
// export const apiEndpointRoot =
//   (process.env.ENGINE_MOUNT_TO_ROOT !== '0') ? '/api' : '/web/api';

export default {
  name: "Home",
  components: {
    Result
  },
  data() {
    return {
      randomNumber: 0,
      user: {
        age: 16,
        annual_income: 200,
        working_hours: 8,
        overtime: 40,
        commuting_time: 60,
        rent: 55000
      },
      result: false
    };
  },
  methods: {
    getRandom() {
      this.randomNumber = this.getRandomFromBackend();
    },
    getRandomFromBackend() {
      const path = `http://localhost:5000/api/random`;
      axios
        .get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber;
        })
        .catch(error => {
          console.log(error);
        });
    },
    saveAsNew() {
      const params = new URLSearchParams();
      params.append("age", this.user.age);
      params.append("annual_income", this.user.annual_income);
      params.append("working_hours", this.user.working_hours);
      params.append("overtime", this.user.overtime);
      params.append("commuting_time", this.user.commuting_time);
      params.append("rent", this.user.rent);
      const path = `http://localhost:5000/api/users`;
      axios
        .post(path, params)
        .then(response => {
          this.result = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    this.getRandom();
  }
};
</script>
