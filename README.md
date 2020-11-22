## 上海地理位置爬虫

采用selenium自动化爬取，数据来源[上海本地生活](http://life.city8090.com/shanghai/)

## 数据格式
- **类别**：共十四类，"度假村/度假区", "文化馆/活动中心", "夜总会/娱乐中心", "休闲广场", "购物中心", "电器商场", "超市", "小区", "别墅","办公大厦", "道路名称", "区县", "商圈", "乡镇"
- **数据内容**：包含具体位置名字（name）以及具体地址（address），[示例见此](https://git.mgvai.cn/ai/spider/-/blob/master/data_sample.json)

## hanlp命名实体识别模块
- api调用位置：hanlpAPI.py 参考网址：https://www.hanlp.com/product.html
- github代码位置：hanlp.py 参考网址：https://github.com/hankcs/HanLP

## 文件说明
### 1.爬虫代码
crawler.py
### 2.hanlp的爬取数据识别效果
apiTestResult.json

