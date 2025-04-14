""" this file prepares your dataset and dataloader """
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms

def get_dataset():
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    train_dataset = datasets.MNIST(root="data", train=True, transform=transform, download=True)
    val_dataset = datasets.MNIST(root="data", train=False, transform=transform)
    return train_dataset, val_dataset
