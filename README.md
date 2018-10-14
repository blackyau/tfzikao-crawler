# tfzikao-crawler

四川自考网 Python爬虫 ,用于爬取历年试题的链接和试题名称

## 依赖

[```Python 3```](https://www.python.org/downloads/)

``` pip install requests```

``` pip install pandas```

``` pip install beautifulsoup4```

## 运行

``` git clone https://github.com/blackyau/tfzikao-crawler.git ```

或 下载源码 https://github.com/blackyau/tfzikao-crawler/archive/master.zip

下载完毕后在项目文件夹内运行 ``` python get.py ``` 后会在运行目录内生成 ```tfzikaoDATA.csv``` ,使用 EXCEL 打开中文会乱码请自行查找解决方法或使用[现代文本编辑器](https://code.visualstudio.com/)打开该文本

![](https://i.loli.net/2018/10/14/5bc3045c6395f.jpg)

## 说明

默认抓取 [理工类专业](http://www.tfzikao.com/xlks/lnst/gxlzy/) 的历年试题,你可以修改 ```get.py``` [第7行](https://github.com/blackyau/tfzikao-crawler/blob/master/get.py#L7)的 url 变量为你需要对应专业的试题

默认抓取前 132 页的内容,你可以修改 ```get.py``` [第31行](https://github.com/blackyau/tfzikao-crawler/blob/master/get.py#L31)的数字为你 期望的页数+1 

公共课真题 ```http://www.tfzikao.com/xlks/lnst/ggkzt/```

经济类专业 ```http://www.tfzikao.com/xlks/lnst/jjxzy/```

法学类专业 ```http://www.tfzikao.com/xlks/lnst/fxlzy/```

文学类专业 ```http://www.tfzikao.com/xlks/lnst/wxlzy/```

理工类专业 ```http://www.tfzikao.com/xlks/lnst/gxlzy/```

教育类专业 ```http://www.tfzikao.com/xlks/lnst/jyl/```

管理类专业 ```http://www.tfzikao.com/xlks/lnst/gllzy/```

农学类专业 ```http://www.tfzikao.com/xlks/lnst/nxlzy/```

医学类专业 ```http://www.tfzikao.com/xlks/lnst/yxlzy/```

其它类 ```http://www.tfzikao.com/xlks/lnst/qtl/```

# TODO

- 自动获得总页数
- 交互式选择不同的专业的历年试题
- 优化代码