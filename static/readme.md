# 数控机3代 PCB板
## 步进电机
### 原理图部分

> ![原理图](/assets/yuanlitu.jpg){:width="700" height="598"} ![原理图1](/assets/yuanlitu1.jpg){:width="700" height="598"}

> RP1 电位器用电阻替换.标识好点.可能要调

> DRV8825发热严重.要求再8825芯片下的位置开个圆孔.以便填锡增加散热效果

> +24的电源部分用 DC接口![DC接口](/assets/dc.jpg){:width="80" height="80"}输入即可 

> VCC用插针.可以外部输入.

> S1 部分采用 2.54 的插针(因为用跳线帽跳选,脚位位置不能变)

> AOUT1,AOUT2,BOUT1,BOUT2 直接连接到边缘留过孔可以焊线,线比较粗.这几根线在PCB上也画粗点

> 18,27 脚留焊盘出来可以焊接即可

> 

> [DRV8825 datasheet](/assets/DRV88_datasheet.pdf)
> [黄工画的PCB文件](/assets/ad.PCB)

## PCB板子
> 3组 8825,一个电源系统.电源12V转3.3v和5v

[markdown 教程][gcssloop]{:target="_blank"}
[gcssloop]: https://www.gcssloop.com/markdown/markdown-links "点击访问markdown 教程"