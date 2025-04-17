class <lambda>(torch.nn.Module):
    def forward(self, arg0_1: "f32[10000]"):
         # File: /workspace/AI/exp/example.py:3 in fn, code: a = torch.cos(x)
        cos: "f32[10000]" = torch.ops.aten.cos.default(arg0_1);  arg0_1 = None
        
         # File: /workspace/AI/exp/example.py:4 in fn, code: b = torch.sin(a)
        sin: "f32[10000]" = torch.ops.aten.sin.default(cos);  cos = None
        return (sin,)
        