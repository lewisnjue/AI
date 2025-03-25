## why initalze weights close to zero in pytorch? 

when training neural networks, weights intilizatin plays a crucial role in ensuring stable and efficient learning. Randomly initlalzed weights that are too large or too smal can cause problems like: 
1. vanising gradients: 
- if weights are too small, gradients shrink exponentially during backpropagation (eg in deep networks with sigmoid/tanh)
- result: neurons stop learning ("die")

2. exploding gradients: 
- if weights are too large, gradients grow exponentially, calusing unstable updtes. 
- result: model fails to converge. 

3. Dead Neurons(ReLU):
- in ReLu, if weights are intialzed such that pre-activations are negative, gradients become zero (no leanring). 

## common initialzaton methods in pytorch 
pytorch provides built-in methods to avoid thsee issues: 
1. **Xavier/Glorot initization**
- for sigmoid/tanh: 

```py
torch.nn.init.xavier_uniform_(layer.weight)  # Uniform distribution
torch.nn.init.xavier_normal_(layer.weight)   # Normal distribution
```
- scales weith based on input/outpu dimenstiosn 
Var(W) = 2 / (nin + nout)

2. He initlization(For ReLU/Leadky ReLu)

```py
torch.nn.init.kaiming_uniform_(layer.weight, mode='fan_in', nonlinearity='relu')
```
- scales weights by: var(W) = 2/ nin

3. Small Random Values 
```py
torch.randn(layer.weight.shape) * 0.01  # Small Gaussian noise
```

example:proper initlaiztin in pytorch 

```py
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 10)

        # Initialize weights
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.kaiming_normal_(self.fc2.weight, mode='fan_in', nonlinearity='relu')

        # Initialize biases to zero
        nn.init.zeros_(self.fc1.bias)
        nn.init.zeros_(self.fc2.bias)
```
