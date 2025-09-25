# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a comprehensive **Professional CV Builder** application built with Streamlit, specifically designed for PhD bioinformaticians, computational biologists, and researchers. The application provides a complete solution for creating, editing, and exporting professional academic and industry CVs with specialized sections for scientific careers.

## Architecture

- **streamlit_app.py**: Main application containing the full CV builder with sections for:
  - Personal information with photo upload
  - Education (PhD, academic credentials)
  - Work experience with timeline
  - Technical skills (programming, bioinformatics tools, databases)
  - Research projects with GitHub links
  - Publications (academic papers, conferences)
  - Certifications and awards
  - Professional PDF export with multiple templates

- **requirements.txt**: Dependencies including Streamlit, ReportLab, PIL, Plotly
- **cv_todo_list.md**: Comprehensive development roadmap and feature specifications

## Development Commands

### Setup
```bash
pip install -r requirements.txt
```

### Run the application
```bash
streamlit run streamlit_app.py
```

The application will start on `http://localhost:8501` with a sidebar navigation system.

## Key Features

### CV Sections
1. **Personal Information**: Name, title, contact details, ORCID, GitHub, LinkedIn, professional summary
2. **Education**: Degrees, institutions, thesis titles, advisors, GPA
3. **Work Experience**: Job titles, companies, dates, descriptions with academic/industry focus
4. **Technical Skills**: Categorized by programming languages, bioinformatics tools, statistical software, databases, cloud platforms
5. **Projects**: Research projects, software development, with technology stacks and repository links
6. **Publications**: Academic papers with DOI, PMID, journal details, citation formatting
7. **Certifications & Awards**: Professional certifications and academic honors

### Export Features
- **PDF Export**: Multiple professional templates (Professional Blue, Academic Classic, Modern Minimal, Scientific Research)
- **Data Export/Import**: JSON format for backup and transfer
- **Template Options**: A4/Letter page formats
- **Professional Styling**: Academic and industry-appropriate formatting

### Data Management
- Session state persistence during application use
- Form-based data entry with validation
- Dynamic adding/removing of entries
- Preview functionality before export

## Application Architecture

The application uses a single-page architecture with sidebar navigation:
- Each section is implemented as a separate function
- Session state management for data persistence
- Professional CSS styling with multiple color schemes
- ReportLab-based PDF generation with template support

## Customization Notes

- Template colors and styles are defined in the `generate_pdf_cv()` function
- Skills categories are specifically tailored for bioinformatics/computational biology
- Publication section supports academic citation formats
- All forms include relevant placeholders and help text for scientific careers