# EqualizeHist_homework

## 方法原理

直方图均衡化是将灰度级映射到更加均匀的分布。

核心公式：
<img src="https://latex.codecogs.com/svg.latex?s_k=T(r_k)=\sum^k_{j=0}p_r(r_j)=\sum^k_{j=0}\frac{n_j}{n}">

通过该公式将每个灰度级进行映射，然后保存图片。

## 实验结果

灰度图效果较明显。

在HSI和RGB空间下效果HSI优于RGB，RGB在一些情景下会改变颜色。
如:
HSI:
<img src="https://raw.githubusercontent.com/Littlebus/EqualizeHist_homework/master/processed/13_hsi.jpg">
和RGB:
<img src="https://raw.githubusercontent.com/Littlebus/EqualizeHist_homework/master/processed/13_rgb.jpg">

并且一些场景下，和背景很接近的区域会被明显放大:

<img src="https://raw.githubusercontent.com/Littlebus/EqualizeHist_homework/master/processed/3_hsi.jpg">
<img src="https://raw.githubusercontent.com/Littlebus/EqualizeHist_homework/master/processed/3_rgb.jpg">

## 需要
- `PyQt5`

## 运行

`python main.py`

在打开的窗口点击选择文件，之后点击均衡化，就会弹出两个窗口，如果是RGB就会弹出RGB均衡和HSI均衡的结果；如果是灰度图就会弹出灰度均衡结果。
