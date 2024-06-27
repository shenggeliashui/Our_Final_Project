# final_project
项目源代码结构介绍：
front-end为前端实现代码
back-end为后端实现代码


使用方法：
在开始使用之前，先准备好数据库数据，进入sql文件夹，输入如下命令：
mysql -u root -p < memorized_backup.sql mysql -u root -p < wordapp_backup.sql
然后进入front-end，命令行处输入：
	npm run serve
然后进入back-end，命令行输入：
	python run-all.py
随后点击命令行打印出的网站：
	App running at:
	  - Local:   http://localhost:8080/ 
	  - Network: http://172.26.66.135:8080/
任意进入一个网站即可使用


> A Vue.js project

## 前端文件组成说明：
---src：源代码  
   &emsp; ---assets：图片等  
    &emsp;---components：组件  
         &emsp;&emsp; &emsp;---calendar：日历  
         &emsp;&emsp; &emsp;---site_header:导航栏  
        &emsp;&emsp; &emsp;---Spell:拼写  
        &emsp;&emsp; &emsp;---global.css:全局css,背景和底层文本框  
       &emsp;&emsp; &emsp;---Homepage:首页组件  
      &emsp;&emsp; &emsp;---freeback：反馈页面组件  
    &emsp; ---router：路由配置  
    &emsp; ---view：完整页面的vue文件  
        &emsp; &emsp; &emsp;---frame：框架  
       &emsp; &emsp; &emsp;---FreeBack：客户反馈界面  
        &emsp; &emsp; &emsp;---SpellTenWords：拼写界面  
       &emsp; &emsp; &emsp;---HomeShow:主页  
    &emsp; ---App.vue：根组件  
     &emsp;---main.js：入口  
    

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
