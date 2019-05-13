# EqualizeHist_homework

## 方法原理

直方图均衡化是将灰度级映射到更加均匀的分布。

<img src="https://latex.codecogs.com/svg.latex?s_k=T(r_k)=\sum^k_{j=0}p_r(r_j)=\sum^k_{j=0}\frac{n_j}{n}">

## 实验结果

灰度图效果明显。

在HSI和RGB空间下效果HSI优于RGB，RGB在一些情景下会改变颜色。

## 需要
- `PyQt5`

## 运行

`python main.py`
