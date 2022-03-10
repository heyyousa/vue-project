<template>
  <div class="container">
    <el-form
      :model="infoform"
      :rules="inforules"
      ref="ruleForm"
      label-width="100px"
      class="userinfoform"
      style="font-size: 20px"
    >
      <el-form-item label="昵称" prop="username" :required="true">
        <el-input v-model="infoform.name"></el-input>
      </el-form-item>
      <el-form-item label="真实姓名" prop="realname">
        <el-input v-model="infoform.realname"></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="sex">
        <el-select v-model="infoform.sex" placeholder="请选择性别">
          <el-option label="男" value="nan"></el-option>
          <el-option label="女" value="nv"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="手机号" prop="phonenum">
        <el-input v-model="infoform.phonenum"></el-input>
      </el-form-item>
      <el-form-item label="科室" prop="keshi">
        <el-select v-model="infoform.keshi" placeholder="请选择科室">
          <el-option label="信息科" value="xinxike"></el-option>
          <el-option label="总务科" value="zongwuke"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="职务" prop="duty">
        <el-select v-model="infoform.duty" placeholder="请选择职务">
          <el-option label="主任" value="zhuren"></el-option>
          <el-option label="副主任" value="fuzhuren"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="个人简介" prop="introduce">
        <el-input type="textarea" v-model="infoform.introduce"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('infoform')"
          >保存更改
        </el-button>
        <el-button @click="resetForm('infoform')">重置</el-button>
        <el-button @click="goinfolist">返回</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      comflag: "1",
      infoform: {
        username: "",
        realname: "",
        sex: "",
        phonenum: "",
        keshi: "",
        duty: "",
        introduce: "",
      },
      inforules: {
        username: [],
        realname: [],
        sex: [],
        phonenum: [],
        keshi: [],
        duty: [],
        introduce: [],
      },
    };
  },

  methods: {
    goinfolist() {
      this.$emit("comflagchange", this.comflag);
    },
  },
};
</script>

<style lang='less' scoped>
.container {
  width: 50%;
  position: relative;
  left: 50%;
  transform: translate(-50%);
}
</style>