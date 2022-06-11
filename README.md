# 抖音web直播间([live.douyin.com](https://live.douyin.com))弹幕抓取


> ### 近期工作内容比较繁重，大概率会摸一段时间 (from:q792602257)
> 
> ### 实现功能： 
> 1. 使用新版mitmproxy，使mitmproxy进程跑在主进程里，兼容Python3.10
> 2. 数据无磁盘IO，通过Queue请求传输proto数据，如果对弹幕发送时间要求较高的，可以使用消息对象中的时间 
> 3. 修改输出为组件化，后期通过配置进行启用或禁用，开发者也可以自行编写对应的保存逻辑 
> 4. 自动打开配置的房间及用户首页 
>  
> ### 对其中的修改： 
> 1. 删除了mongo相关内容（以后补吧……，重写一个也不麻烦）  
> 
> ### 待实现功能（咕）： 
> 1. 未开播时，自动刷新页面进行重新检测 
> 2. 下播事件触发及对应动作 
> 3. 上播事件触发及自动打开对应的房间 
> 4. 录播支持 
> 5. 异步输出支持 

### **如何配置**
1. 首先配置`config/settings.yml`中`webdriver.use`将要使用到的浏览器（现仅支持`chrome`及`edge`浏览器）
2. 下载对应浏览器`WebDriver`驱动
   - [Edge浏览器](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
   - [Chrome浏览器](https://chromedriver.chromium.org/downloads "官网下载") [国内镜像](https://registry.npmmirror.com/binary.html?path=chromedriver/ "淘宝镜像")
3. 配置`WebDriver`驱动可执行文件目录
   - Edge浏览器请配置于`webdriver.edge.bin`
   - Chrome浏览器请配置于`webdriver.chrome.bin`
4. 配置浏览器是否需要无头`headless`模式
   - `webdriver.headless`设置为True，浏览器打开后不会显示窗口，适合Linux服务器等无需显示的情况
   - `webdriver.headless`设置为False，浏览器打开后会显示窗口，更适合需要自己手动操作浏览器等其他需要显示情况
5. 配置输出插件(`output.use`)，可以自由搭配使用
   - `print`：控制台打印的组件，收到弹幕信息会在控制台中输出
   - `xml`：B站弹幕姬相兼容的弹幕格式，适用于后期与视频叠加或分析
   - `debug`：开发或测试使用，会保存所有未处理的消息类型，及保留报错信息，方便后期维护排查
6. 配置默认需要打开的房间及用户主页
   - `live.rooms`: 填写房间号（链接地址最后一串数字），或者完整链接地址
   - `live.users`: 填写用户加密ID（用户首页链接地址最后一串字符串），或者完整链接地址 *（暂无任何用途）*

## 运行步骤：

1. 安装依赖 `pip install -r requirements.txt`
2. 按照上述步骤进行配置
3. 运行`main.py`


## **屏幕效果截图**

![enter image description here](https://github.com/FedoraLinux1/douyin_web_live/blob/main/20220519190807.png)

![enter image description here](https://github.com/gll19920817/tiktok_live/blob/main/WX20211129-144919@2x.png?raw=true)


