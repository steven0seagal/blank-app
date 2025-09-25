"""
Preview and Export section for CV Builder.
"""

import streamlit as st
import json
from src.utils.styles import display_section_header, display_success_message
from src.utils.pdf_generator import generate_pdf_cv

def preview_export_section():
    """Render the preview and export section"""
    display_section_header("👀 Preview & Export")

    cv_data = st.session_state.cv_data
    personal = cv_data['personal_info']

    # Preview section
    st.subheader("📋 CV Preview")

    if not personal.get('full_name'):
        st.warning("Please complete your personal information before previewing or exporting.")
        return

    # Create preview in a styled container
    with st.container():
        st.markdown('<div class="cv-preview">', unsafe_allow_html=True)

        # Personal Info Preview
        if personal['full_name']:
            st.markdown(f"### {personal['full_name']}")
            if personal['title']:
                st.markdown(f"*{personal['title']}*")

            contact_info = []
            if personal['email']:
                contact_info.append(f"📧 {personal['email']}")
            if personal['phone']:
                contact_info.append(f"📱 {personal['phone']}")
            if personal['location']:
                contact_info.append(f"📍 {personal['location']}")

            if contact_info:
                st.write(" | ".join(contact_info))

            # Online presence
            online_presence = []
            if personal['linkedin']:
                online_presence.append(f"💼 LinkedIn")
            if personal['github']:
                online_presence.append(f"💻 GitHub")
            if personal['orcid']:
                online_presence.append(f"🎓 ORCID")

            if online_presence:
                st.write(" | ".join(online_presence))

            if personal['summary']:
                st.markdown("**Professional Summary:**")
                st.write(personal['summary'])

        # Skills Preview
        if any(cv_data['skills'].values()):
            st.markdown("**Technical Skills:**")
            for category, skills_list in cv_data['skills'].items():
                if skills_list:
                    category_name = category.replace('_', ' ').title()
                    st.write(f"*{category_name}:* {', '.join(skills_list[:5])}{'...' if len(skills_list) > 5 else ''}")

        # Education Preview
        if cv_data['education']:
            st.markdown("**Education:**")
            for edu in cv_data['education']:
                st.write(f"• {edu['degree']} - {edu['institution']} ({edu['start_year']}-{edu['end_year']})")

        # Experience Preview
        if cv_data['experience']:
            st.markdown("**Work Experience:**")
            for exp in cv_data['experience']:
                st.write(f"• {exp['job_title']} at {exp['company']} ({exp['start_date']} - {exp['end_date']})")

        # Projects Preview
        if cv_data['projects']:
            st.markdown("**Projects:**")
            for project in cv_data['projects'][:3]:  # Show first 3 projects
                st.write(f"• {project['name']} - {project['type']}")

        # Publications Preview
        if cv_data['publications']:
            st.markdown("**Publications:**")
            for pub in cv_data['publications'][:3]:  # Show first 3 publications
                st.write(f"• {pub['title']} ({pub['year']})")

        st.markdown('</div>', unsafe_allow_html=True)

    # Export functionality
    st.subheader("💾 Export Options")
    st.markdown('<div class="export-section">', unsafe_allow_html=True)

    # PDF Template Selection
    st.subheader("📄 PDF Export Templates")
    template_col1, template_col2 = st.columns(2)

    with template_col1:
        pdf_template = st.selectbox(
            "Choose PDF Template Style:",
            ["Professional Blue", "Academic Classic", "Modern Minimal", "Scientific Research"],
            help="Select a template that best fits your career focus"
        )

        # Template descriptions
        template_descriptions = {
            "Professional Blue": "Corporate/Industry focused with blue accents",
            "Academic Classic": "Traditional academic format with conservative styling",
            "Modern Minimal": "Clean, contemporary design with minimal borders",
            "Scientific Research": "Research-focused with green accents"
        }
        st.info(template_descriptions[pdf_template])

    with template_col2:
        pdf_format = st.selectbox(
            "PDF Format:",
            ["A4", "Letter"],
            help="Choose page size for your CV"
        )

        compression_level = st.selectbox(
            "Compression Level:",
            ["Standard", "High Quality", "Web Optimized"],
            help="Balance between file size and quality"
        )

    # Export buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📄 Generate & Download PDF", type="primary"):
            with st.spinner("Generating PDF..."):
                pdf_file = generate_pdf_cv(cv_data, template=pdf_template, page_format=pdf_format)
                if pdf_file:
                    filename = f"{personal['full_name'].replace(' ', '_')}_CV_{pdf_template.replace(' ', '_')}.pdf"
                    st.download_button(
                        label="⬇️ Download PDF",
                        data=pdf_file,
                        file_name=filename,
                        mime="application/pdf",
                        help="Click to download your formatted CV"
                    )
                    display_success_message("PDF generated successfully!")

    with col2:
        # Export as JSON
        json_data = json.dumps(cv_data, indent=2, default=str)
        filename_json = f"{personal['full_name'].replace(' ', '_')}_CV_data.json" if personal['full_name'] else "CV_data.json"
        st.download_button(
            label="💾 Export Data (JSON)",
            data=json_data,
            file_name=filename_json,
            mime="application/json",
            help="Export your CV data for backup or transfer"
        )

    with col3:
        # Import JSON data
        uploaded_json = st.file_uploader(
            "📂 Import CV Data",
            type=['json'],
            help="Import previously exported CV data"
        )
        if uploaded_json is not None:
            try:
                imported_data = json.load(uploaded_json)
                st.session_state.cv_data = imported_data
                display_success_message("CV data imported successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error importing data: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

    # Data Statistics
    st.subheader("📊 CV Statistics")
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

    with stats_col1:
        st.metric("Education Entries", len(cv_data['education']))

    with stats_col2:
        st.metric("Work Experience", len(cv_data['experience']))

    with stats_col3:
        st.metric("Projects", len(cv_data['projects']))

    with stats_col4:
        st.metric("Publications", len(cv_data['publications']))

    # Completion checklist
    st.subheader("✅ Completion Checklist")
    completion_items = [
        ("Personal Information", bool(personal.get('full_name') and personal.get('email'))),
        ("Professional Summary", bool(personal.get('summary'))),
        ("Education", bool(cv_data['education'])),
        ("Work Experience", bool(cv_data['experience'])),
        ("Technical Skills", bool(any(cv_data['skills'].values()))),
        ("Projects", bool(cv_data['projects'])),
        ("Publications", bool(cv_data['publications']))
    ]

    completed = sum(1 for _, status in completion_items if status)
    total = len(completion_items)
    completion_percentage = (completed / total) * 100

    st.progress(completion_percentage / 100)
    st.write(f"CV Completion: {completed}/{total} sections ({completion_percentage:.1f}%)")

    for item, status in completion_items:
        icon = "✅" if status else "⬜"
        st.write(f"{icon} {item}")

    return cv_data