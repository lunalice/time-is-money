<template>
  <div class="simulator container pb-50">
    <form class="pb-50">
      <div class="form-group row" :class="{ 'form-group--error': $v.user.age.$error }">
        <label class="col-sm-2 col-form-label-sm col-form-label">年齢</label>
        <div class="col-sm-10">
          <input type="text" v-model.trim="$v.user.age.$model" required class="form-control-sm form-control" placeholder="例：16">
        </div>
      </div>
      <div class="error" v-if="!$v.user.age.required">Field is required</div>
      <div class="error" v-if="!$v.user.age.between">greater than or equal to {{ $v.user.age.$params.between.min }}. less than or equal to {{ $v.user.age.$params.between.max }}</div>
      <div class="form-group row" :class="{ 'form-group--error': $v.user.annual_income.$error }">
        <label class="col-sm-2 col-form-label-sm col-form-label">年収</label>
        <div class="col-sm-10">
          <input type="text" v-model="$v.user.annual_income.$model" required class="form-control-sm form-control" placeholder="例：500">
        </div>
      </div>
      <div class="error" v-if="!$v.user.annual_income.required">Field is required</div>
      <div class="error" v-if="!$v.user.annual_income.between">greater than or equal to {{ $v.user.annual_income.$params.between.min }}. less than or equal to {{ $v.user.annual_income.$params.between.max }}</div>
      <div class="form-group row" :class="{ 'form-group--error': $v.user.working_hours.$error }">
        <label class="col-sm-2 col-form-label-sm col-form-label">労働時間</label>
        <div class="col-sm-10">
          <input type="text" v-model="$v.user.working_hours.$model" required class="form-control-sm form-control" placeholder="例：8">
        </div>
      </div>
      <div class="error" v-if="!$v.user.working_hours.required">Field is required</div>
      <div class="error" v-if="!$v.user.working_hours.between">greater than or equal to {{ $v.user.working_hours.$params.between.min }}. less than or equal to {{ $v.user.working_hours.$params.between.max }}</div>
      <div class="form-group row" :class="{ 'form-group--error': $v.user.overtime.$error }">
        <label class="col-sm-2 col-form-label-sm col-form-label">平均残業時間（月）</label>
        <div class="col-sm-10">
          <input type="text" v-model="$v.user.overtime.$model" required class="form-control-sm form-control" placeholder="例：40">
        </div>
      </div>
      <div class="error" v-if="!$v.user.overtime.required">Field is required</div>
      <div class="error" v-if="!$v.user.overtime.between">greater than or equal to {{ $v.user.overtime.$params.between.min }}. less than or equal to {{ $v.user.overtime.$params.between.max }}</div>
      <div class="form-group row" :class="{ 'form-group--error': $v.user.commuting_time.$error }">
        <label class="col-sm-2 col-form-label-sm col-form-label">通勤時間（片道分）</label>
        <div class="col-sm-10">
          <input type="text" v-model="$v.user.commuting_time.$model" required class="form-control-sm form-control" placeholder="例：60">
        </div>
      </div>
      <div class="error" v-if="!$v.user.commuting_time.required">Field is required</div>
      <div class="error" v-if="!$v.user.commuting_time.between">greater than or equal to {{ $v.user.commuting_time.$params.between.min }}. less than or equal to {{ $v.user.commuting_time.$params.between.max }}</div>
      <div class="form-group row" :class="{ 'form-group--error': $v.user.rent.$error }">
        <label class="col-sm-2 col-form-label-sm col-form-label">家賃（月額）</label>
        <div class="col-sm-10">
          <input type="text" v-model="$v.user.rent.$model" required class="form-control-sm form-control" placeholder="例：50000">
        </div>
      </div>
      <div class="error" v-if="!$v.user.rent.required">Field is required</div>
      <div class="error" v-if="!$v.user.rent.between">greater than or equal to {{ $v.user.rent.$params.between.min }}. less than or equal to {{ $v.user.rent.$params.between.max }}</div>
      <div class="form-group row">
        <input
          type="button"
          value="シミュレート"
          class="btn btn-outline-primary"
          @click="submit()"
        />
      </div>
    </form>
    <Result :result="result" />
  </div>
</template>

<style lang="scss"></style>

<script>
// @ is an alias to /src
import { required, between } from "vuelidate/lib/validators";
import Result from "@/components/Result.vue";
import axios from "axios";

export default {
  name: "Simulator",
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
      result: false,
      submitStatus: ""
    };
  },
  validations: {
    user: {
      age: {
        required,
        between: between(16, 65)
      },
      annual_income: {
        required,
        between: between(150, 1350)
      },
      working_hours: {
        required,
        between: between(1, 8)
      },
      overtime: {
        required,
        between: between(0, 80)
      },
      commuting_time: {
        required,
        between: between(0, 120)
      },
      rent: {
        required,
        between: between(20000, 1000000)
      }
    }
  },
  methods: {
    submit() {
      this.$v.$touch();
      if (this.$v.$invalid) {
        this.submitStatus = "ERROR";
      } else {
        this.submitStatus = "PENDING";
        setTimeout(() => {
          this.saveAsNew();
        }, 500);
      }
    },
    saveAsNew() {
      const params = new URLSearchParams();
      params.append("age", this.user.age);
      params.append("annual_income", this.user.annual_income);
      params.append("working_hours", this.user.working_hours);
      params.append("overtime", this.user.overtime);
      params.append("commuting_time", this.user.commuting_time);
      params.append("rent", this.user.rent);
      const path = process.env.VUE_APP_API_BASE_URL
        ? `${process.env.VUE_APP_API_BASE_URL}api/users`
        : `http://localhost:5000/api/users`;
      axios
        .post(path, params)
        .then(response => {
          this.result = response.data;
        })
        .catch(error => {
          console.log('database filed.');
          return Promise.reject(error);
        });
    }
  }
};
</script>
