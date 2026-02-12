# low_quality_preview.py
# 要求：pip install pillow   （你的环境如果没有 Pillow，先安装）

from PIL import Image
import os

# ====================== 配置区 ======================
input_root = r"./"          # 替换成你的图片根目录
quality = 30                                   # 0~100，值越小文件越小、画质越差，建议 25~45
max_size = (800, 800)                          # 长宽最大不超过这个尺寸（等比例缩放）
extensions = ('.jpg', '.jpeg', '.png')        # 只处理这些后缀
output_suffix = "_low"                         # 生成的文件名后缀，例如 原图.jpg → 原图_low.jpg
# ====================================================

def process_image(filepath):
    try:
        with Image.open(filepath) as img:
            # 转 RGB（避免 PNG 带透明通道问题）
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')

            # 等比例缩放到 max_size 内
            img.thumbnail(max_size)

            # 生成输出路径（同目录，换后缀）
            base, ext = os.path.splitext(filepath)
            out_path = f"{base}{output_suffix}{ext}"

            # 保存低质量版本
            img.save(out_path, 'JPEG', quality=quality, optimize=True)
            print(f"生成低画质版：{out_path}")
    except Exception as e:
        print(f"处理失败 {filepath} : {e}")


# 递归遍历文件夹
for root, dirs, files in os.walk(input_root):
    for file in files:
        if file.lower().endswith(extensions):
            full_path = os.path.join(root, file)
            process_image(full_path)

print("全部处理完成！")