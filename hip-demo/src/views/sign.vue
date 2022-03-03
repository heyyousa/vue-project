<template>
  <div class="vbody">
    <div class="container">
      <el-form
        :model="signform"
        class="signform"
        label-width="80px"
        :rules="signrules"
        ref="signform"
      >
        <el-form-item label="账号" prop="uid">
          <el-input
            v-model="signform.uid"
            placeholder="不超过15位，不允许包含中文，推荐使用本人工号"
          ></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input
            v-model="signform.password"
            placeholder="不超过15位"
            type="password"
          ></el-input>
        </el-form-item>
        <el-form-item label="昵称" prop="username">
          <el-input
            v-model="signform.username"
            placeholder="不超过15个字"
          ></el-input>
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

.signform {
  position: absolute;
  width: 100%;
  bottom: 0px;
  padding: 0 20px;
  box-sizing: border-box;
}
</style>