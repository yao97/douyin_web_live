# 抖音web直播间([live.douyin.com](https://live.douyin.com))弹幕抓取


## 近期工作内容比较繁重，大概率会摸一段时间 (from:q792602257)

## 实现功能： 
 1. 使用旧版（7.0.4）的mitmproxy，使mitmproxy进程跑在主进程里（主要是Queue这种方式需要） 
 2. 数据无磁盘IO，通过Queue请求传输proto数据，如果对弹幕发送时间要求较高的，可以使用消息对象中的时间 
 3. 修改输出为组件化，后期通过配置进行启用或禁用，开发者也可以自行编写对应的保存逻辑 
 4. 自动打开配置的房间及用户首页 
 
## 对其中的修改： 
1. 删除了mongo相关内容（以后补吧……，重写一个也不麻烦）  

## 待实现功能（咕）： 
1. 未开播时，自动刷新页面进行重新检测 
2. 下播事件触发及对应动作 
3. 上播事件触发及自动打开对应的房间 
4. 修改README 
5. 录播支持 
6. 异步输出支持 


## 改版后，运行步骤：

1. 下载edge浏览器的**webDriver**驱动：
   - 下载地址：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   - 下载后在{ **/config/settings.yml** }，配置**webdriver - edge**的路径，直接放在运行目录，就不用修改配置文件
3. 使用 [ **requirements.txt** ] 下的包，新版的**不支持mitmproxy8**，只**支持mitmproxy7**的版本。
4. 新版不需要在额外先启动mitmproxy，直接运行**main.py**就行


## **屏幕效果截图**

![enter image description here](https://github.com/FedoraLinux1/douyin_web_live/blob/main/20220519190807.png)

![enter image description here](https://github.com/gll19920817/tiktok_live/blob/main/WX20211129-144919@2x.png?raw=true)


