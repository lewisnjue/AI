import torch
def train_one_epoch(model, dataloader, optimizer, criterion, device):
    """
    this function is used to train a model for one epoch 
    """
    model.train()
    total_loss = 0
    for batch in dataloader:
        inputs, targets = batch
        inputs, targets = inputs.to(device), targets.to(device) # putting input and target to the device . this is not a tensor you so it return new memory pointer to device 

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets) # creterion is the loss function 

        # Backward pass
        optimizer.zero_grad()  # make gradient of parameter zero 
        loss.backward() # deposite new gradients
        optimizer.step() # update parameters 

        total_loss += loss.item() # since loss is a single item tenor 
    return total_loss / len(dataloader)

def evaluate(model, dataloader, criterion, device):
    """
    this funciton is used to eveluate the model 
    """
    model.eval() # putting model in evaluation face useful for things like normalization layers 
    total_loss = 0
    with torch.no_grad(): # dont do aditional computation since i will not bec calling loss.backwards 
        for batch in dataloader:
            inputs, targets = batch
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            total_loss += loss.item()
    return total_loss / len(dataloader)
