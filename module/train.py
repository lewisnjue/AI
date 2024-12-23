""" this script parses command-line arguments , initializes everyting and runs training  """

import argparse
import torch
from torch.utils.data import DataLoader
from model import SimpleModel
from engine import train_one_epoch, evaluate
from datasets import get_dataset  # Assume this function exists in datasets.py

def main(args):
    # Set up device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load data
    train_dataset, val_dataset = get_dataset()
    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size)

    # Initialize model
    model = SimpleModel(input_size=28*28, hidden_size=128, output_size=10).to(device)

    # Define optimizer and loss
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
    criterion = torch.nn.CrossEntropyLoss()

    # Training loop
    for epoch in range(args.num_epochs):
        train_loss = train_one_epoch(model, train_loader, optimizer, criterion, device)
        val_loss = evaluate(model, val_loader, criterion, device)

        print(f"Epoch [{epoch+1}/{args.num_epochs}], Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}")

    # Save the model
    torch.save(model.state_dict(), f"{args.model}.pth")
    print(f"Model saved as {args.model}.pth")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a PyTorch model")
    parser.add_argument("--model", type=str, required=True, help="Name of the model")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size")
    parser.add_argument("--lr", type=float, default=0.001, help="Learning rate")
    parser.add_argument("--num_epochs", type=int, default=10, help="Number of epochs")
    args = parser.parse_args()

    main(args)
