---
name: mind-wiki
description: Mind Wiki - 可装载的个人/团队/岗位知识库。一个目录 = 完整的知识+身份+风格包，可直接加载到任意智能体。
author: icychick
user-invocable: true
---

# Mind Wiki Skill

> **可装载的思维包** — 一个目录就是一个完整的知识+身份+风格集合，可直接加载到任意智能体。基于 llm-wiki 极简设计，扩展个人/团队身份风格支持。

**核心特性：**
- ✨ 初始化一个新的 Mind Wiki 知识库
- 📥 Ingest 摄入任意文件/目录/项目
- 🔍 查询回答时自动匹配该知识库的说话风格与立场
- 📝 记录个人观点、反应、思考
- 🔀 无缝切换多个独立知识库
- 🏥 健康检查与维护
- 🔗 知识库关联：通过 LINKS.md 实现跨库知识引用
- 📦 100% 兼容 llm-wiki 知识库结构
- 🚀 可直接装载到任意新智能体，无需额外配置

## 命令

### 初始化
```
/mind init [name] [path]
```
- 示例：`/mind init icychick-personal`
- 可选指定路径，默认在 `~/Documents/mind-wiki/[name]` 初始化

### 摄入新源
```
/mind ingest [file-or-directory]
/mind ingest --all       # 摄入所有 untracked 文件
/mind ingest -y          # 跳过确认直接执行
/mind ingest --project  # 明确指定是整个项目摄入
```

### 查询问题
```
/mind query "你的问题是什么？"
```
- 回答会匹配当前知识库的说话风格和立场
- 回答后可选择保存问答到知识库

### 记录观点/想法
```
/mind note "我的新想法..."
/mind react "我对这篇文章的看法..."
```
- 快速记录思考、反应、观点到知识库

### 知识库管理
```
/mind list          # 列出所有知识库
/mind switch <name> # 切换当前知识库
/mind status        # 显示当前知识库状态
/mind config        # 显示当前配置
/mind lint          # 健康检查
/mind lint --fix    # 自动修复问题
```

### 快速保存（兼容 qmd 指令）
```
/qmd <内容标题>        # 快速将对话内容保存到当前知识库
/qmd                  # 交互式保存
```

## 工作流程

1. **Ingest** - 添加原始源 → 提取关键信息 → 生成该知识库视角的解读 → 创建/更新页面 → 更新索引
2. **Query** - 读取索引 → 查找相关内容 → 结合该知识库的身份/风格/立场 → 生成个性化回答
3. **Note** - 记录观点 → 归入观点库 → 更新索引
4. **Lint** - 检查一致性 → 修复问题 → 保持知识库健康

## 知识库结构
每个目录都是独立完整的：
```
知识库目录/
├── IDENTITY.md          # 身份定义：我是谁、什么背景
├── STYLE.md             # 说话风格：语气、习惯、禁忌
├── STANCE.md            # 核心立场：价值观、基本态度
├── LINKS.md             # 跨库关联：索引授权声明
├── raw/
│   ├── untracked/       # 待处理新源
│   └── ingested/        # 已处理源
└── wiki/
    ├── index.md         # 总索引
    ├── log.md           # 操作日志
    ├── concepts/        # 概念页面
    ├── sources/         # 源摘要页面
    └── answers/         # 已保存问答页面
```

## 装载机制
新智能体只需指向该知识库目录，即可自动读取：
- IDENTITY.md → 了解身份
- STYLE.md → 匹配说话方式
- STANCE.md → 遵循核心立场
- 知识库内容 → 拥有相关知识
- 无需任何额外配置，开箱即用

## 与 llm-wiki 兼容性
所有 llm-wiki 知识库可直接迁移，只需添加 IDENTITY.md、STYLE.md、STANCE.md 三个文件即可启用个性化功能。
