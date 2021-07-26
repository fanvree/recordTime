<template>
  <a-layout id="components-layout-demo-top" class="layout">
    <a-layout-header>
      <a-menu
        theme="dark"
        mode="horizontal"
        :defaultSelectedKeys="['1']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1" @click="ChooseMenu = 1">时间轴</a-menu-item>
        <a-menu-item key="2" @click="ChooseMenu = 2">日历</a-menu-item>
      </a-menu>
    </a-layout-header>


    <!-- 对话框 -->
    <a-layout-content style="padding: 0 50px" v-if="ChooseMenu == 1">
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
          <!-- <a-switch checked-children="定时通知" un-checked-children="关闭通知" default-checked/> -->
      <a-row type="flex" justify="space-around" align="middle">
        <a-col :span="12">
          <a-button type="primary" :style="{margin: '10px 0px 0px 0px'}" @click="posting">
          提交
          </a-button>
        </a-col>
        <!-- <a-col :span="8">
          <a-button type="primary" :style="{margin: '10px 0px 0px 0px'}" @click="posting">
          提交
          </a-button>
        </a-col> -->
        <a-col :span="6" style="text-align:right" v-if="!isMobile">
          <div :style="{margin: '10px 0px 0px 0px'}">
            每隔
          <a-input-number id="inputNumber" v-model="value" :min="1" :max="100000" @change="onChange" :disabled="!onNotice" @pressEnter="inputBlur" @blur="sendTips"/>
          分钟通知
          </div>
        </a-col>
        <a-col :span="isMobile?12:6" style="text-align:right">
          <!-- <div> -->

          <div style="font-size: 30px">
          <a-switch checked-children="定时通知" un-checked-children="关闭通知" default-checked
          @change="onClickSwitch"/>
          </div>
        </a-col>
      </a-row>
      </div>
    </a-layout-content>


  <!-- 日历 -->
    <a-layout-content style="padding: 0 50px" v-if="ChooseMenu == 2">
      <a-breadcrumb style="margin: 16px 0">
        <a-breadcrumb-item>日历</a-breadcrumb-item>
      </a-breadcrumb>
      <div :style="{ background: '#fff', padding: '24px 24px 24px 24px'}">
            <div
      :style="{
        display: 'inline-block',
        border: '1px solid #d9d9d9',
        borderRadius: '4px',
      }"
    >
        <a-calendar>
          <ul slot="dateCellRender" slot-scope="value" class="events">
            <div v-for="item in getListData(value)" :key="item.content">
              <a-badge :status="item.type" :text="item.content" />
            </div>
          </ul>
          <template slot="monthCellRender" slot-scope="value">
            <!-- <div v-if="getMonthData(value)" class="notes-month">
              <section>{{ getMonthData(value) }}</section>
            </div> -->
            <div v-for="item in getMonthData(value)" :key="item.content">
              <a-badge :status="item.type" :text="item.content" />
            </div>
          </template>
        </a-calendar>
            </div>
      </div>
    </a-layout-content>

    <!-- 时间轴 -->
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
        <a-timeline-item v-for="(item, index) in info" :key="index" @click="clickTimeLineItem(item)" postion = "left">
          <!-- {{item.time}}{{"  " + item.content}} -->
          {{item.time + " "}}<span v-html="item.content"></span>
          <div :style="{height: item.timeHeight + 'px'}"></div>
        </a-timeline-item>
        </a-timeline>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      Record ©2021 Created by Fzr
    </a-layout-footer>


    <!-- <a-drawer
      title="Basic Drawer"
      placement="bottom"
      closable="false"
      :visible="showDrawer"
    >
      <p>Some contents...</p>
      <p>Some contents...</p>
      <p>Some contents...</p>
    </a-drawer> -->
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
      value: 10,
      onNotice: true,
      ChooseMenu: 1, 
      showDrawer: true,
      isMobile: false // 屏幕尺寸
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
      this.timer = setInterval(this.popNotice, 1000*60*10)
      this.isMobile = this._isMobile()
  },
  mounted() {
    this.axios
      .get('https://api.itsinghua.top/article/article-list/', {
        params: {
          owner: this.$route.path.substr(1),
          secret_key: 'record',
        }
      })
      .then(response => 
        {
          this.info = []
          let lasttime = 0
          response.data.forEach(element => {

            if (!this.sameDay(element.fields.createdTime, lasttime)) {
              this.info.unshift({
                position: 'left',
                content: '',
                contentbr: '',
                timeHeight: 0,
                time: this.timeStamp(lasttime),
                createdTime: element.fields.createdTime
              })
            }

            this.info.unshift({
              position: 'right',
              content: element.fields.content,
              contentbr: element.fields.content.replace(/\n/g,"<br/>"),
              timeHeight: this.getTimeHeight(element.fields.createdTime, lasttime),
              time: this.timeStamp(element.fields.createdTime),
              createdTime: element.fields.createdTime
            })
            console.log(this.getTimeHeight(element.fields.createdTime, lasttime))
            lasttime = element.fields.createdTime
          });
          this.$forceUpdate()
          console.log(this.info)
        }
      )
  },
  methods: {
    sameDay(time1, time2) {
      return (new Date(time1 * 1000).toDateString() === new Date(time2 * 1000).toDateString())
    },
    sameMonth(time1, time2) {
      return (new Date(time1 * 1000).getMonth() === new Date(time2 * 1000).getMonth())
    },
    getTimeHeight(time1, time2) {
      if (new Date(time1 * 1000).toDateString() === new Date(time2 * 1000).toDateString()) {
        return 0
      }
      // let timeDis = time1 - time2
      // if (timeDis  < 60 * 15) {
      //   return 0
      // }
      // if (timeDis  < 60 * 60) {
      //   return 10
      // }
      // if (timeDis  < 60 * 60 * 24) {
      //   return 20
      // }
      return 30
    },
    clickTimeLineItem(item) {
      let temp = item.content
      item.content = item.contentbr
      item.contentbr = temp
    },
    onChange(value) {
      clearInterval(this.timer)
      console.log(value)
      // this.value = value
      this.timer = setInterval(this.popNotice, 1000*60*this.value)
      // this.$message.success(
      //   String(value) + "分钟后发送通知",
      //   3,
      // );
    }, 
    inputBlur() {
      var input = document.getElementById("inputNumber");
      input.blur()
    },
    sendTips() {
      this.$message.success(
        String(this.value) + "分钟后发送通知",
        3,
      );
    },
    onClickSwitch(checked) {
      this.onNotice = checked
      if (checked) {
      this.timer = setInterval(this.popNotice, 1000*60*this.value)
      } else {
      clearInterval(this.timer)
      }
    },
    posting(){
    this.axios
      .get('https://api.itsinghua.top/article/article-create/', {
        params: {
          secret_key: 'record',
          content: this.content,
          owner: this.$route.path.substr(1),
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


 getListData(value) {
      // return 0
      let listData = []
      let count = 0
      this.info.forEach(element => {
            if (this.sameDay(Date.parse(value.toDate())/1000, element.createdTime)) {
              // listData.push({
              //   content: element.content,
              //   type: 'success'
              // })
              count ++
              // this.info.unshift({
              //   position: 'left',
              //   content: '',
              //   contentbr: '',
              //   timeHeight: 0,
              //   time: this.timeStamp(lasttime)
              // })
            }
      })
      if (count > 0)
      listData.push({
                content: '共' + String(count - 1) + "条日志",
                type: 'success'
              })
      return listData || []
      // return [
      //       { type: 'warning', content: value.date() },
      //       { type: 'success', content: value.date() },
      //     ];
      // let listData;
      // switch (value.date()) {
      //   case 8:
      //     listData = [
      //       { type: 'warning', content: 'This is warning event.' },
      //       { type: 'success', content: 'This is usual event.' },
      //     ];
      //     break;
      //   case 10:
      //     listData = [
      //       { type: 'warning', content: 'This is warning event.' },
      //       { type: 'success', content: 'This is usual event.' },
      //       { type: 'error', content: 'This is error event.' },
      //     ];
      //     break;
      //   case 15:
      //     listData = [
      //       { type: 'warning', content: 'This is warning event' },
      //       { type: 'success', content: 'This is very long usual eventddddddddddddddddd' },
      //       { type: 'error', content: 'This is error event 1.' },
      //       { type: 'error', content: 'This is error event 2.' },
      //       { type: 'error', content: 'This is error event 3.' },
      //       { type: 'error', content: 'This is error event 4.' },
      //     ];
      //     break;
      //   default:
      // }
      // return listData || [];
    },

    getMonthData(value) {
      let listData = []
      let count = 0
      this.info.forEach(element => {
            if (this.sameMonth(Date.parse(value.toDate())/1000, element.createdTime)) {
              count ++
            }
      })
      if (count > 0)
      listData.push({
                content: '共' + String(count - 1) + "条日志",
                type: 'success'
              })
      return listData || []
    },



//App.vue
_isMobile() {
  let flag = navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i)
  return flag;
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
