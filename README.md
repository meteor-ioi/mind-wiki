# Mind Wiki

> 可装载的思维包 — 一个目录就是一个完整的知识+身份+风格集合，可直接加载到任意智能体。

## 简介
Mind Wiki 是基于 llm-wiki 扩展的知识库工具，在 llm-wiki 纯知识存储的基础上，增加了**身份、风格、立场**三层配置，让知识库不仅能回答问题，还能以你的方式回答问题。

## 核心特性
- ✨ **完整思维包**：一个目录 = 知识 + 身份 + 风格 + 立场
- 🚀 **可装载**：任意智能体只需指向该目录，立即拥有该身份的所有知识和说话方式
- 🔀 **无缝切换**：像切换输入法一样切换不同的思维包（个人/团队/岗位）
- 📥 **智能摄入**：自动提取内容并生成该视角的解读
- 🔍 **个性化回答**：回答自动匹配该知识库的说话风格和立场
- 🔗 **知识库关联**：通过 `LINKS.md` 建立网状知识关联，支持跨库查询
- 📦 **100% 兼容 llm-wiki**：原有知识库可直接迁移
- 🧹 **健康检查**：自动检测矛盾、孤立页面、缺失内容等问题

## 快速开始

### 1. 安装
将技能目录放到 OpenClaw 技能目录下，重启 OpenClaw 即可使用。

### 2. 初始化第一个知识库
```
/mind init icychick-personal
```
默认会在 `~/Documents/mind-wiki/icychick-personal` 创建知识库。

### 3. 定义你的身份
编辑三个核心文件：
- `IDENTITY.md`：你是谁、什么背景
- `STYLE.md`：你怎么说话、语气习惯
- `STANCE.md`：你的核心立场、价值观

### 4. 摄入内容
把文件放到 `raw/untracked/` 目录，然后：
```
/mind ingest --all
```
Mind Wiki 会自动分析内容，提取概念，并生成你的视角解读。

### 5. 开始查询
```
/mind query "刻意练习的核心是什么？"
```
回答会自动匹配你的说话风格和立场。

## 核心命令

### 知识库管理
```
/mind init [name] [path]    # 初始化新知识库
/mind list                  # 列出所有知识库
/mind switch <name>         # 切换当前知识库
/mind status                # 显示当前知识库状态
```

### 内容操作
```
/mind ingest [path]         # 摄入指定文件/目录
/mind ingest --all          # 摄入所有待处理文件
/mind ingest --project      # 摄入整个项目
/mind note "我的想法..."     # 记录观点/思考/反应
/mind query "问题"           # 查询知识库
/mind lint                  # 健康检查
/mind lint --fix            # 自动修复问题
```

### 快速保存
```
/qmd "内容"                 # 快速保存内容到知识库
/qmd                        # 交互式保存最近对话
```

## 知识库结构
```
知识库目录/
├── IDENTITY.md          # 身份定义
├── STYLE.md             # 说话风格
├── STANCE.md            # 核心立场
├── raw/
│   ├── untracked/       # 待处理新源
│   └── ingested/        # 已处理源（按日期归档）
└── wiki/
    ├── index.md         # 总索引
    ├── log.md           # 操作日志
    ├── concepts/        # 概念页面（包含"我的解读"）
    ├── sources/         # 源摘要页面
    ├── viewpoints/      # 观点/反应/思考页面
    └── answers/         # 已保存的问答页面
```

## 装载机制
当你创建新智能体时，只需要：
1. 安装 Mind Wiki 技能
2. 指向某个知识库目录：`~/Documents/mind-wiki/icychick-personal/`
3. 智能体自动读取所有配置和内容，立即以该身份运作，无需额外配置。

## 迁移 llm-wiki 知识库
1. 把 llm-wiki 知识库复制到 `~/Documents/mind-wiki/` 目录
2. 添加 `IDENTITY.md`、`STYLE.md`、`STANCE.md` 三个文件到根目录
3. 执行 `/mind add <name> <path>` 添加到配置
4. 直接使用，所有功能兼容。

## 许可证
MIT
