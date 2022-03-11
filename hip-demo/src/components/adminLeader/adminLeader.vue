
// 个人中心组件
<template>
  <div class="container">
    <div class="iconbox1" v-if="comflag == 1">
      <el-avatar :size="150" :src="uinfo.iconurl" @error="errorHandler">
        <img :src="imgerror" />
      </el-avatar>
    </div>
    <iconbox v-else-if="comflag == 2" @comflagchange="getnewcomflag"></iconbox>
    <userinfolist
      v-if="comflag == 1"
      @comflagchange="getnewcomflag"
    ></userinfolist>
    <userinfoform
      v-else-if="comflag == 2"
      @comflagchange="getnewcomflag"
    ></userinfoform>
    <div class="btnbox"></div>
  </div>
</template>

<script>
import axiosHip from "../../utils/http-hip";
import userinfolist from "./userinfolist.vue";
import userinfoform from "./userinfoform.vue";
import iconbox from "../iconbox.vue";
import axios from "axios";

export default {
  data() {
    return {
      iconurl: "",
      imgerror: require("../../assets/img/imgerror.png"),
      //用户信息
      uinfo: {},
      // comname: "userinfolist",
      comflag: "1",
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

    getnewcomflag(val) {
      this.comflag = val;
    },
  },

  created() {
    // this.inituserinfo();
  },

  components: {
    userinfolist,
    userinfoform,
    iconbox,
  },
};
</script>

<style lang='less' scoped>
.container {
  position: relative;
  top: 30px;
}

.iconbox1 {
  position: relative;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  left: 50%;
  transform: translate(-50%);
}

.iconbox {
  position: relative;
  z-index: 10;
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