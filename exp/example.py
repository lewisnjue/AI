import torch
def fn(x):
   a = torch.cos(x)
   b = torch.sin(a)
   return b
device = 'cuda' if torch.cuda.is_available() else 'cpu'
new_fn = torch.compile(fn, backend="inductor")
input_tensor = torch.randn(10000).to(device=device)
a = new_fn(input_tensor)