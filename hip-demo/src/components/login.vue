<template>
  <div id="container">
    <div class="iconbox">
      <img src="../assets/logo.png" alt="" class="iconimg" />
    </div>
    <el-form class="loginform" :model="loginform" ref="loginformRef">
      <el-form-item>
        <el-input
          prefix-icon="el-icon-user"
          v-model="loginform.username"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-input
          prefix-icon="el-icon-lock"
          v-model="loginform.password"
          type="password"
        ></el-input>
      </el-form-item>
      <el-form-item class="btnbox">
        <el-button type="primary">登录</el-button>
        <el-button type="info" @click="loginformreset">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginform: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    loginformreset() {
      this.$refs.loginformRef.resetField();
    },
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

.iconbox {
  position: absolute;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: 1px solid #bbb;
  background-color: #bbb;
  padding: 10px;
}

.iconimg {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #fff;
}

.loginform {
  position: absolute;
  width: 100%;
  bottom: 0px;
  padding: 0 20px;
  box-sizing: border-box;
}

.btnbox {
  display: flex;
  justify-content: flex-end;
}
</style>