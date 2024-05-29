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

![image-20240528213452457-6903294](https://github.com/Nadia-Chen/FasterRCNN/assets/67884201/e43204e7-d67b-4750-8dd3-902710e7e4e5)

以下是验证集上的mAP曲线：

![image-20240528213415954-6903260](https://github.com/Nadia-Chen/FasterRCNN/assets/67884201/d1ec3900-0a92-4f30-a5aa-b7900324ea5b)


## 实验结果

### 测试集上的预测结果

从VOC 2007验证集中随机挑选4张图像进行预测，结果如下：

- 图像1预测结果：

![1](https://github.com/Nadia-Chen/FasterRCNN/assets/67884201/410f8904-8eeb-43f0-8bc0-beda24e5d4ca)


- 图像2预测结果：

![4](https://github.com/Nadia-Chen/FasterRCNN/assets/67884201/3bfda2da-c6a2-4561-a4cd-e15dc939a034)


- 图像3预测结果：
  
![6](https://github.com/Nadia-Chen/FasterRCNN/assets/67884201/c3560628-1545-40dc-bf3b-bfffab2eec9b)

- 图像4预测结果：

![8](https://github.com/Nadia-Chen/FasterRCNN/assets/67884201/47dc53a1-fdaf-4849-8dac-f62b68d32cfe)


### 非VOC数据集图像的预测结果

搜集了三张不在VOC数据集内但包含有VOC中类别物体的图像，预测结果如下：

- 图像1预测结果：

![test_chair](https://github.com/Nadia-Chen/FasterRCNN/assets/67884201/bf22c9cc-9e2a-454a-b195-ae94e7f1ec8a)


- 图像2预测结果：

![test_person2](https://github.com/Nadia-Chen/FasterRCNN/assets/67884201/8b49a071-d1b5-467e-b505-2b6838b2ab19)


- 图像3预测结果：

![test_train](https://github.com/Nadia-Chen/FasterRCNN/assets/67884201/ffcd37ac-c2be-4fde-b515-a7eaab8ed2a4)


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
