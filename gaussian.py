import torch
import torchvision
import numpy as np
import os
from PIL import Image

import torchvision.transforms as transforms

transform = transforms.ToTensor()
testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                      download=True, transform=transform)
save_dir = 'adversarial/gaussian'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

mean = 0
std = [0.05, 0.1, 0.15, 0.2]
std = 0.1

for idx, (image, label) in enumerate(testset):
    noise = torch.randn(image.shape) * std + mean
    noisy_image = image + noise
    noisy_image = torch.clamp(noisy_image, 0, 1)
    noisy_image = transforms.ToPILImage()(noisy_image)
    save_path = os.path.join(save_dir, f'noisy_image_{idx}.png')
    noisy_image.save(save_path)
    
    if idx >= 1000:
        break