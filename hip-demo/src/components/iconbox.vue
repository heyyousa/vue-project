
// 大头像和头像选择组件
<template>
  <div class="iconbox">
    <div class="text-icon-container">
      <el-avatar
        :size="150"
        :src="chosenicon"
        class="icon"
        v-on:click.native="showicons"
      ></el-avatar>
      <div class="suf-title" v-on:click="showicons">{{ chooseiconText }}</div>
    </div>
    <div class="icons-container" ref="iconsRef">
      <el-avatar
        class="icons"
        shape="square"
        :size="50"
        :src="icon.url"
        v-for="icon in iconsurl"
        :key="icon.index"
        @click.native="chooseicon(icon)"
      ></el-avatar>
    </div>
  </div>
</template>

<script>
import axiosHip from "../utils/http-hip.js";

export default {
  data() {
    return {
      chosenicon: "",
      iconsurl: [],
      chooseiconText: "点击头像更换",
    };
  },

  methods: {
    async get_uicons() {
      const { data: res } = await axiosHip.get("/hipud/get_uicons/");
      this.iconsurl = res;
      this.chosenicon = res[0].url;
    },

    showicons() {
      if (this.$refs.iconsRef.style.display === "") {
        this.$refs.iconsRef.style.display = "block";
        this.chooseiconText = "点击头像关闭";
      } else if (this.$refs.iconsRef.style.display === "block") {
        this.$refs.iconsRef.style.display = "";
        this.chooseiconText = "点击头像更换";
      }
    },
    // 将每个小头像的icon对象传递进来以此获取对应的url
    chooseicon(icon) {
      this.chosenicon = icon.url;
    },
  },

  created() {
    this.get_uicons();
  },
};
</script>

<style lang="less" scoped>
.iconbox {
  width: 150px;
}

.icon {
  cursor: pointer;
}

.text-icon-container {
  width: 150px;
  text-align: center;
}

.suf-title {
  top: 80px;
}

.icons-container {
  display: none;
  position: absolute;
  z-index: 10;
  left: 50%;
  top: 180px;
  transform: translate(-50%);
  width: 425px;
  height: 300px;
  background-color: #666;
  overflow-y: auto;
  border-radius: 5px;
}

.icons {
  margin-left: 6px;
}
</style>