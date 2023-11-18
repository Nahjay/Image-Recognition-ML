""" Create Anime Machine Learning Model """

# Imports
import torch
import torch.nn as nn
import torch.nn.functional as F


# Create Model
class AnimeModel(nn.Module):
    def __init__(self, num_classes):
        super(AnimeCharacterCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * 32 * 32, 128)
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 128 * 64 * 64)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
