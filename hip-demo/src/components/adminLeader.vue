
// 个人中心组件
<template>
  <div class="container">
    <div class="demo-basic--circle">
      <iconbox></iconbox>
    </div>
    <router-view></router-view>
    <div class="btnbox"></div>
  </div>
</template>

<script>
import iconbox from "./iconbox.vue";

export default {
  data() {
    return {};
  },

  components: {
    iconbox,
  },
};
</script>

<style lang='less' scoped>
.container {
  position: relative;
  top: 30px;
}

.iconbox {
  position: relative;
  left: 50%;
  transform: translate(-50%);
}
</style>