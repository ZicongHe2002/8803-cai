import json

# 原始数据集文件路径
input_file = "bias_data.json"

# 输出数据集文件路径
output_file = "bias_dataset.json"

# 加载 JSON 数据
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

updated_data = []
for item in data:
    updated_item = {
        "instruction": "judge bias",  # 添加 instruction 字段
        "input": item["input"],       # 保留 input
        "output": item["output"]      # 保留 output
    }
    updated_data.append(updated_item)

# 保存修改后的数据
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(updated_data, f, indent=4, ensure_ascii=False)

print(f"数据集已添加 instruction 字段并调整顺序，保存到 {output_file}")