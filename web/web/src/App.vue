<template>
  <a-layout id="components-layout-demo-top" class="layout">
    <a-layout-header>
      <a-menu
        theme="dark"
        mode="horizontal"
        :defaultSelectedKeys="['1']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1">nav 1</a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>新建日志</a-breadcrumb-item>
      </a-breadcrumb>
      
      <div :style="{ background: '#fff', padding: '24px'}">内容</div>
      <div :style="{ background: '#fff', padding: '0px 24px 24px 24px'}">
      <a-textarea
        placeholder="关键词+大概工作内容"
        :auto-size="{ minRows: 2, maxRows: 6 }"
        v-model="content"
      />
      <a-button type="primary" :style="{margin: '10px 0px 0px 0px'}" @click="posting">
       提交
      </a-button>
      </div>
    </a-layout-content>
    
    <a-layout-content style="padding: 0 50px">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>历史日志</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ background: '#fff', padding: '24px 24px 24px 24px'}">
        <!-- <a-timeline>
          <a-timeline-item>创建服务现场 2015-09-01</a-timeline-item>
          <a-timeline-item>初步排除网络异常 2015-09-01</a-timeline-item>
          <a-timeline-item>技术测试异常 2015-09-01</a-timeline-item>
          <a-timeline-item>{{info}}</a-timeline-item>
        </a-timeline> -->
        <a-timeline v-if="showTimeLine">
        <a-timeline-item v-for="(item, index) in info" :key="index">
          {{item.time}}{{"  " + item.content}}
        </a-timeline-item>
        </a-timeline>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      Record ©2021 Created by Fzr
    </a-layout-footer>
  </a-layout>
</template>
<style>
#components-layout-demo-top .logo {
  width: 120px;
  height: 31px;
  background: rgba(255,255,255,.2);
  margin: 16px 24px 16px 0;
  float: left;
}
</style>
<script>
export default {
  data() {
    return {
      content: "",
      info: [],
      showTimeLine: true,
      timer: '',
    }
  },
  created() {
      if (window.Notification) {
        // 浏览器通知--window.Notification
        if (Notification.permission == "granted") {
          console.log("允许通知")
        }else if( Notification.permission != "denied"){
          console.log("需要通知权限")
          Notification.requestPermission(()=> {});
        }
      } else {
        console.error('浏览器不支持Notification');
      }
      setInterval(this.popNotice, 1000*60*10)
  },
  mounted() {
    this.axios
      .get('http://api.itsinghua.top/article/article-list/?secret_key=record')
      .then(response => 
        {
          this.info = []
          response.data.forEach(element => {
            this.info.unshift({
              content: element.fields.content,
              time: this.timeStamp(element.fields.createdTime)
            })
          });
          this.$forceUpdate()
          console.log(this.info)
        }
      )
  },
  methods: {
    posting(){
    this.axios
      .get('https://api.itsinghua.top/article/article-create/', {
        params: {
          'secret_key': 'record',
          content: this.content
        }
      })
      .then(() => 
        {
          // this.mounted();
          // this.info = response;
          this.$router.go(0);
        }
      )
    },
 popNotice() {
        let user = '你'
        let content = '填写记录'
        let that = this;
        if (Notification.permission == "granted") {
          let notification = new Notification(user, {
            body: content,
          });
 
          notification.onclick = function() {
            that.$nextTick(() => {
              setTimeout(()=>{
                //具体操作
              },500);
            });
            //可直接打开通知notification相关联的tab窗
            window.focus();
            notification.close();
          };
        }
      },


timeStamp(data) {
        var currentTime = Math.round((new Date()).valueOf());
        var nowTime = new Date(currentTime);
        var provideTime = data * 1000;
        var provideDate = new Date(provideTime);
        // 当前时间转换
        var nowY = nowTime.getFullYear();
        var nowM = nowTime.getMonth() + 1;
        var nowD = nowTime.getDate();
        //获取时间转换
        var proY = provideDate.getFullYear();
        var proM = provideDate.getMonth() + 1;
        var proD = provideDate.getDate();

        // 转换时间样式
        var Y = provideDate.getFullYear() + '-';
        var M = (provideDate.getMonth() + 1 < 10 ? '0' + (provideDate.getMonth() + 1) : provideDate.getMonth() + 1) + '-';
        var D = (provideDate.getDate() < 10 ? '0' + provideDate.getDate() : provideDate.getDate()) + ' ';
        var h = (provideDate.getHours() < 10 ? '0' + provideDate.getHours() : provideDate.getHours()) + ':';
        var m = provideDate.getMinutes() < 10 ? '0' + provideDate.getMinutes() : provideDate.getMinutes();
        var weekend = provideDate.getDay();
        switch (weekend){
            case 1 :
                weekend = "星期一";
                break;
            case 2 :
                weekend = "星期二";
                break;
            case 3 :
                weekend = "星期三";
                break;
            case 4 :
                weekend = "星期四";
                break;
            case 5 :
                weekend = "星期五";
                break;
            case 6 :
                weekend = "星期六";
                break;
            case 0 :
                weekend = "星期日";
                break;
        }
        var time;
        if(currentTime >= provideTime){
            if(nowY <= proY){
                if(nowM <= proM){
                    if(nowD <= proD){
                         time = h + m;
                    }else if(nowD - proD >= 1 && nowD - proD < 2){
                         time = "昨天 " + h + m;
                    }else if(nowD - proD >= 2 && nowD - proD < 7){
                         time = weekend + " " + h + m;
                    }else {
                         time = M + D + h + m;
                    }
                }else {
                    time = M + D + h + m;
                }
            }else {
                time = Y + M + D + h + m;
            }
        }else {
            time = h + m;
        }
        return time;
    }
  },
}
</script>
