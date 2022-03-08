<template>
  <div class="vbody">
    <div id="container">
      <div class="iconbox">
        <img src="../assets/logo.png" alt="" class="iconimg" />
      </div>
      <el-form class="loginform" :model="loginform" ref="loginformRef">
        <el-form-item prop="username">
          <el-input
            prefix-icon="el-icon-user"
            v-model="loginform.username"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            prefix-icon="el-icon-lock"
            v-model="loginform.password"
            type="password"
          ></el-input>
        </el-form-item>
        <el-form-item class="btnbox">
          <el-button type="primary" @click="showpty">登录</el-button>
          <el-button type="success" @click="gosignup">注册</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 表单数据对象
      loginform: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    gosignup() {
      // 使用编程式导航跳转到注册组件
      this.$router.push("/sign");
    },

    showpty() {
      console.log(this["axios"]);
    },
  },
};
</script>

<style lang='less' scoped>
.vbody {
  width: 100%;
  height: 100%;
  background-color: #3f51b5;
}

#container {
  background-color: #eee;
  width: 450px;
  height: 300px;
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  border-radius: 5px;
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
  padding: 6px;
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