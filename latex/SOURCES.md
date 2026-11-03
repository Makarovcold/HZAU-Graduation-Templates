# 来源与参考文档

本文列出模板使用的公开格式文档、上游项目和技术资料。

## 学校公开文档

[本科生院《学位（毕业）论文撰写规范（自然科学类）》](https://bksy.hzau.edu.cn/info/1039/1059.htm)，公开页面日期 2022-04-18，文件号校发〔2017〕73号。用于对照论文组成、A4 页面、装订边、页码、标题字号、摘要、图表和参考文献。

[信息学院 2026 届学士学位论文答辩工作方案](https://coi.hzau.edu.cn/info/1611/63091.htm)，发布于 2026-05-09。用于核对提交形式：该届方案涉及 PDF 和带修订痕迹的 Word；LaTeX 工程不会自动生成带修订痕迹的 Word。后续届次应查阅当届通知。

模板采用图表按节编号；公开规范的图表示例为连续编号。使用时应按学院要求选择编号方式。

## 上游项目与素材

上游：[eriche2016/HZAU_UnderGraduateThesis_Template](https://github.com/eriche2016/HZAU_UnderGraduateThesis_Template)，作者 Xinwei He。类文件头保留原署名和仓库链接。

本项目在上游排版类基础上整理了身份信息配置、字体选项、双面分页、目录链接和自动参考文献。排版特性与验证范围见完整包中的 `docs/THESIS_REVIEW.md`。

校名图形来自[上游 Fig/HZAU.png](https://github.com/eriche2016/HZAU_UnderGraduateThesis_Template/blob/main/Fig/HZAU.png)，PPT 使用同一素材并保留比例。本项目不主张该图形的原创权。许可说明见完整包根目录的 `THIRD_PARTY_NOTICES.md`。

## 技术文档

| 文档 | 用途 |
| --- | --- |
| [CTeX](https://ctan.org/pkg/ctex) | 中文、UTF-8、字体配置 |
| [biblatex-gb7714-2015](https://ctan.org/pkg/biblatex-gb7714-2015) | 作者—年份引用、姓名及中文文献基础 |
| [Biber](https://ctan.org/pkg/biber) | 文献数据处理 |
| [latexmk](https://www.cantab.net/users/johncollins/latexmk/) | 多轮编译与依赖处理 |
| [bicaption](https://ctan.org/pkg/bicaption) | 双语图题 |
| [Overleaf XeLaTeX](https://www.overleaf.com/learn/latex/XeLaTeX) | 编译器与字体使用说明 |
| [LaTeX Workshop 编译文档](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile) | VS Code 构建 recipe |
| [Microsoft PowerPoint 模板说明](https://support.microsoft.com/en-us/powerpoint/create-and-save-a-powerpoint-template) | POTX 格式与复用方法 |

常见文献类型的作者大小写、年份位置和标点由 `config/bibliography.tex` 统一设置。未覆盖的类型仍沿用宏包回退格式，需逐条核对。两部示例著作仅用于展示引用，条目见 `references.bib`；它们不是学校排版依据。

## PPT 设计

18 页毕业答辩和 12 页中期答辩的通用布局由本项目制作，使用深绿、浅绿、米白和微软雅黑。中期模板侧重目标、工作证据、问题与剩余计划。

文本、表格、图表、技术路线和连接线可编辑，毕业答辩图表含嵌入数据表；数据均为虚构排版示例。图像和公式槽待使用者替换。增删页后需更新文本页码，两套模板均有隐藏备用页。
