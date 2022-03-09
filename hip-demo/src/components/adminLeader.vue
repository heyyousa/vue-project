
// 个人中心组件
<template>
  <div class="container">
    <div class="iconbox">
      <el-avatar :size="150" :src="uinfo" @error="errorHandler">
        <img :src="imgerror" />
      </el-avatar>
    </div>
    <router-view></router-view>
    <div class="btnbox"></div>
  </div>
</template>

<script>
import axiosHip from "../utils/http-hip";
import imgerror from "../assets/img/imgerror.png";
export default {
  data() {
    return {
      iconurl: "",
      imgerror: imgerror,
      uinfo: {},
    };
  },

  methods: {
    errorHandler() {
      return true;
    },

    async inituserinfo() {
      const { data: res } = axiosHip.get("/hipud/get_uinfo");
      this.uinfo = res;
    },
  },

  created() {
    this.inituserinfo();
  },

  components: {},
};
</script>

<style lang='less' scoped>
.container {
  position: relative;
  top: 30px;
}

.iconbox {
  position: relative;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  left: 50%;
  transform: translate(-50%);
}

.iconimg {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #fff;
}
</style>