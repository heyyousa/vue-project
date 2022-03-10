
// 用户信息展示列表组件
<template>
  <div>
    <el-descriptions
      class="margin-top"
      title="用户信息"
      :column="3"
      size=""
      border
    >
      <template slot="extra">
        <el-button type="primary" size="small" @click="goinfoform"
          >编辑</el-button
        >
      </template>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-user"></i>
          账号
        </template>
        001
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-edit"></i>
          昵称
        </template>
        赵彬
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-view"></i>
          真实姓名
        </template>
        赵彬
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-office-building"></i>
          性别
        </template>
        男
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-mobile-phone"></i>
          手机号
        </template>
        18011112222
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-place"></i>
          所在科室
        </template>
        院长办公室
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-office-building"></i>
          职务
        </template>
        院长
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-reading"></i>
          个人简介
        </template>
        简单说点什么吧
      </el-descriptions-item>
    </el-descriptions>
  </div>
</template>

<script>
export default {
  name: "userinfolist",

  data() {
    return {
      comflag: "2",
    };
  },

  methods: {
    goinfoform() {
      this.$emit("comflagchange", this.comflag);
    },
  },
};
</script>

<style lang='less' scoped>
</style>