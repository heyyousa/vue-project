<template>
  <el-container class="container">
    <el-aside>
      <el-menu
        :default-active="this.$route.path"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        :router="true"
      >
        <el-menu-item index="/mailLeader/mails">
          <i class="el-icon-s-promotion"></i>
          <span slot="title">意见箱</span>
        </el-menu-item>
        <el-menu-item index="2">
          <i class="el-icon-menu"></i>
          <span slot="title">院内贴吧</span>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="el-icon-document"></i>
          <span slot="title">文件共享</span>
        </el-menu-item>
        <el-menu-item index="/mailLeader/admin">
          <i class="el-icon-user"></i>
          <span slot="title">个人中心</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },

    gomailbox() {
      this.$router.push("/mailLeader/mails");
    },

    goadmin() {
      this.$router.push("/mailLeader/admin");
    },
  },
};
</script>

<style lang='less' scoped>
.container {
  height: 100%;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  width: 200px !important;
  height: 100%;
}

.el-menu-vertical-demo {
  height: 100%;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
}

.badgebox {
  margin-bottom: 10px;
}

.item {
  margin-top: 10px;
  margin-right: 40px;
}
</style>