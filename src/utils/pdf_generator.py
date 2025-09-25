"""
PDF generation utilities for CV export with multiple templates.
"""

from io import BytesIO

import streamlit as st
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def get_template_colors(template):
    """Get color scheme for different PDF templates"""
    template_colors = {
        "Professional Blue": {
            "title": "#1e3a8a",
            "subtitle": "#1e40af",
            "section": "#1e40af",
            "border": "#3b82f6",
        },
        "Academic Classic": {
            "title": "#0f172a",
            "subtitle": "#374151",
            "section": "#374151",
            "border": "#6b7280",
        },
        "Modern Minimal": {
            "title": "#111827",
            "subtitle": "#4b5563",
            "section": "#6b7280",
            "border": "#d1d5db",
        },
        "Scientific Research": {
            "title": "#065f46",
            "subtitle": "#047857",
            "section": "#059669",
            "border": "#10b981",
        },
    }
    return template_colors.get(template, template_colors["Professional Blue"])


def create_pdf_styles(template):
    """Create PDF styles based on template"""
    colors_scheme = get_template_colors(template)
    styles = getSampleStyleSheet()

    # Title style
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        fontSize=24 if template != "Modern Minimal" else 22,
        spaceAfter=6,
        alignment=TA_CENTER,
        textColor=colors.HexColor(colors_scheme["title"]),
    )

    # Subtitle style
    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=styles["Heading2"],
        fontSize=14,
        spaceAfter=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor(colors_scheme["subtitle"]),
    )

    # Section header style
    section_style = ParagraphStyle(
        "SectionHeader",
        parent=styles["Heading2"],
        fontSize=14 if template != "Modern Minimal" else 12,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.HexColor(colors_scheme["section"]),
        borderWidth=1 if template != "Modern Minimal" else 0,
        borderColor=(
            colors.HexColor(colors_scheme["border"])
            if template != "Modern Minimal"
            else None
        ),
        borderPadding=3 if template != "Modern Minimal" else 0,
    )

    # Body text style
    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["Normal"],
        fontSize=10,
        spaceBefore=3,
        spaceAfter=3,
        leftIndent=0,
    )

    return {
        "title": title_style,
        "subtitle": subtitle_style,
        "section": section_style,
        "body": body_style,
    }


def add_personal_info_section(story, personal, styles):
    """Add personal information section to PDF"""
    if personal["full_name"]:
        title = Paragraph(f"<b>{personal['full_name']}</b>", styles["title"])
        story.append(title)

    if personal["title"]:
        subtitle = Paragraph(personal["title"], styles["subtitle"])
        story.append(subtitle)

    # Contact Information
    contact_data = []
    if personal["email"]:
        contact_data.append(["Email:", personal["email"]])
    if personal["phone"]:
        contact_data.append(["Phone:", personal["phone"]])
    if personal["location"]:
        contact_data.append(["Location:", personal["location"]])
    if personal["linkedin"]:
        contact_data.append(["LinkedIn:", personal["linkedin"]])
    if personal["github"]:
        contact_data.append(["GitHub:", personal["github"]])
    if personal["orcid"]:
        contact_data.append(["ORCID:", personal["orcid"]])

    if contact_data:
        # Split contact data into two columns
        mid_point = len(contact_data) // 2 + len(contact_data) % 2
        col1 = contact_data[:mid_point]
        col2 = contact_data[mid_point:] if len(contact_data) > mid_point else []

        # Pad col2 to match col1 length
        while len(col2) < len(col1):
            col2.append(["", ""])

        contact_table_data = []
        for i in range(len(col1)):
            row = [
                col1[i][0],
                col1[i][1],
                col2[i][0] if i < len(col2) else "",
                col2[i][1] if i < len(col2) else "",
            ]
            contact_table_data.append(row)

        contact_table = Table(
            contact_table_data, colWidths=[1 * inch, 2 * inch, 1 * inch, 2 * inch]
        )
        contact_table.setStyle(
            TableStyle(
                [
                    ("FONTSIZE", (0, 0), (-1, -1), 9),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                    ("FONTNAME", (2, 0), (2, -1), "Helvetica-Bold"),
                ]
            )
        )
        story.append(contact_table)
        story.append(Spacer(1, 12))

    # Professional Summary
    if personal["summary"]:
        story.append(Paragraph("<b>PROFESSIONAL SUMMARY</b>", styles["section"]))
        summary = Paragraph(personal["summary"], styles["body"])
        story.append(summary)
        story.append(Spacer(1, 6))


def add_skills_section(story, skills_data, styles):
    """Add skills section to PDF"""
    if any(skills_data.values()):
        story.append(Paragraph("<b>TECHNICAL SKILLS</b>", styles["section"]))

        for category, skills_list in skills_data.items():
            if skills_list:
                category_name = category.replace("_", " ").title()
                skills_text = f"<b>{category_name}:</b> {', '.join(skills_list)}"
                skills_para = Paragraph(skills_text, styles["body"])
                story.append(skills_para)
        story.append(Spacer(1, 6))


def add_education_section(story, education_list, styles):
    """Add education section to PDF"""
    if education_list:
        story.append(Paragraph("<b>EDUCATION</b>", styles["section"]))
        for edu in education_list:
            edu_title = f"<b>{edu['degree']}</b> - {edu['institution']}"
            story.append(Paragraph(edu_title, styles["body"]))

            edu_details = f"{edu['start_year']} - {edu['end_year']} | {edu['location']}"
            story.append(Paragraph(edu_details, styles["body"]))

            if edu["thesis_title"]:
                thesis = f"<i>Thesis:</i> {edu['thesis_title']}"
                story.append(Paragraph(thesis, styles["body"]))

            if edu["advisor"]:
                advisor = f"<i>Advisor:</i> {edu['advisor']}"
                story.append(Paragraph(advisor, styles["body"]))

            if edu["gpa"]:
                gpa = f"<i>GPA:</i> {edu['gpa']}"
                story.append(Paragraph(gpa, styles["body"]))

            if edu["description"]:
                story.append(Paragraph(edu["description"], styles["body"]))

            story.append(Spacer(1, 6))


def add_experience_section(story, experience_list, styles):
    """Add work experience section to PDF"""
    if experience_list:
        story.append(Paragraph("<b>WORK EXPERIENCE</b>", styles["section"]))
        for exp in experience_list:
            exp_title = f"<b>{exp['job_title']}</b> - {exp['company']}"
            story.append(Paragraph(exp_title, styles["body"]))

            exp_details = f"{exp['start_date']} - {exp['end_date']} | {exp['location']} | {exp['job_type']}"
            story.append(Paragraph(exp_details, styles["body"]))

            if exp["description"]:
                story.append(Paragraph(exp["description"], styles["body"]))

            story.append(Spacer(1, 6))


def add_projects_section(story, projects_list, styles):
    """Add projects section to PDF"""
    if projects_list:
        story.append(Paragraph("<b>PROJECTS</b>", styles["section"]))
        for project in projects_list:
            project_title = f"<b>{project['name']}</b> - {project['type']}"
            story.append(Paragraph(project_title, styles["body"]))

            project_details = f"{project['start_date']} - {project['end_date']}"
            if project["technologies"]:
                project_details += f" | Technologies: {project['technologies']}"
            story.append(Paragraph(project_details, styles["body"]))

            if project["description"]:
                story.append(Paragraph(project["description"], styles["body"]))

            if project["github_link"]:
                github = f"Repository: {project['github_link']}"
                story.append(Paragraph(github, styles["body"]))

            story.append(Spacer(1, 6))


def add_publications_section(story, publications_list, styles):
    """Add publications section to PDF"""
    if publications_list:
        story.append(Paragraph("<b>PUBLICATIONS</b>", styles["section"]))
        for pub in publications_list:
            pub_title = f"<b>{pub['title']}</b>"
            story.append(Paragraph(pub_title, styles["body"]))

            pub_details = f"{pub['authors']} ({pub['year']}). {pub['journal']}"
            if pub["volume"] and pub["pages"]:
                pub_details += f", Vol. {pub['volume']}, pp. {pub['pages']}"
            story.append(Paragraph(pub_details, styles["body"]))

            if pub["doi"]:
                doi = f"DOI: {pub['doi']}"
                story.append(Paragraph(doi, styles["body"]))

            story.append(Spacer(1, 6))


def add_certifications_section(story, certifications_list, styles):
    """Add certifications section to PDF"""
    if certifications_list:
        story.append(Paragraph("<b>CERTIFICATIONS</b>", styles["section"]))
        for cert in certifications_list:
            cert_title = f"<b>{cert['name']}</b> - {cert['issuing_org']}"
            story.append(Paragraph(cert_title, styles["body"]))

            cert_details = (
                f"Issued: {cert['issue_date']} | Expires: {cert['expiry_date']}"
            )
            story.append(Paragraph(cert_details, styles["body"]))

            story.append(Spacer(1, 6))


def add_awards_section(story, awards_list, styles):
    """Add awards section to PDF"""
    if awards_list:
        story.append(Paragraph("<b>AWARDS & HONORS</b>", styles["section"]))
        for award in awards_list:
            award_title = f"<b>{award['name']}</b> - {award['awarding_org']}"
            story.append(Paragraph(award_title, styles["body"]))

            award_details = f"Date: {award['date']}"
            story.append(Paragraph(award_details, styles["body"]))

            if award["description"]:
                story.append(Paragraph(award["description"], styles["body"]))

            story.append(Spacer(1, 6))


def generate_pdf_cv(cv_data, template="Professional Blue", page_format="A4"):
    """Generate comprehensive PDF version of the CV with template options"""
    try:
        # Page setup
        pagesize = A4 if page_format == "A4" else letter
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=pagesize,
            rightMargin=0.75 * inch,
            leftMargin=0.75 * inch,
            topMargin=0.75 * inch,
            bottomMargin=0.75 * inch,
        )

        # Get styles for the selected template
        styles = create_pdf_styles(template)
        story = []

        # Add all sections
        add_personal_info_section(story, cv_data["personal_info"], styles)
        add_skills_section(story, cv_data["skills"], styles)
        add_education_section(story, cv_data["education"], styles)
        add_experience_section(story, cv_data["experience"], styles)
        add_projects_section(story, cv_data["projects"], styles)
        add_publications_section(story, cv_data["publications"], styles)
        add_certifications_section(story, cv_data["certifications"], styles)
        add_awards_section(story, cv_data["awards"], styles)

        # Build the PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()

    except Exception as e:
        st.error(f"Error generating PDF: {e}")
        return None
