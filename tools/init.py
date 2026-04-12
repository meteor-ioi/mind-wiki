#!/usr/bin/env python3
"""
Mind Wiki 初始化工具
"""
import os
import sys
from pathlib import Path
from datetime import datetime
import shutil

SKILL_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = SKILL_DIR / "templates"

def init_wiki(name, path=None):
    """初始化新的知识库"""
    from config import add_wiki, switch_wiki
    
    # 确定路径
    if path is None:
        path = Path.home() / "Documents" / "mind-wiki" / name
    else:
        path = Path(path).expanduser().resolve()
    
    # 检查目录
    if path.exists() and any(path.iterdir()):
        confirm = input(f"目录 {path} 已存在且不为空，是否继续？(y/N) ")
        if confirm.lower() != "y":
            print("已取消")
            return
    
    # 创建目录结构
    path.mkdir(parents=True, exist_ok=True)
    (path / "raw" / "untracked").mkdir(parents=True, exist_ok=True)
    (path / "raw" / "ingested").mkdir(parents=True, exist_ok=True)
    (path / "wiki" / "concepts").mkdir(parents=True, exist_ok=True)
    (path / "wiki" / "sources").mkdir(parents=True, exist_ok=True)
    (path / "wiki" / "answers").mkdir(parents=True, exist_ok=True)
    (path / "wiki" / "viewpoints").mkdir(parents=True, exist_ok=True)
    
    # 复制模板文件
    templates = [
        ("IDENTITY.md.template", "IDENTITY.md"),
        ("STYLE.md.template", "STYLE.md"),
        ("STANCE.md.template", "STANCE.md"),
        ("LINKS.md.template", "LINKS.md"),
        ("index.md.template", "wiki/index.md"),
        ("log.md.template", "wiki/log.md"),
    ]
    
    for template_name, target_path in templates:
        template_path = TEMPLATES_DIR / template_name
        target_full_path = path / target_path
        
        with open(template_path, "r") as f:
            content = f.read()
        
        # 替换变量
        content = content.replace("{wiki_name}", name)
        content = content.replace("{YYYY-MM-DD}", datetime.now().strftime("%Y-%m-%d"))
        
        with open(target_full_path, "w") as f:
            f.write(content)
    
    # 添加到配置并切换
    add_wiki(name, str(path))
    switch_wiki(name)
    
    print(f"\n✅ 知识库 {name} 初始化完成！")
    print(f"📍 位置: {path}")
    print("\n📝 下一步:")
    print("1. 填充 IDENTITY.md、STYLE.md、STANCE.md 定义你的身份")
    print("2. 把文件放到 raw/untracked/ 目录")
    print("3. 执行 /mind ingest 开始摄入内容")
    
    return path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: init.py <知识库名称> [路径]")
        sys.exit(1)
    
    name = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else None
    init_wiki(name, path)
