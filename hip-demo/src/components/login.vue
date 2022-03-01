<template>
  <div id="container">
    <el-form class="loginform">
      <el-form-item>
        <el-input></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style lang='less' scoped>
#container {
  background-color: #eee;
  width: 300px;
  height: 300px;
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.loginform {
  position: absolute;
  width: 100%;
  bottom: 0px;
  padding: 0 20px;
  box-sizing: border-box;
}
</style>