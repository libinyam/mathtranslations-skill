# MathTranslations Agent Skill

一个平台无关的严谨数学翻译 Agent Skill。它把数学书籍、论文、讲义或已有
LaTeX 项目翻译成可编译、可校对、可维护的中文 LaTeX，并支持复核与修复
现有译稿。

本 Skill 不绑定 Codex 或任何特定模型、厂商和 Agent 框架。任何能够读取
Markdown 指令、访问项目文件并调用必要工具的 Agent 都可以使用。

本项目根据 [MathTranslations 数学翻译指南](https://mathtranslations.org/guide/)
整理为可执行工作流，并经 MathTranslations 创始人和版权所有者授权，内置
MIT 许可的 LaTeX 模板与 logo。在线术语表仍保持外部引用，以免固定过期数据。

## 能做什么

- 以出版 PDF 为内容核对依据，以源 TeX 辅助恢复结构和标记
- 保留定理、证明、公式、标签、引用、脚注、图表和层级结构
- 建立项目术语表，检查术语与符号一致性
- 支持 MathTranslations 官方模板的 `\newterm`、术语索引、长证明及习题答案互跳
- 插图按优先级处理：清晰原图优先截图、简单插图用 TikZ、交换图统一用 `tikz-cd` 重绘
- 行间公式统一 `align` 类环境、有序列表用 `enumerate`、中文引号用 TeX 引号写法
- 新项目可以直接从 skill 的 `assets/` 复制模板与 logo，无需额外下载
- 分离中文、数学、编译与版面三类校对
- 用内置脚本检查重复标签、未定义引用、缺失资源、模板漂移、连续展示公式、
  全角弯引号、手动编号列表和编译日志

## Agent 兼容性

Agent 最好具备以下能力：

- 读取 `SKILL.md` 和按需读取 `references/`
- 读取原始 PDF、MinerU Markdown、图片和 LaTeX 文件
- 在工作目录中创建和修改文件
- 执行 Python、XeLaTeX 或项目已有的构建命令
- 检查编译日志和生成的 PDF

`agents/openai.yaml` 只是 OpenAI/Codex 客户端可选的界面元数据。其他 Agent
可以忽略它，直接使用 `SKILL.md`。

## 安装与调用

将本仓库克隆到本地：

```bash
git clone https://github.com/libinyam/mathtranslations-skill.git
```

然后选择适合当前 Agent 的方式：

1. 将仓库复制到该 Agent 的 skills、rules 或 instructions 目录。
2. 在 Agent 配置中将本仓库或 `SKILL.md` 注册为一个 skill。
3. 在任务中直接要求 Agent 先读取本仓库的 `SKILL.md`。

支持 skill 调用语法的 Agent 可以使用：

```text
使用 $mathtranslations 把这篇数学论文翻译成中文 LaTeX，并编译校对。
所有交换图、态射图和适合节点箭头表达的数学图必须使用 tikzcd 重绘，
不得使用截图代替。
```

不支持 `$skill-name` 语法的 Agent 可以使用：

```text
请先读取 mathtranslations/SKILL.md，并严格按照其中的工作流，
把这篇数学论文翻译成中文 LaTeX，完成编译与校对。
所有交换图、态射图和适合节点箭头表达的数学图必须使用 tikzcd 重绘。
```

审校已有译本：

```text
使用 $mathtranslations 对照原始 PDF 复核这个中文 LaTeX 项目，修复引用和排版问题。
```

创建新译本时，只需向 Agent 提供原书 PDF、MinerU Markdown 以及提取的图片；
skill 会从自身 assets 复制模板和 logo 到项目目录。

## LaTeX 审计

```bash
python scripts/audit_latex.py path/to/project
python scripts/audit_latex.py path/to/project --strict
python scripts/audit_latex.py path/to/project --profile mathtranslations --strict
```

默认情况下，确定性错误返回非零状态；`--strict` 也会让警告返回非零状态，
适合 CI。`--profile mathtranslations` 还会检查 XeLaTeX、模板元信息、字体与
链接配置、术语键、长证明配对、句末标点、行间公式环境、引号写法、列表
环境和最终术语索引。

## 目录

```text
mathtranslations/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── mathtranslations-translation-template.tex
│   └── logo.pdf
├── references/
│   ├── latex-quality.md
│   ├── mathtranslations-template.md
│   ├── review-checklist.md
│   └── workflow.md
├── scripts/audit_latex.py
└── tests/test_audit_latex.py
```

## 来源与边界

工作流主要依据 MathTranslations 公开指南整理，并使用自己的表述和实现。
在线指南、术语资源与模板可能更新，实际项目应以
[指南页面](https://mathtranslations.org/guide/) 当前版本为准。

模板配置参考核对了官方
`mathtranslations-translation-template.zip`（2026-08-23 版；旧名
`MathTranslations-Template.c9598d4a8d56.zip` 为同一模板的早期发布）的
实际 TeX 与示例 PDF。模板 TeX 与 logo 经版权所有者授权，作为本仓库 MIT
许可内容公开；编译示例 PDF 未打包，因为运行 skill 不需要它。

数学翻译仍需要领域知识和人工判断。编译成功或脚本检查通过，不代表数学内容
已经正确。

## License

本仓库内容（包括 `assets/mathtranslations-translation-template.tex` 与
`assets/logo.pdf`）采用 MIT License。在线术语数据与原始数学作品仍受其
各自许可和版权约束。
