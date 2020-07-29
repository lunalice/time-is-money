<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
    <div>
      <p>Home page</p>
      <p>Random number from backend: {{ randomNumber }}</p>
      <button @click="getRandom">New random number</button>
    </div>
    <h1>時給シミュレーター</h1>
    <form id="inputbox">
      <table>
        <tr>
          <th>年齢</th>
          <td>
            <input
              type="text"
              v-model="user.age"
              required
              placeholder="16"
              id="input_nen"
            />
          </td>
          <td class="soe">年齢</td>
        </tr>
        <tr>
          <th>年収</th>
          <td>
            <input
              type="text"
              v-model="user.annual_income"
              required
              placeholder="500"
              id="input_money"
            />
          </td>
          <td class="soe">年収</td>
        </tr>
        <tr>
          <th>労働時間</th>
          <td>
            <input
              type="text"
              required
              placeholder="8"
              v-model="user.working_hours"
              id="input_dotime"
            />
          </td>
          <td class="soe">労働時間</td>
        </tr>
        <tr>
          <th>残業時間</th>
          <td>
            <input
              type="text"
              required
              placeholder="40"
              v-model="user.overtime"
              id="input_overtime"
            />
          </td>
          <td class="soe">残業時間</td>
        </tr>
        <tr>
          <th>通勤時間(分)</th>
          <td>
            <input
              type="text"
              required
              placeholder="60"
              v-model="user.commuting_time"
              id="input_commuting_time"
            />
          </td>
          <td class="soe">通勤時間（分）</td>
        </tr>
        <tr>
          <th>家賃（月）</th>
          <td>
            <input
              type="text"
              required
              placeholder="5"
              v-model="user.rent"
              id="input_rent"
            />
          </td>
          <td class="soe">家賃（月）</td>
        </tr>
      </table>

      <input
        type="submit"
        value="シミュレート"
        id="zikko"
        @click="saveAsNew()"
      />
    </form>
    <div id="result"></div>
    <table id="data_list"></table>
    <footer>
      <p>Copyright (C)&nbsp; 2020 yamaP</p>
    </footer>
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

td text {
  box-sizing: border-box;
  width: 100%;
}

td input {
  box-sizing: border-box;
  width: 100%;
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

footer p {
  margin: 20px 0px 0px 0px;
  font-size: 15px;
  background-color: rgb(255, 255, 255);
}
</style>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";

// // 調整する
// export const apiEndpointRoot =
//   (process.env.ENGINE_MOUNT_TO_ROOT !== '0') ? '/api' : '/web/api';

export default {
  name: "Home",
  // components: {
  //   HelloWorld
  // },
  data() {
    return {
      randomNumber: 0,
      user: {
        age: 16,
        annual_income: 200,
        // holiday: 10, dbに融合
        working_hours: 8,
        overtime: 40,
        commuting_time: 60,
        rent: 55000
      }
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
          this.randomNumber = response.data.randomNumber;
        })
        .catch(error => {
          console.log(error);
        });
      // return fetch(
      //   `${apiEndpointRoot}/places/`,
      //   Object.assign({}, defaultPostParams, {
      //     body: JSON.stringify(placeData),
      //   }))
      //   .then(response => response.json());
    }
  },
  created() {
    this.getRandom();
  }
};

// // backendでやるべきものがほとんどなのでいい感じに移植する
// let str_path = location.pathname;
// let str_array = str_path.split("/");
// let input_list_path =
//   str_path
//     .replace(str_array.pop(), "")
//     .substring(1)
//     .replace("/", "/") + "data/inputdata.txt";

// // vueMountに移動がいいかも
// // window.onload=function(){
// //  readRecord();
// // }

// function simulate() {
//   let input_nen = document.getElementById("input_nen").value;
//   let input_money = document.getElementById("input_money").value;
//   let input_rest = document.getElementById("input_rest").value;
//   let input_dotime = document.getElementById("input_dotime").value;
//   let input_overtime = document.getElementById("input_overtime").value;
//   let input_rostime = document.getElementById("input_rostime").value;
//   let input_rosmoney = document.getElementById("input_rosmoney").value;
//   simulate_output(
//     input_nen,
//     input_money,
//     input_rest,
//     input_dotime,
//     input_overtime,
//     input_rostime,
//     input_rosmoney
//   );
//   insertRecord();
// }

// function simulate_output(
//   input_nen,
//   input_money,
//   input_rest,
//   input_dotime,
//   input_overtime,
//   input_rostime,
//   input_rosmoney
// ) {
//   var str_edit = "";
//   var result = exRound(
//     keisan(input_money, input_rest, input_dotime, input_overtime),
//     1
//   );
//   str_edit =
//     " " +
//     input_nen +
//     '�΂���̎����� <font color="red">' +
//     result +
//     "</font> �~�ł��B</br>";
//   str_edit =
//     str_edit +
//     '������ <font color="red">' +
//     exRound((input_money * 10000) / activeDays(input_rest), 1) +
//     '</font> �~(�ғ� <font color="red">' +
//     exRound(
//       Number(input_dotime) + Number(input_overtime / activeDays(input_rest)),
//       2
//     ) +
//     "</font> ����)�ł��B</br>";
//   var result_ros = exRound(ros_keisan(result, input_rostime, input_rest), 1);
//   str_edit =
//     str_edit +
//     '�ʋΎ��Ԃ͔N�� <font color="red">' +
//     exRound(rosTime(input_rostime, input_rest), 1);
//   str_edit =
//     str_edit +
//     '</font> ���Ԃ� <font color="red">' +
//     result_ros +
//     "</font> �~����Ă��܂��B</br>";
//   var yachin = input_rosmoney * 12;
//   str_edit =
//     str_edit +
//     '�ƒ�(<font color="red">' +
//     yachin +
//     '</font>�~)���킹�N�� <font color="red">' +
//     exRound(Number(result_ros) + yachin, 1) +
//     "</font> �~����Ă��܂��B</br>";
//   str_edit =
//     str_edit +
//     '�N�Ԏ����� (<font color="red">' +
//     input_money * 10000 +
//     '</font>�~ - <font color="red">' +
//     exRound(Number(result_ros) + yachin, 1) +
//     '</font>�~) = <font color="red">' +
//     (input_money * 10000 - exRound(Number(result_ros) + yachin, 1)) +
//     '</font>(�c�ƕ�<font color="red">' +
//     input_overtime * result +
//     "</font>)�~�ł��I</br></br>" +
//     "�ߖ�q���g�F�ƒ����グ�ĒʋΎ��Ԃ������Ă݂悤�I</br>" +
//     "�����Ԃ̂ݑz�肵�Ă���ׁA���M��E�H��͍l�����Ă���܂���B</br>";
//   document.getElementById("result").innerHTML = str_edit;
// }

// function exRound(input_number, input_keta) {
//   return (
//     Math.round(input_number * Math.pow(10, input_keta)) /
//     Math.pow(10, input_keta)
//   );
// }

// function keisan(input_money, input_rest, input_dotime, input_overtime) {
//   var activeday = activeDays(input_rest);
//   var day_money = (input_money * 10000) / activeday;
//   var day_time = Number(input_dotime) + input_overtime / activeday;
//   return day_money / day_time;
// }

// function activeDays(rest) {
//   return 365 - rest;
// }

// function ros_keisan(result, input_rostime, input_rest) {
//   return result * rosTime(input_rostime, input_rest);
// }

// function rosTime(input_rostime, input_rest) {
//   return ((input_rostime * 2) / 60) * (365 - input_rest);
// }

// function insertRecord() {
//   var fs = new ActiveXObject("Scripting.FileSystemObject");
//   var file_path = fs.openTextFile(input_list_path, 1, false, 0);
//   var string_array = file_path.AtEndOfStream ? "" : file_path.ReadAll();
//   string_array = string_array.split(",");
//   file_path.close();
//   var createID =
//     string_array.length != 0 ? 1 + (string_array.length - 1) / 8 : 1;
//   var file_path = fs.openTextFile(input_list_path, 8, false, 0);
//   var str_record =
//     createID +
//     "," +
//     document.getElementById("input_nen").value +
//     "," +
//     document.getElementById("input_money").value +
//     "," +
//     document.getElementById("input_rest").value +
//     ",";
//   str_record =
//     str_record +
//     document.getElementById("input_dotime").value +
//     "," +
//     document.getElementById("input_overtime").value +
//     "," +
//     document.getElementById("input_rostime").value +
//     ",";
//   str_record =
//     str_record + document.getElementById("input_rosmoney").value + ",";
//   file_path.write(str_record);
//   file_path.close();
//   readRecord();
// }

// function deleteRecord() {
//   var fs = new ActiveXObject("Scripting.FileSystemObject");
//   var file_path = fs.openTextFile(input_list_path, 1, false, 0);
//   var string_array = file_path.ReadAll();
//   file_path.close();
//   var array_buff = string_array.split(",");
//   var data_list = document.getElementById("data_list");
//   for (var i = 1; i < data_list.rows.length; i++) {
//     if (data_list.rows(i).getElementsByTagName("input")[0].checked == true) {
//       data_list.rows(i).getElementsByTagName("input")[0].checked = false;
//       var str_buff = "";
//       for (var j = 0; j < data_list.rows[i].cells.length; j++) {
//         str_buff = str_buff + data_list.rows[i].cells[j].innerText + ",";
//       }
//       alert(str_buff + "���폜���܂��B");
//       string_array = string_array.replace(str_buff, "");
//       i = i - 1;
//     }
//   }
//   file_path = fs.openTextFile(input_list_path, 2, false, 0);
//   file_path.write(string_array);
//   file_path.close();
//   readRecord();
// }

// function readRecord() {
//   document.getElementById("data_list").innerHTML = "";
//   var fs = new ActiveXObject("Scripting.FileSystemObject");
//   var file_path = fs.openTextFile(input_list_path, 1, false, 0);
//   var string_array = file_path.AtEndOfStream
//     ? "".split(",")
//     : file_path.ReadAll().split(",");
//   var tr = document.createElement("tr");
//   tr.innerHTML =
//     "<tr><th></th><th>ID</th><th>�N��</th><th>�N��</th><th>�x��</th><th>�Ζ�����</th><th>�c�Ǝ���</th><th>�ʋΎ���</th><th>�ƒ�</th></tr>";
//   document.getElementById("data_list").appendChild(tr);
//   for (var i = 0; i < string_array.length - 1; i = i + 8) {
//     var tr = document.createElement("tr");
//     tr.innerHTML =
//       '<input name="selectTarget" type="radio" onChange="checkAdd();"/>';
//     for (var j = 0; j < 8; j++) {
//       tr.innerHTML = tr.innerHTML + "<td>" + string_array[i + j] + "</td>";
//     }
//     tr.innerHTML =
//       tr.innerHTML +
//       '<input·type="submit"·value=""·onclick="deleteRecord();"/>';
//     document.getElementById("data_list").appendChild(tr);
//   }
//   file_path.close();
// }

// function checkAdd() {
//   var data_list = document.getElementById("data_list");
//   for (var i = 1; i < data_list.rows.length; i++) {
//     if (data_list.rows(i).getElementsByTagName("input")[0].checked == true) {
//       for (var j = 0; j < data_list.rows[i].cells.length; j++) {
//         switch (j) {
//           case 1:
//             var input_nen = data_list.rows[i].cells[j].innerHTML;
//             break;
//           case 2:
//             var input_money = data_list.rows[i].cells[j].innerHTML;
//             break;
//           case 3:
//             var input_rest = data_list.rows[i].cells[j].innerHTML;
//             break;
//           case 4:
//             var input_dotime = data_list.rows[i].cells[j].innerHTML;
//             break;
//           case 5:
//             var input_overtime = data_list.rows[i].cells[j].innerHTML;
//             break;
//           case 6:
//             var input_rostime = data_list.rows[i].cells[j].innerHTML;
//             break;
//           case 7:
//             var input_rosmoney = data_list.rows[i].cells[j].innerHTML;
//             break;
//         }
//       }
//     }
//   }
//   simulate_output(
//     input_nen,
//     input_money,
//     input_rest,
//     input_rest,
//     input_dotime,
//     input_overtime,
//     input_rostime,
//     input_rosmoney
//   );
// }
</script>
