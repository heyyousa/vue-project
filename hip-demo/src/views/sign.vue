<template>
  <div class="vbody">
    <div class="container">
      <div class="iconbox">
        <el-avatar :size="150" :src="circleUrl" class="icon"></el-avatar>
        <div class="suf-title">选择头像</div>
      </div>
      <el-form
        :model="signform"
        class="signform"
        label-width="70px"
        ref="signform"
      >
        <el-form-item label="账号" prop="uid">
          <el-input
            v-model="signform.uid"
            placeholder="不超过15位，不允许包含中文，推荐使用本人工号"
          ></el-input>
        </el-form-item>
        <el-form-item label="昵称" prop="username">
          <el-input
            v-model="signform.username"
            placeholder="不超过15个字"
          ></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input
            v-model="signform.password"
            placeholder="不超过15位"
            type="password"
          ></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="password">
          <el-input
            v-model="signform.password"
            placeholder="不超过15位"
            type="password"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary">注册</el-button>
          <el-button type="info">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 加载本地图片资源用require函数
      circleUrl: require("../assets/logo.png"),

      signform: {
        uid: "",
        password: "",
        username: "",
      },

      signrules: {
        uid: [
          {
            requeired: true,
            message: "此为必填项",
            trigger: "blur",
          },
          {
            min: 1,
            max: 15,
            message: "长度在1-15之间",
            trigger: "blur",
          },
        ],

        password: [
          {
            requeired: true,
            message: "请输入密码",
            trigger: "blur",
          },
          {
            min: 1,
            max: 15,
            message: "长度在1-15位",
            trigger: "blur",
          },
        ],
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

.icon {
  position: absolute;
  left: 50%;
  top: -75px;
  transform: translate(-50%);
  cursor: pointer;
}

.suf-title {
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  top: 80px;
}

.container {
  background-color: #eee;
  width: 450px;
  height: 420px;
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  border-radius: 5px;
}

.signform {
  position: absolute;
  width: 100%;
  bottom: 0px;
  padding: 0 20px;
  box-sizing: border-box;
}
</style>