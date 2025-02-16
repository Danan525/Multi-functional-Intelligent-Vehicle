import torch
import onnx

model = torch.load('best.pt')

input_shape = (1, 3, 224, 224)
dummy_input = torch.randn(input_shape)

#导出onnx
output_path = 'best.onnx'
torch.onnx.export(model, dummy_input, output_path)