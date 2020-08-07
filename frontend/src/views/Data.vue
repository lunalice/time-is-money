<template>
  <div class="data container pb-50" v-if="users">
    <paginate name="paginate-users" :list="users" :per="10">
      <div class="table-responsive">
        <table class="table table-dark">
          <thead>
            <tr>
              <th scope="col">checked</th>
              <th scope="col">年齢</th>
              <th scope="col">年収</th>
              <th scope="col">休日</th>
              <th scope="col">勤務時間</th>
              <th scope="col">残業時間</th>
              <th scope="col">通勤時間</th>
              <th scope="col">家賃</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in paginated('paginate-users')" :key="user.id">
              <th scope="row"><input name="selectTarget" type="radio" @change="selectedUser($event, index)" /></th>
              <td>{{ user.age }}</td>
              <td>{{ user.annual_income }}</td>
              <td>{{ user.holiday }}</td>
              <td>{{ user.working_hours }}</td>
              <td>{{ user.overtime }}</td>
              <td>{{ user.commuting_time }}</td>
              <td>{{ user.rent }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </paginate>
    <nav aria-label="Page navigation">
      <paginate-links
        for="paginate-users"
        :classes="{
          'ul': ['pagination', 'justify-content-center'],
          'li': 'page-item',
          'a': ['page-link', 'page-link--color']
        }"
        :show-step-links="true">
      </paginate-links>
    </nav>
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
      selected: false,
      paginate: ['paginate-users']
    };
  },
  methods: {
    getUsers() {
      const path = process.env.VUE_APP_API_BASE_URL ? `${process.env.VUE_APP_API_BASE_URL}api/users`
        : `http://localhost:5000/api/users`;
      axios
        .get(path)
        .then(response => {
          this.users = response.data;
        })
        .catch(error => {
          console.log('database filed.');
          return Promise.reject(error);
        });
    },
    selectedUser(event, index) {
      this.selected = this.users[index];
    }
  },
  mounted() {
    this.getUsers();
  }
};
</script>

<style scoped lang="scss">
.data {
  ul {
    padding: 0;
  }
  nav {
    color: #007bff !important;
    &:active {
      color: #fff !important;
    }
  }
}
</style>
