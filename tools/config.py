#!/usr/bin/env python3
"""
Mind Wiki 配置管理工具
"""
import os
import json
from pathlib import Path

CONFIG_PATH = Path.home() / ".mind-wiki" / "config.json"

def init_config():
    """初始化配置文件"""
    CONFIG_PATH.parent.mkdir(exist_ok=True, parents=True)
    if not CONFIG_PATH.exists():
        config = {
            "current_wiki": "",
            "wikis": {}
        }
        with open(CONFIG_PATH, "w") as f:
            json.dump(config, f, indent=2)
    return CONFIG_PATH

def load_config():
    """加载配置"""
    init_config()
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_config(config):
    """保存配置"""
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

def add_wiki(name, path):
    """添加新的知识库"""
    config = load_config()
    config["wikis"][name] = str(Path(path).expanduser().resolve())
    save_config(config)

def switch_wiki(name):
    """切换当前知识库"""
    config = load_config()
    if name not in config["wikis"]:
        raise ValueError(f"知识库 {name} 不存在")
    config["current_wiki"] = name
    save_config(config)
    return config["wikis"][name]

def get_current_wiki_path():
    """获取当前知识库路径"""
    config = load_config()
    if not config["current_wiki"]:
        raise ValueError("没有选中的知识库，请先初始化或切换")
    return Path(config["wikis"][config["current_wiki"]])

def list_wikis():
    """列出所有知识库"""
    config = load_config()
    return config["wikis"], config["current_wiki"]

def get_wiki_path(name):
    """获取指定知识库的路径"""
    config = load_config()
    if name not in config["wikis"]:
        raise ValueError(f"知识库 {name} 不存在")
    return Path(config["wikis"][name])

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("用法: config.py [init|list|switch|current] [name]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "init":
        init_config()
        print("配置初始化完成")
    elif cmd == "list":
        wikis, current = list_wikis()
        print("现有知识库:")
        for name, path in wikis.items():
            prefix = "✅" if name == current else "  "
            print(f"{prefix} {name:<20} {path}")
    elif cmd == "switch" and len(sys.argv) == 3:
        name = sys.argv[2]
        path = switch_wiki(name)
        print(f"已切换到知识库: {name} → {path}")
    elif cmd == "current":
        try:
            path = get_current_wiki_path()
            print(f"当前知识库: {path}")
        except ValueError as e:
            print(e)
    else:
        print("无效命令")
        sys.exit(1)
