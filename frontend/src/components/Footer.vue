<template>
  <div class="footer">
    <footer>
      Copyright (C)&nbsp; 2020 yamaP
    </footer>
  </div>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped lang="scss">
footer {
    background-color: black;
    border-top: solid 1px white;
    border-bottom: solid 1px white;
    font-size: 14px;
    text-align: center;
    bottom: 0;
    left: 0;
    right: 0;
    box-sizing: border-box;
    z-index: 20;
    position: fixed;
}
</style>
