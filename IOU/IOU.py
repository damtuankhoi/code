def iou(box1, box2):

    xi1 = max(box1[0], box2[0])
    yi1 = max(box1[1], box2[1])
    xi2 = min(box1[2], box2[2])
    yi2 = min(box1[3], box2[3])
    inter_area = (yi2 - yi1) * (xi2 - xi1)

    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union_area = box1_area + box2_area - inter_area

    # compute the IoU
    print(box1_area,box2_area,inter_area,union_area)
    iou = inter_area / union_area

    return iou
box1 = (106, 587, 119, 599)
box2 = (121, 364, 137, 389)
print("iou = " + str(iou(box1, box2)))



#     # box1 -- first box, list object with coordinates (x1, y1, x2, y2)
#     # box2 -- second box, list object with coordinates (x1, y1, x2, y2)

# import torch
# import torchvision.ops.boxes as bops

# box1 = torch.tensor([[511, 41, 577, 76]], dtype=torch.float)
# box2 = torch.tensor([[544, 59, 610, 94]], dtype=torch.float)
# iou = bops.box_iou(box1, box2)
# print("iou = " + str(iou))