# MathTranslations Skill

一个用于严谨数学翻译的 Codex skill。它把数学书籍、论文、讲义或已有
LaTeX 项目翻译成可编译、可校对、可维护的中文 LaTeX，并支持复核与修复
现有译稿。

本项目根据 [MathTranslations 数学翻译指南](https://mathtranslations.org/guide/)
整理为可执行工作流，但并非 MathTranslations 官方项目，也不复制或固定打包
可能持续更新的在线术语表与模板。

## 能做什么

- 以出版 PDF 为内容核对依据，以源 TeX 辅助恢复结构和标记
- 保留定理、证明、公式、标签、引用、脚注、图表和层级结构
- 建立项目术语表，检查术语与符号一致性
- 分离中文、数学、编译与版面三类校对
- 用内置脚本检查重复标签、未定义引用、缺失资源、待办标记和编译日志

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

## LaTeX 审计

```bash
python scripts/audit_latex.py path/to/project
python scripts/audit_latex.py path/to/project --strict
```

默认情况下，确定性错误返回非零状态；`--strict` 也会让警告返回非零状态，
适合 CI。

## 目录

```text
mathtranslations/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── latex-quality.md
│   ├── review-checklist.md
│   └── workflow.md
├── scripts/audit_latex.py
└── tests/test_audit_latex.py
```

## 来源与边界

工作流主要依据 MathTranslations 公开指南整理，并使用自己的表述和实现。
在线指南、术语资源与模板可能更新，实际项目应以
[指南页面](https://mathtranslations.org/guide/) 当前版本为准。

数学翻译仍需要领域知识和人工判断。编译成功或脚本检查通过，不代表数学内容
已经正确。

## License

本仓库原创内容采用 MIT License。第三方网站、模板、术语数据与原始数学作品
仍受其各自许可和版权约束。
