# MathTranslations Skill

一个用于严谨数学翻译的 Codex skill。它把数学书籍、论文、讲义或已有
LaTeX 项目翻译成可编译、可校对、可维护的中文 LaTeX，并支持复核与修复
现有译稿。

本项目根据 [MathTranslations 数学翻译指南](https://mathtranslations.org/guide/)
整理为可执行工作流，并经 MathTranslations 创始人和版权所有者授权，内置
MIT 许可的 LaTeX 模板与 logo。在线术语表仍保持外部引用，以免固定过期数据。

## 能做什么

- 以出版 PDF 为内容核对依据，以源 TeX 辅助恢复结构和标记
- 保留定理、证明、公式、标签、引用、脚注、图表和层级结构
- 建立项目术语表，检查术语与符号一致性
- 支持 MathTranslations 官方模板的 `\newterm`、术语索引、长证明及习题答案互跳
- 新项目可以直接从 skill 的 `assets/` 复制模板与 logo，无需额外下载
- 分离中文、数学、编译与版面三类校对
- 用内置脚本检查重复标签、未定义引用、缺失资源、模板漂移和编译日志

## 安装

将本仓库克隆或复制到 Codex skills 目录：

```text
~/.codex/skills/mathtranslations
```

重新启动 Codex 后，可以显式调用：

```text
使用 $mathtranslations 把这篇数学论文翻译成中文 LaTeX，并编译校对。
```

也可以用于审校：

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
链接配置、术语键、长证明配对、句末标点和最终术语索引。

## 目录

```text
mathtranslations/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── MathTranslations-Template.tex
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

模板配置参考核对了
`MathTranslations-Template.c9598d4a8d56.zip` 的实际 TeX 与示例 PDF。
模板 TeX 与 logo 经版权所有者授权，作为本仓库 MIT 许可内容公开；编译示例
PDF 未打包，因为运行 skill 不需要它。

数学翻译仍需要领域知识和人工判断。编译成功或脚本检查通过，不代表数学内容
已经正确。

## License

本仓库内容（包括 `assets/MathTranslations-Template.tex` 与
`assets/logo.pdf`）采用 MIT License。在线术语数据与原始数学作品仍受其
各自许可和版权约束。
