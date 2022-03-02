<template>
  <div class="vbody">
    <div class="container">
      <el-form :model="signform">
        <el-form-item>
          <el-input></el-input>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      signform: {
        uid: "",
        username: "",
        password: "",
      },
    };
  },
};
</script>

<style lang="less" scoped>
.vbody {
  width: 100%;
  height: 100%;
  background-color: #3f51b5;
}

.container {
  background-color: #eee;
  width: 450px;
  height: 500px;
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  border-radius: 5px;
}
</style>