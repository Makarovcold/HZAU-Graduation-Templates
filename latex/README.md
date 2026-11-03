# LaTeX 通用论文模板

从本目录编译：

```sh
latexmk -xelatex main.tex
```

需要 XeLaTeX、Biber 和 latexmk。首次使用建议安装带中文支持的完整 TeX Live。也可以在 VS Code 中打开本目录，安装 LaTeX Workshop，并使用随工程提供的构建 recipe。

## 修改顺序

1. 在 `config/metadata.tex` 中改题目、姓名、学院、专业、班级、导师、中英文日期及学位类型。
2. 在 `frontmatter/abstracts.tex` 中写中英文摘要和关键词。
3. 在 `chapters/` 中写正文。当前基于 `article`，一级标题使用 `\section`。
4. 在 `references.bib` 中加文献，正文使用 `\parencite{key}` 或 `\textcite{key}`。
5. 替换图表数据，在 `main.tex` 文末写致谢。
6. 编译并逐页检查 PDF。方括号、示例姓名及全零学号均需要替换。

## 参考文献

文末由 `\printbibliography` 自动生成，仅输出正文引用的文献。中文条目建议加 `langid = {chinese}`，英文条目加 `langid = {english}`。

以 `gb7714-2015ay` 作者—年份样式为基础，在 `config/bibliography.tex` 对常见书籍、期刊、会议、文集章节、学位论文与在线条目统一设置著录：姓名保留正常大小写、去掉类型标识、书籍年份置后，中文与英文使用不同标点。期刊、会议的卷期页码和出版字段须按实际文献填写。未覆盖的类型沿用宏包回退样式。

文内两位中文作者使用“和”、英文作者使用“and”，多作者使用等 / et al。中文条目在前，按姓名排序；单次引用多部文献时请手动按要求安排键名顺序。不要使用 `\nocite{*}` 收录未引用文献。

不用 latexmk 时，运行完整流程：

```sh
xelatex -interaction=nonstopmode -halt-on-error main.tex
biber main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

## 字体、空白页和图表编号

- 默认使用 Windows 环境中的宋体、黑体和 Times New Roman。缺少 Times New Roman 时会警告并回退；不同系统的 CTeX 中文字体默认值也可能不同。
- 跨平台使用时，在 `main.tex` 的类选项中添加 `portablefonts`，即 `\documentclass[portablefonts,UTF8,twoside,AutoFakeBold=1,AutoFakeSlant,zihao=-4]{HZAU}`，改用 Fandol / TeX Gyre Termes。字体切换后重新检查分页。
- 封面、扉页与声明后保留双面装订用空白背页，由 `config/layout.tex` 的 `\thesisBlankPage` 控制。
- 目录之后和摘要之后通过 `\thesisRectoPage` 必要时补空白页，让新页码序列从正面开始。默认示例中的第 2、4、6、8 个物理页为空白；修改摘要、目录长度后空白页位置可能变化。
- 图表和公式沿用“节号-序号”，例如 `3-1`。若学院要求连续图表编号，需同时修改 `HZAU.cls` 的编号格式及按节重置规则。
- 封面题目过长可能改变行数，定稿时应查看整页。

## 图片与签名

图片放在 `Fig/`，建议使用英文文件名，注意大小写。引用示例：

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.85\linewidth]{Fig/your-image.pdf}
  \bicaption{中文图题}{English caption}
  \label{fig:your-image}
\end{figure}
```

将 `your-image.pdf` 换成真实文件。图题在下、表题在上，表格使用三线表。交叉引用用 `\ref`，公式引用用 `\eqref`。

缺少签名时自动保留空白签名栏。若提交要求电子签名，可在本地的 `private/` 中放入 `author_signature.png` 和 `mentor_signature.png`，不要将真实签名提交到公开仓库。

## Overleaf

上传本目录内容，或上传单独的 Overleaf ZIP，主文件选择 `main.tex`，编译器选择 XeLaTeX，并添加 `portablefonts`。系统字体和跨平台字体模式均已在 TeX Live 2026 下通过本地编译验证，Overleaf 平台兼容性尚未实测。

## 常见问题

| 现象 | 处理 |
| --- | --- |
| 引用显示键名或文末为空 | 检查 Biber 是否运行成功、引用键是否存在 |
| 目录或引用显示 `??` | 修复前面的错误后继续运行 latexmk |
| 中文报错 | 确认 XeLaTeX、中文宏包和 Fandol 字体可用 |
| 图片缺失 | 检查文件、大小写和编译工作目录 |
| 旧缓存异常 | `latexmk -c main.tex` 后重新构建 |
| 宽表或长公式越界 | 检查日志中的 Overfull，并修改排版 |

可运行 `python scripts/check_assets.py main` 检查输入文件、图片和引用键。

学校格式及上游来源见[总来源说明](SOURCES.md)。
