<template>
  <div class="vbody">
    <div class="container">
      <iconbox></iconbox>
      <el-form
        :model="signform"
        class="signform"
        label-width="70px"
        ref="signform"
        :rules="signrules"
      >
        <el-form-item label="账号" prop="uid">
          <el-input
            v-model="signform.uid"
            placeholder="1-15位，禁止中文、空格、符号，推荐用本人工号"
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
        <el-form-item label="确认密码" prop="cfmPassword">
          <el-input
            v-model="signform.cfmPassword"
            placeholder="不超过15位"
            type="password"
          ></el-input>
        </el-form-item>
        <el-form-item class="btnbox">
          <el-button type="primary">注册</el-button>
          <el-button type="info" @click="resetform">重置</el-button>
          <el-button type="info" @click="backlogin">返回首页</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import iconbox from "../components/iconbox.vue";

export default {
  data() {
    return {
      signform: {
        uid: "",
        username: "",
        password: "",
        cfmPassword: "",
      },

      signrules: {
        uid: [
          {
            requeired: true,
            message: "不能为空",
            trigger: "blur",
          },
          {
            min: 1,
            max: 15,
            message: "长度在1-15位之间",
            trigger: "blur",
          },
          // {
          //   vaildator: checkcn,
          //   trigger: "blur",
          // },
        ],

        username: [
          { requeired: true, message: "不能为空" },
          { min: 1, max: 15, message: "长度在1-15位之间", trigger: "blur" },
        ],

        password: [
          {
            requeired: true,
            message: "不能为空",
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
  // 组件方法
  methods: {
    backlogin() {
      this.$router.push("/login");
    },

    resetform() {
      this.$refs.signform.resetFields();
    },
  },
  // 注册组件
  components: {
    iconbox,
  },
};
</script>

<style lang="less" scoped>
.vbody {
  width: 100%;
  height: 100%;
  background-color: #3f51b5;
}

.iconbox {
  position: absolute;
  z-index: 2;
  left: 50%;
  transform: translate(-50%, -50%);
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

.btnbox {
  display: flex;
  justify-content: flex-end;
}
</style>