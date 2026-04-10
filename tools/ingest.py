#!/usr/bin/env python3
"""
Mind Wiki 摄入工具
"""
import os
import sys
from pathlib import Path
from datetime import datetime
import shutil

def ingest_target(target_path=None, all=False, project=False, yes=False):
    """摄入内容"""
    from config import get_current_wiki_path
    
    wiki_path = get_current_wiki_path()
    untracked_dir = wiki_path / "raw" / "untracked"
    ingested_dir = wiki_path / "raw" / "ingested" / datetime.now().strftime("%Y-%m-%d")
    
    # 确定目标路径
    if all:
        targets = list(untracked_dir.iterdir()) if untracked_dir.exists() else []
        if not targets:
            print("❌ 没有待处理的文件")
            return
    elif target_path:
        targets = [Path(target_path).expanduser().resolve()]
    else:
        print("❌ 请指定文件路径或使用 --all")
        return
    
    # 创建已处理目录
    ingested_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📥 开始摄入内容到知识库: {wiki_path.name}")
    print(f"处理日期: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"待处理文件: {len(targets)} 个")
    
    # 打印文件列表
    for i, target in enumerate(targets, 1):
        print(f"  {i}. {target.name}")
    
    # 确认操作
    if not yes:
        confirm = input("\n是否继续？(Y/n) ")
        if confirm.lower() not in ["", "y", "yes"]:
            print("已取消")
            return
    
    # 处理文件
    for target in targets:
        if not target.exists():
            print(f"❌ 文件不存在: {target}")
            continue
        
        # 复制到 untracked 目录（如果不是在那里）
        if not str(target).startswith(str(untracked_dir)):
            dest = untracked_dir / target.name
            if target.is_dir():
                shutil.copytree(target, dest)
            else:
                shutil.copy2(target, dest)
            target = dest
        
        # 移动到已处理目录
        dest = ingested_dir / target.name
        if dest.exists():
            # 如果已存在，重命名
            base = dest.stem
            ext = dest.suffix
            counter = 1
            while dest.exists():
                dest = ingested_dir / f"{base}_{counter}{ext}"
                counter += 1
        
        shutil.move(str(target), str(dest))
        print(f"✅ 已处理: {target.name} → {dest.name}")
    
    print(f"\n🎉 摄入完成！")
    print(f"已处理文件保存在: {ingested_dir}")
    print("\n接下来 AI 会分析内容并生成概念页面和解读。")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="摄入内容到知识库")
    parser.add_argument("path", nargs="?", help="要摄入的文件或目录路径")
    parser.add_argument("--all", action="store_true", help="摄入所有 untracked 文件")
    parser.add_argument("--project", action="store_true", help="明确指定是整个项目摄入")
    parser.add_argument("-y", "--yes", action="store_true", help="跳过确认直接执行")
    
    args = parser.parse_args()
    ingest_target(args.path, args.all, args.project, args.yes)
