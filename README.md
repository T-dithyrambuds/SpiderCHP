# spider
## 1.项目介绍
根据开放接口爬取 情话、朋友圈文案、毒鸡汤，通过与本地数据库内容对比，去重后存储到数据库

## 2.创建数据库
```
sqlite3 homework.db
create table  mywork (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    type varchar(255), 
    item varchar(255)
    )
```

## 3.项目依赖包以及安装
```
pip install requests
pip install sqlite3
```

## 4.如何使用
` python spider.py `


## 5.引用申明
数据来源 https://shadiao.app 已获取作者授权