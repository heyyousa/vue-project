
// 领导意见箱组件
<template>
  <div>
    <div class="badgebox">
      <el-badge :value="12" class="item">
        <el-button size="small">新邮件</el-button>
      </el-badge>
      <el-badge :value="3" class="item">
        <el-button size="small">新回复</el-button>
      </el-badge>
      <el-badge :value="1" class="item" type="primary">
        <el-button size="small">未处理</el-button>
      </el-badge>
      <el-badge :value="2" class="item" type="warning">
        <el-button size="small">全部邮件</el-button>
      </el-badge>
    </div>
    <el-table :data="mailsData" stripe style="width: 100%">
      <el-table-column prop="date" label="日期" width="105"> </el-table-column>
      <el-table-column prop="name" label="昵称" width="130"> </el-table-column>
      <el-table-column prop="address" label="标题"> </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mailsData: [
        {
          date: "2016-05-02",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1518 弄",
        },
        {
          date: "2016-05-04",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1517 弄",
        },
        {
          date: "2016-05-01",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1519 弄",
        },
        {
          date: "2016-05-03",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1516 弄",
        },
      ],
    };
  },
};
</script>

<style lang='less' scoped>
.badgebox {
  margin-bottom: 10px;
}

.item {
  margin-top: 10px;
  margin-right: 40px;
}
</style>