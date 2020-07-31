<template>
  <div class="result" v-if="result">
    <h1>診断結果</h1>
    <p>
      {{ result.age }}才さんの時給は {{ result.hourly_wage }} 円です。<br />
      日給は{{ result.daily_wage }}円（稼働{{result.operating_time }}時間）です。
      通勤時間は年間{{ result.annual_commuting_time }}時間で金額にして{{ result.consumption }}円消費されてます。<br />
      家賃（{{ result.annual_rent }}円）と合わせて{{ result.annual_rent + result.consumption }}円消費されています。<br />
      年間収入は（{{ result.annual_income }}円 - {{ result.annual_rent + result.consumption }}円) =
      {{ result.income }}(残業分{{ result.overtime_pay }}円)です！<br />
    </p>
    <p>
      節約のヒント：通勤時間を下げて見よう！リモートワークって最高だよね！<br />
      家賃が高くても通勤時間が下がるなら有効！<br />
      ※ 時間のみ考慮している為、光熱費・食費等は含んでいません。<br />
      ※ 空いた時間は年収を上げる為にスキル向上に使うもよし、年収に満足してるなら趣味に使うのもよき<br />
    </p>
    <a :href="result.twitter_intent_url" target="_blank" rel="noopener">tweet</a>
  </div>
</template>

<script>
export default {
  name: "Result",
  props: {
    result: Object
  }
};
</script>

<style scoped lang="scss"></style>
