# import mmcv
# from mmdet.apis import init_detector, inference_detector
# import numpy as np
# import matplotlib.pyplot as plt
# import cv2

# # 配置文件和模型权重文件路径
# config_file = 'configs/faster_rcnn/my_faster_rcnn_voc.py'
# checkpoint_file = 'work_dirs/my_faster_rcnn_voc/epoch_11.pth'

# # 初始化模型
# model = init_detector(config_file, checkpoint_file, device='cuda:0')

# # 类别名称
# # class_names = ['train','person','dog','chair']

# def draw_boxes(img, boxes, scores=None, labels=None, class_names=None, score_thr=0.5):
#     for i, box in enumerate(boxes):
#         if scores is not None and scores[i] < score_thr:
#             continue
#         left_top = (int(box[0]), int(box[1]))
#         right_bottom = (int(box[2]), int(box[3]))
#         cv2.rectangle(img, left_top, right_bottom, (0, 255, 0), thickness=2)
#         if labels is not None and class_names is not None:
#             label_text = class_names[labels[i]]
#             if scores is not None:
#                 label_text += f'|{scores[i]:.02f}'
#             cv2.putText(img, label_text, (int(box[0]), int(box[1] - 2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
#     return img

# test_images = [
#     'data/VOCdevkit/VOC2007/JPEGImages/000001.jpg',
#     'data/VOCdevkit/VOC2007/JPEGImages/000002.jpg',
#     'data/VOCdevkit/VOC2007/JPEGImages/000003.jpg',
#     'data/VOCdevkit/VOC2007/JPEGImages/000004.jpg'
# ]

# for img_path in test_images:
#     img = mmcv.imread(img_path)
    
#     # 获取proposal boxes
#     x = model.extract_feat(img)
#     rpn_outs = model.rpn_head(x)
#     proposal_cfg = model.test_cfg.rpn
#     proposals = model.rpn_head.get_bboxes(*rpn_outs, img_metas=[[{'img_shape': img.shape, 'scale_factor': 1.0}]], cfg=proposal_cfg)
#     proposal_boxes = proposals[0][0][:, :4].cpu().numpy()
    
#     # 绘制proposal boxes
#     img_proposals = img.copy()
#     img_proposals = draw_boxes(img_proposals, proposal_boxes, score_thr=0.5)
#     proposal_output_path = img_path.replace('.jpg', '_proposals.jpg')
#     mmcv.imwrite(img_proposals, proposal_output_path)
    
#     # 获取最终预测结果
#     result = inference_detector(model, img)
    
#     # 绘制最终预测结果
#     bbox_result, segm_result = result if isinstance(result, tuple) else (result, None)
#     bboxes = np.vstack(bbox_result)
#     labels = [
#         np.full(bbox.shape[0], i, dtype=np.int32)
#         for i, bbox in enumerate(bbox_result)
#     ]
#     labels = np.concatenate(labels)
#     img_result = img.copy()
#     img_result = draw_boxes(img_result, bboxes, scores=bboxes[:, 4], labels=labels, score_thr=0.5)
#     result_output_path = img_path.replace('.jpg', '_result.jpg')
#     mmcv.imwrite(img_result, result_output_path)

# def display_image(image_path, title):
#     img = cv2.imread(image_path)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     plt.figure(figsize=(10, 10))
#     plt.imshow(img)
#     plt.title(title)
#     plt.axis('off')
#     plt.show()

# for img_path in test_images:
#     proposal_output_path = img_path.replace('.jpg', '_proposals.jpg')
#     result_output_path = img_path.replace('.jpg', '_result.jpg')
    
#     display_image(proposal_output_path, 'Proposal Boxes')
#     display_image(result_output_path, 'Final Prediction')


from mmdet.apis import init_detector, inference_detector
from mmdet.registry import VISUALIZERS
import cv2
import mmcv
import torch
import pdb

config_file = 'configs/faster_rcnn/my_faster_rcnn_voc.py'
checkpoint_file = 'work_dirs/my_faster_rcnn_voc/epoch_11.pth'
# checkpoint_file = '/data/lina_new/faster/mmdetection/rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth'

model = init_detector(config_file, checkpoint_file, device=torch.device('cuda:0'))
visualizer = VISUALIZERS.build(model.cfg.visualizer)
visualizer.dataset_meta = model.dataset_meta

import os
base = './test_pic/'
# file_name = []
for _,_,files in os.walk(base):
    print(files)
    # file_name.append(file)

for file in files:
    pic = base+file
    img = cv2.imread(pic)

    result = inference_detector(model, img)
    # pdb.set_trace()
    img = mmcv.imconvert(img, 'bgr', 'rgb')
    visualizer.add_datasample(
        name='result',
        image=img,
        data_sample=result,
        draw_gt=False,
        pred_score_thr=0.3,
        show=False)

    img = visualizer.get_image()
    img = mmcv.imconvert(img, 'bgr', 'rgb')
    cv2.imwrite(f'{base}test_{file}', img)

    cv2.waitKey(0)
    print(f'{base}test_{file}:over!')