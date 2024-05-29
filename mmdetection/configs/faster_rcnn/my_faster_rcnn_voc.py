_base_ = [
    '../_base_/models/faster-rcnn_r50_fpn.py',
    '../_base_/datasets/voc0712.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
# _base_.visualizer.vis_backends = [
#     dict(type='LocalVisBackend'), #
#     dict(type='TensorboardVisBackend')
#     ]

model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=20)))  # VOC数据集有20个类别

# 修改数据路径
data = dict(
    train=dict(
        type='RepeatDataset',
        times=3,
        dataset=dict(
            type='VOCDataset',
            ann_file=[
                'data/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt'
            ],
            img_prefix=[
                'data/VOCdevkit/VOC2007/'
            ])),
    val=dict(
        type='VOCDataset',
        ann_file='data/VOCdevkit/VOC2007/ImageSets/Main/val.txt',
        img_prefix='data/VOCdevkit/VOC2007/'),
    test=dict(
        type='VOCDataset',
        ann_file='data/VOCdevkit/VOC2007/ImageSets/Main/test.txt',
        img_prefix='data/VOCdevkit/VOC2007/'))

log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHook')
    ])

# vis_backends = [
#     dict(type='LocalVisBackend'),
#     dict(type='TensorboardVisBackend')
# ]
# visualizer = dict(
#     type='DetLocalVisualizer', vis_backends=vis_backends, name='visualizer')
# vis_backends = [
#     dict(type='LocalVisBackend'),
#     dict(type='TensorboardVisBackend'),
# ]
# visualizer = dict(
#     name='visualizer',
#     type='DetLocalVisualizer',
#     vis_backends=[
#         dict(type='LocalVisBackend'),
#         dict(type='TensorboardVisBackend'),
#     ])