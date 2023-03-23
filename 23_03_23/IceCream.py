from icecream import ic
import math
import torch

ic.configureOutput(prefix='ic depug log : ')
ic.enable()
ic.disable()

var_1=5

def test_func(num):
    num=num**3
    num=math.sqrt(num)
    ic()
    return num

var_2=test_func(var_1)

case_tensor=torch.rand(2,3)

ic(var_1)
ic(var_2)
ic(case_tensor)

