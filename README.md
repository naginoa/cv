# cv比赛

一个校级的cv比赛决赛题目，需要实验，论文和答辩

## 题目

图像识别

现有一15.88cm*15.88cm的正方形图片，每张图片由一个阿拉伯数字和打乱的二维码背景组成。数字于gif图中依次更换，每张图片停留3s。如下图所示：

![](https://github.com/naginoasukara/cv/blob/master/%E8%AF%86%E5%88%AB%E4%BA%8C%E7%BB%B4%E7%A0%81%E4%B8%AD%E7%9A%84%E6%95%B0%E5%AD%97/download.gif)

## 难点

* 处理gif

* 二维码对数字的干扰

## 解决

### 开始思路

想办法去掉图中干扰的二维码

1、二值化

2、一次5，5膨胀

3、删除200以下轮廓

4、第二次5，5膨胀路

结果如图：

![](https://github.com/naginoasukara/cv/blob/master/%E8%AF%86%E5%88%AB%E4%BA%8C%E7%BB%B4%E7%A0%81%E4%B8%AD%E7%9A%84%E6%95%B0%E5%AD%97/image/1.jpg)

### 后来思路

使用模板匹配

opencv中的macthTemplate函数

[模板匹配详情](http://blog.csdn.net/guodongxiaren "悬停显示")
