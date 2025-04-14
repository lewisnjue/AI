import torch.nn as nn
class SimpleModel(nn.Module):
    def __init__(self,input_size,hidden_size,output_size):
        """
        input_size is the fan_in. output_size is the fan_out
        """
        super(SimpleModel,self).__init__()# please dont forget to do this 
        self.fc1 = nn.Linear(input_size,hidden_size)
        self.relu = nn.ReLU()
        self.fc2= nn.Linear(hidden_size,output_size)
    def forward(self, x):
        x = x.view(x.size(0), -1)  # Flatten the input tensor # -1 means it will be cacluated aoutomatically 
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
