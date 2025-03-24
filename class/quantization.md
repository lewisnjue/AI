## quantization in deep learning 

quantization is a technique used to  make deep learing models faster and more efficient by reduincg the numerical precision of their weights and activatiosn, instead fo using high-precision floating point number like 32-bit float32 quantization converts them into lower precision formats like int8  thies leads to: 

- smaller models sizze (eg x reduction with int8 vs float32)
- faster computation (since interger math is faster on most hardware)
- lower memory bandwidth usage(helpful for edge devices like smartphones)


## how quantization works 

1. Floating-point vs Qantized models. 
- floating point model: uses 32 bit nubmers for weights and activations (high precision, but slow and memory heavy)
- quantized(int8) model: uses 8-bit integers (lower precision, but much faster and smaller)


2. key concepts in quantization: 
*quantization process*
1. scale & zero-point calculation
- floating piint nubmers are mapped to integers 

```
Quantized Value=Round( fp32 value/ scale)+Zero-Point

 ```
- scale = (max_value - min_value) / (quant_max - quant_min) eg for int8 , quant_max = 127, quanti_min = -128 

- zero-point = an integer bias to ensrue 0 in float maps to 0 in quantized form. 
2. deqantization(reverse process)

- converts integers back to approximate floating-point values: 

fp32 ~= (antized value - zero-point) * scale 


*type of quantization*

1. dynamic quantization 

- only weights are quantized ahead of time 
- activatiosn are quantized on-the-fly during inference. 
- best for modles like LSTMs and Transformers (where weights loading is the bottleneck). 

2. static quantization
- both weight and activatiosn are quantized. 
- requres a calibation step( running samples data to determine optimal scale/zero-point)
- best for CNNs(where both compute and memory matter)


3. Qauntization-awre Training(QAT)
- simulates quantization during traning (using fake quantization)
- produces more accurate quantized modesl than post-training methods. 


## quantizatin in pytorch 

pytorch supports three main approaches: 
**Eager model quantization (Manual,Beta)**
- user manually specifiesr where quantization happends. 
- supports modules (not functional ops)
**FX Graph mode Quantization (automatic , maintenance mode)**
- automates quantization but requres model compatibility with torch.fx 

**pytorch 2 export Quantization(new, recommended)**
- uses torch.export for better model capture 
- more flexible and works with more models. 


*example: Dynamic quantiztion in pytorch* 


```py 
import torch 
model = torch.nn.Linear(4,4)

# cnvert in INT* (dynamic quantizatin)

quantized_model = torch.quantization.quantize_dynamic(model,
{torch.nn.Linear}, dtype=torch.qint8
)

# now runs in INT*! 
input = torch.randn(1,4)
output = quantized_model(input)

```
