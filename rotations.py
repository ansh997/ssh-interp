import torch
import torchvision
from PIL import Image
import os
import numpy as np
from torchvision.transforms import functional as F

import torchvision.transforms as transforms

save_dir = 'adversarial/rotations'
os.makedirs(save_dir, exist_ok=True)
transform = transforms.Compose([
    transforms.ToTensor()
])
testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                      download=True, transform=transform)

rotation_angles = [0, 90, 180, 270]


for idx, (image, label) in enumerate(testset):
    img = transforms.ToPILImage()(image)
    class_dir = os.path.join(save_dir, str(label))
    os.makedirs(class_dir, exist_ok=True)

    for angle in rotation_angles:
        rotated_img = F.rotate(img, angle)
        save_path = os.path.join(class_dir, f'img_{idx}_rot_{angle}.png')
        rotated_img.save(save_path)
    
    if idx >= 1000:
        break