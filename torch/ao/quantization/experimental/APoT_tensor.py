import torch
from torch import Tensor

# test1.3

# class to store APoT quantized tensor
class TensorAPoT(torch.Tensor):
    @staticmethod
    def quantize_APoT(tensor2quantize: Tensor) -> Tensor:
        raise NotImplementedError

    def dequantize(self) -> Tensor:
        raise NotImplementedError

    def q_apot_alpha(self) -> float:
        raise NotImplementedError

# test1.1 test1.1
