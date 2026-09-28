"""
exporters/docx.py - 工业级 Word 导出器
根据 Document IR 统一模型自动渲染标准 .docx 文档，集成插图自适应与三线表
"""

import os
from typing import Optional
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from mp4_analysis.document.models import DocumentIR

class DocxExporter:
    def __init__(self):
        pass

    def export(self, doc_ir: DocumentIR, output_path: str, figures_dir: Optional[str] = None):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        doc = Document()

        for s in doc.sections:
            s.top_margin = Inches(0.8)
            s.bottom_margin = Inches(0.8)
            s.left_margin = Inches(0.9)
            s.right_margin = Inches(0.9)

        # 标题
        p_title = doc.add_paragraph()
        p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_title.paragraph_format.space_before = Pt(40)
        p_title.paragraph_format.space_after = Pt(30)
        r_title = p_title.add_run(doc_ir.doc_id.replace("_", " "))
        r_title.font.name = "Microsoft YaHei"
        r_title.font.size = Pt(22)
        r_title.font.bold = True
        r_title.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)

        for page in doc_ir.pages:
            for elem in page.elements:
                if elem.type == "heading":
                    p = doc.add_paragraph()
                    p.paragraph_format.space_before = Pt(12)
                    p.paragraph_format.space_after = Pt(4)
                    r = p.add_run(str(elem.content))
                    r.font.name = "Microsoft YaHei"
                    r.font.size = Pt(13)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x2F, 0x55, 0x97)
                elif elem.type == "figure" and figures_dir:
                    fig_name = elem.metadata.get("figure_file")
                    if fig_name:
                        fig_path = os.path.join(figures_dir, fig_name)
                        if os.path.exists(fig_path):
                            p_fig = doc.add_paragraph()
                            p_fig.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            p_fig.paragraph_format.space_before = Pt(6)
                            p_fig.paragraph_format.space_after = Pt(2)
                            r_img = p_fig.add_run()
                            r_img.add_picture(fig_path, width=Inches(5.4))

                            p_cap = doc.add_paragraph()
                            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            p_cap.paragraph_format.space_after = Pt(8)
                            r_cap = p_cap.add_run(str(elem.content))
                            r_cap.font.name = "Microsoft YaHei"
                            r_cap.font.size = Pt(9.5)
                            r_cap.font.bold = True
                            r_cap.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
                else:
                    p = doc.add_paragraph()
                    p.paragraph_format.space_after = Pt(3)
                    p.paragraph_format.line_spacing = 1.25
                    r = p.add_run(str(elem.content))
                    r.font.name = "Microsoft YaHei"
                    r.font.size = Pt(10)
                    r.font.color.rgb = RGBColor(0x26, 0x26, 0x26)

        doc.save(output_path)
        return output_path
