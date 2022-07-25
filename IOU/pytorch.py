import numpy as np
import torch

tensor_cpu = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], device='cpu')
tensor_cpu = tensor_cpu * 5
print(tensor_cpu)
