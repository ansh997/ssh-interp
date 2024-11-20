import torch
import torchvision
import os
from PIL import Image
import numpy as np
import torchvision.transforms as transforms

save_dir = "adversarial/contrast"
os.makedirs(save_dir, exist_ok=True)

transform = transforms.Compose([
    transforms.ToTensor()
])

testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                      download=True, transform=transform)

def adjust_contrast_brightness(image, contrast_factor=None, brightness_factor=None):
    if contrast_factor is None:
        contrast_factor = np.random.uniform(0.5, 1.5)
    if brightness_factor is None:
        brightness_factor = np.random.uniform(0.5, 1.5)

    image = transforms.functional.adjust_contrast(image, contrast_factor)
    image = transforms.functional.adjust_brightness(image, brightness_factor)
    return image

for idx, (image, label) in enumerate(testset):
    modified_image = adjust_contrast_brightness(image)
    pil_image = transforms.ToPILImage()(modified_image)
    save_path = os.path.join(save_dir, f'image_{idx}_label_{label}.png')
    pil_image.save(save_path)
    if idx >= 1000:
        break