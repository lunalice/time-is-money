<template>
  <div class="data" v-if="users">
    <h1>触ってくれた方々</h1>
    <table class="table table-dark">
      <tr><th></th><th></th><th>年齢</th><th>年収</th><th>休日</th><th>勤務時間</th><th>残業時間</th><th>通勤時間</th><th>家賃</th></tr>
      <tr v-for="(user, index) in users" :key="user.id"><th></th><th><input name="selectTarget" type="radio" @change="selectedUser($event, index)" /></th><th>{{ user.age }}</th><th>{{ user.annual_income }}</th><th>{{ user.holiday }}</th><th>{{ user.working_hours }}</th><th>{{ user.overtime }}</th><th>{{ user.commuting_time }}</th><th>{{ user.rent }}</th></tr>
    </table>
    <!-- pagenation実装・・・ -->
    <Result :result="selected" />
  </div>
</template>
<script>
import Result from "@/components/Result.vue";
import axios from "axios";

export default {
  name: "Data",
  components: {
    Result
  },
  data() {
    return {
      users: false,
      selected: false
    };
  },
  methods: {
    getUsers() {
      const path = `http://localhost:5000/api/users`;
      axios
        .get(path)
        .then(response => {
          this.users = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    selectedUser(event, index) {
      this.selected = this.users[index];
    }
  },
  created() {
    this.getUsers();
  }
};
</script>

<style scoped lang="scss"></style>
