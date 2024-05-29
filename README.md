# Faster R CNN目标检测模型在VOC数据集上的训练与测试报告

## 引言

本报告旨在展示使用MMDetection框架在VOC数据集上训练Faster R CNN目标检测模型的过程。我们将介绍所用模型和数据集的基本信息，详细描述实验设置，并展示实验结果，包括训练过程中的损失和验证集上的mAP曲线、测试集上的预测结果和一些来自VOC数据集外的图像的预测结果。

## 模型介绍

Faster R-CNN是一种流行的目标检测模型，它通过整合区域生成和目标分类两大任务，实现了高效的目标检测。Faster R-CNN的主要组成部分有：卷积神经网络 (CNN)、区域建议网络 (Region Proposal Network, RPN)、ROI Pooling（区域兴趣池化）、ROI Pooling使用最大池化（max pooling）、分类和边界框回归。

## 数据集介绍

PASCAL VOC 2012数据集是一个广泛使用的目标检测数据集，包含20个类别的目标。数据集分为训练集和验证集，分别包含5717张和5823张图像。

## 实验设置

### 训练测试集划分

- 训练集：VOC 2007训练集
- 验证集：VOC 2007验证集
- 测试集：从VOC 2007验证集中随机挑选4张图像进行测试；从非VOC数据集的图片中挑选3张进行测试。

### 超参数设置

- Batch size：8
- Learning rate：0.001
- 优化器：SGD（动量0.9，权重衰减0.0005）
- 训练周期（epochs）：12
- 损失函数：CrossEntropyLoss
- 评价指标：mAP（mean Average Precision）

### 环境设置

- 软件：Python 3.8.19，PyTorch 1.10.0+cu113，mmcv 2.0.0，mmdet 3.3.0，mmengine  0.10.4



## 实验过程

### 训练过程

使用MMDetection库进行训练

### 训练过程的可视化

使用Tensorboard进行训练过程中损失和mAP曲线的可视化。以下是训练集上的loss曲线：

![image-20240528213452457](Faster%20R%20CNN%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E5%9C%A8VOC%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8A%E7%9A%84%E8%AE%AD%E7%BB%83%E4%B8%8E%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A_images/image-20240528213452457-6903294.png)

以下是验证集上的mAP曲线：

![image-20240528213415954](Faster%20R%20CNN%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E5%9C%A8VOC%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8A%E7%9A%84%E8%AE%AD%E7%BB%83%E4%B8%8E%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A_images/image-20240528213415954-6903260.png)

## 实验结果

### 测试集上的预测结果

从VOC 2007验证集中随机挑选4张图像进行预测，结果如下：

- 图像1预测结果：

  ![图像1预测结果](Faster%20R%20CNN%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E5%9C%A8VOC%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8A%E7%9A%84%E8%AE%AD%E7%BB%83%E4%B8%8E%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A_images/1.jpg)

- 图像2预测结果：

  ![](Faster%20R%20CNN%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E5%9C%A8VOC%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8A%E7%9A%84%E8%AE%AD%E7%BB%83%E4%B8%8E%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A_images/4.jpg)

- 图像3预测结果：

  ![](Faster%20R%20CNN%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E5%9C%A8VOC%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8A%E7%9A%84%E8%AE%AD%E7%BB%83%E4%B8%8E%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A_images/6.jpg)

- 图像4预测结果：

  ![](Faster%20R%20CNN%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E5%9C%A8VOC%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8A%E7%9A%84%E8%AE%AD%E7%BB%83%E4%B8%8E%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A_images/8.jpg)

### 非VOC数据集图像的预测结果

搜集了三张不在VOC数据集内但包含有VOC中类别物体的图像，预测结果如下：

- 图像1预测结果：

  ![](Faster%20R%20CNN%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E5%9C%A8VOC%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8A%E7%9A%84%E8%AE%AD%E7%BB%83%E4%B8%8E%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A_images/test_chair.jpg)

- 图像2预测结果：

  ![](Faster%20R%20CNN%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E5%9C%A8VOC%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8A%E7%9A%84%E8%AE%AD%E7%BB%83%E4%B8%8E%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A_images/test_person2.jpg)

- 图像3预测结果：

  ![](Faster%20R%20CNN%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%A8%A1%E5%9E%8B%E5%9C%A8VOC%E6%95%B0%E6%8D%AE%E9%9B%86%E4%B8%8A%E7%9A%84%E8%AE%AD%E7%BB%83%E4%B8%8E%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A_images/test_train.jpg)

## 结论

本次实验通过使用MMDetection框架，成功在VOC数据集上训练了Faster R CNN目标检测模型，并验证了其在不同图像上的检测效果。通过可视化训练过程中的损失和mAP曲线，可以观察到模型逐渐收敛，并在验证集上取得了较好的性能。测试集和非VOC数据集图像的预测结果也证明了模型的泛化能力。

## 未来工作

未来可以尝试以下方向以提升模型性能：

1. 数据增强：增加训练数据的多样性，提高模型的鲁棒性。
2. 超参数优化：通过网格搜索或贝叶斯优化等方法找到更优的超参数设置。
3. 跨域验证：在不同的数据集上验证模型的泛化能力，如COCO、Cityscapes等。

通过以上改进措施，有望进一步提升目标检测模型的性能和应用价值。

模型链接：链接: https://pan.baidu.com/s/1FS3T7QGexyE_E7Sa6O_zTA?pwd=1234 提取码: 1234

仓库链接：https://github.com/PengChenghao1013/neural_network_mid
