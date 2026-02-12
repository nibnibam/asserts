# 文件名：move_low_to_separate_dir_keep_structure.py
# 功能：把所有 _low.* 文件移动到新的根目录 low_quality 下，保持原相对路径结构

import os
import shutil
from pathlib import Path

# ======================== 配置 ========================
ROOT_DIR = r"./asserts"          # ← 改成你本地 asserts 仓库根路径
NEW_ROOT_NAME = "low_quality"                       # 新根目录名字，会创建在 ROOT_DIR 同级
SUFFIX = "_low"                                     # 低画质后缀（不含扩展名）
EXTENSIONS = ('.jpg', '.jpeg', '.png')              # 处理的后缀
# ========================================================

def main():
    root_path = Path(ROOT_DIR).resolve()
    new_root = root_path.parent / NEW_ROOT_NAME     # 新根目录：仓库同级/low_quality
    new_root.mkdir(exist_ok=True)

    moved_count = 0

    for file_path in root_path.rglob("*"):
        if not file_path.is_file():
            continue

        # 只处理 low 文件
        if not file_path.stem.endswith(SUFFIX):
            continue

        if not file_path.suffix.lower() in EXTENSIONS:
            continue

        # 计算原相对路径
        relative_path = file_path.relative_to(root_path)

        # 新路径：new_root + 相对路径（包含子文件夹）
        new_file_path = new_root / relative_path

        # 创建中间子文件夹
        new_file_path.parent.mkdir(parents=True, exist_ok=True)

        # 移动文件
        try:
            shutil.move(str(file_path), str(new_file_path))
            print(f"移动: {relative_path} → {NEW_ROOT_NAME}/{relative_path}")
            moved_count += 1
        except Exception as e:
            print(f"移动失败 {relative_path}: {e}")

    print(f"\n完成！共移动 {moved_count} 个低画质文件到：")
    print(new_root)

if __name__ == "__main__":
    main()