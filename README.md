抖音web直播间([live.douyin.com](https://live.douyin.com))弹幕抓取
--

改版后，运行步骤：

1. 下载edge浏览器的**webDriver**驱动，
   下载路径：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    下载后在{ **/config/settings.yml** }，配置**webdriver - edge**的路径，直接放在运行目录，就不用修改配置文件
3. 使用 [ **requirements.txt** ] 下的包，新版的**不支持mitmproxy8**，只**支持mitmproxy7**的版本。
4. 新版不需要在额外先启动mitmproxy，直接运行**main.py**就行


**屏幕效果截图**

![enter image description here](https://github.com/FedoraLinux1/douyin_web_live/blob/main/20220519190807.png)

![enter image description here](https://github.com/gll19920817/tiktok_live/blob/main/WX20211129-144919@2x.png?raw=true)

TODO
