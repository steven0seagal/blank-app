import json

import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Professional CV Builder",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Initialize session state
def init_session_state():
    """Initialize all session state variables"""
    if "cv_data" not in st.session_state:
        st.session_state.cv_data = {
            "personal_info": {
                "full_name": "",
                "title": "",
                "email": "",
                "phone": "",
                "location": "",
                "linkedin": "",
                "github": "",
                "orcid": "",
                "website": "",
                "summary": "",
            },
            "photo": None,
            "education": [],
            "experience": [],
            "skills": {
                "programming_languages": [],
                "bioinformatics_tools": [],
                "statistical_software": [],
                "databases": [],
                "cloud_platforms": [],
                "other_technical": [],
            },
            "projects": [],
            "publications": [],
            "certifications": [],
            "awards": [],
        }

    if "current_section" not in st.session_state:
        st.session_state.current_section = "Personal Information"


# Custom CSS for professional styling
def load_css():
    st.markdown(
        """
    <style>
    .main-header {
        font-size: 2.5em;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 1em;
        font-weight: 600;
    }

    .section-header {
        font-size: 1.8em;
        color: #1e40af;
        margin-top: 1.5em;
        margin-bottom: 0.8em;
        border-bottom: 2px solid #3b82f6;
        padding-bottom: 0.3em;
    }

    .info-card {
        background-color: #f8fafc;
        padding: 1.2em;
        border-radius: 0.5em;
        border-left: 4px solid #3b82f6;
        margin: 1em 0;
    }

    .skill-tag {
        display: inline-block;
        background-color: #dbeafe;
        color: #1e40af;
        padding: 0.3em 0.8em;
        border-radius: 1em;
        margin: 0.2em;
        font-size: 0.9em;
    }

    .stButton > button {
        background-color: #3b82f6;
        color: white;
        border-radius: 0.3em;
        border: none;
        padding: 0.5em 1em;
        font-weight: 500;
    }

    .stButton > button:hover {
        background-color: #1e40af;
        border: none;
        color: white;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


def main():
    init_session_state()
    load_css()

    # Main title
    st.markdown(
        '<h1 class="main-header">🧬 Professional CV Builder for Bioinformaticians</h1>',
        unsafe_allow_html=True,
    )

    # Initialize main section in session state
    if "main_section" not in st.session_state:
        st.session_state.main_section = "CV Preview"

    # Main navigation
    main_sections = ["CV Preview", "Edit CV"]
    selected_main = st.sidebar.radio(
        "Main Sections",
        main_sections,
        index=main_sections.index(st.session_state.main_section),
    )

    # Update session state when user manually selects from radio button
    if selected_main != st.session_state.main_section:
        st.session_state.main_section = selected_main

    if st.session_state.main_section == "CV Preview":
        cv_preview_main_page()
    else:
        # Sub-navigation for editing sections
        st.sidebar.title("📋 CV Edit Sections")

        edit_sections = [
            "Personal Information",
            "Education",
            "Work Experience",
            "Skills",
            "Projects",
            "Publications",
            "Certifications & Awards",
            "Export Options",
        ]

        selected_section = st.sidebar.radio("Edit Section:", edit_sections)
        st.session_state.current_section = selected_section

        # Main content area based on selected section
        if selected_section == "Personal Information":
            personal_info_section()
        elif selected_section == "Education":
            education_section()
        elif selected_section == "Work Experience":
            experience_section()
        elif selected_section == "Skills":
            skills_section()
        elif selected_section == "Projects":
            projects_section()
        elif selected_section == "Publications":
            publications_section()
        elif selected_section == "Certifications & Awards":
            certifications_awards_section()
        elif selected_section == "Export Options":
            export_section()


def cv_preview_main_page():
    """Display the main CV preview page"""
    st.markdown(
        '<h2 class="section-header">👀 Your Professional CV</h2>',
        unsafe_allow_html=True,
    )

    cv_data = st.session_state.cv_data
    personal = cv_data["personal_info"]

    # Check if CV has any data
    has_basic_info = any(
        [
            personal["full_name"],
            personal["email"],
            cv_data["education"],
            cv_data["experience"],
        ]
    )

    if not has_basic_info:
        st.info(
            "🚀 Get started by editing your CV information in the 'Edit CV' section!"
        )
        st.markdown("### Quick Start Guide:")
        st.markdown(
            """
        1. **Personal Information** - Add your name, contact details, and
           professional summary
        2. **Education** - Include your degrees and academic background
        3. **Work Experience** - List your professional experience
        4. **Skills** - Showcase your technical abilities
        5. **Projects & Publications** - Highlight your research and
           development work
        """
        )
        return

    # Display CV Preview
    col1, col2 = st.columns([2, 1])

    with col1:
        # Header section
        if personal["full_name"]:
            st.markdown(f"# {personal['full_name']}")

        if personal["title"]:
            st.markdown(f"### *{personal['title']}*")

        # Contact information in a clean layout
        contact_info = []
        if personal["email"]:
            contact_info.append(f"📧 {personal['email']}")
        if personal["phone"]:
            contact_info.append(f"📱 {personal['phone']}")
        if personal["location"]:
            contact_info.append(f"📍 {personal['location']}")

        if contact_info:
            st.markdown(" | ".join(contact_info))

        # Links
        links = []
        if personal["linkedin"]:
            links.append(f"[LinkedIn]({personal['linkedin']})")
        if personal["github"]:
            links.append(f"[GitHub]({personal['github']})")
        if personal["orcid"]:
            links.append(f"[ORCID]({personal['orcid']})")
        if personal["website"]:
            links.append(f"[Website]({personal['website']})")

        if links:
            st.markdown(" • ".join(links))

        st.divider()

        # Professional Summary
        if personal["summary"]:
            st.markdown("## 📝 Professional Summary")
            st.markdown(
                f'<div class="info-card">{personal["summary"]}</div>',
                unsafe_allow_html=True,
            )

        # Technical Skills
        if any(cv_data["skills"].values()):
            st.markdown("## 🛠️ Technical Skills")

            skills_cols = st.columns(2)
            skill_categories = list(cv_data["skills"].items())

            for i, (category, skills_list) in enumerate(skill_categories):
                if skills_list:
                    col_idx = i % 2
                    with skills_cols[col_idx]:
                        category_name = category.replace("_", " ").title()
                        st.markdown(f"**{category_name}:**")
                        skills_html = ""
                        for skill in skills_list:
                            skills_html += f'<span class="skill-tag">{skill}</span>'
                        st.markdown(skills_html, unsafe_allow_html=True)
                        st.markdown("")

        # Education
        if cv_data["education"]:
            st.markdown("## 🎓 Education")
            for edu in cv_data["education"]:
                st.markdown('<div class="info-card">', unsafe_allow_html=True)
                st.markdown(f"**{edu['degree']}**")
                st.markdown(f"*{edu['institution']}* • {edu['location']}")
                st.markdown(f"📅 {edu['start_year']} - {edu['end_year']}")

                if edu["thesis_title"]:
                    st.markdown(f"**Thesis:** {edu['thesis_title']}")
                if edu["advisor"]:
                    st.markdown(f"**Advisor:** {edu['advisor']}")
                if edu["gpa"]:
                    st.markdown(f"**GPA:** {edu['gpa']}")
                if edu["description"]:
                    st.markdown(edu["description"])
                st.markdown("</div>", unsafe_allow_html=True)

        # Work Experience
        if cv_data["experience"]:
            st.markdown("## 💼 Work Experience")
            for exp in cv_data["experience"]:
                st.markdown('<div class="info-card">', unsafe_allow_html=True)
                st.markdown(f"**{exp['job_title']}**")
                st.markdown(f"*{exp['company']}* • {exp['location']}")
                st.markdown(
                    f"📅 {exp['start_date']} - {exp['end_date']} • {exp['job_type']}"
                )
                if exp["description"]:
                    st.markdown(exp["description"])
                st.markdown("</div>", unsafe_allow_html=True)

        # Projects
        if cv_data["projects"]:
            st.markdown("## 🚀 Projects")
            for project in cv_data["projects"]:
                st.markdown('<div class="info-card">', unsafe_allow_html=True)
                st.markdown(f"**{project['name']}** - *{project['type']}*")
                st.markdown(f"📅 {project['start_date']} - {project['end_date']}")

                if project["technologies"]:
                    st.markdown(f"**Technologies:** {project['technologies']}")

                links = []
                if project["github_link"]:
                    links.append(f"[GitHub]({project['github_link']})")
                if project["publication_link"]:
                    links.append(f"[Publication]({project['publication_link']})")
                if links:
                    st.markdown(" • ".join(links))

                if project["description"]:
                    st.markdown(project["description"])
                st.markdown("</div>", unsafe_allow_html=True)

        # Publications
        if cv_data["publications"]:
            st.markdown("## 📚 Publications")
            for pub in cv_data["publications"]:
                st.markdown('<div class="info-card">', unsafe_allow_html=True)
                st.markdown(f"**{pub['title']}**")
                st.markdown(f"*{pub['authors']}*")
                st.markdown(f"📖 {pub['journal']} ({pub['year']})")

                if pub["volume"] and pub["pages"]:
                    st.markdown(f"Vol. {pub['volume']}, pp. {pub['pages']}")
                if pub["doi"]:
                    st.markdown(f"DOI: {pub['doi']}")
                if pub["url"]:
                    st.markdown(f"[Read Publication]({pub['url']})")
                st.markdown("</div>", unsafe_allow_html=True)

        # Certifications & Awards
        if cv_data["certifications"]:
            st.markdown("## 📜 Certifications")
            for cert in cv_data["certifications"]:
                st.markdown('<div class="info-card">', unsafe_allow_html=True)
                st.markdown(f"**{cert['name']}**")
                st.markdown(f"*{cert['issuing_org']}*")
                st.markdown(
                    f"📅 Issued: {cert['issue_date']} • Expires: {cert['expiry_date']}"
                )
                if cert["url"]:
                    st.markdown(f"[View Credential]({cert['url']})")
                st.markdown("</div>", unsafe_allow_html=True)

        if cv_data["awards"]:
            st.markdown("## 🏆 Awards & Honors")
            for award in cv_data["awards"]:
                st.markdown('<div class="info-card">', unsafe_allow_html=True)
                st.markdown(f"**{award['name']}**")
                st.markdown(f"*{award['awarding_org']}*")
                st.markdown(f"📅 {award['date']}")
                if award["description"]:
                    st.markdown(award["description"])
                st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("### 🎯 Quick Actions")

        # Quick edit buttons
        edit_buttons = [
            ("✏️ Edit Personal Info", "Personal Information"),
            ("🎓 Edit Education", "Education"),
            ("💼 Edit Experience", "Work Experience"),
            ("🛠️ Edit Skills", "Skills"),
            ("🚀 Edit Projects", "Projects"),
            ("📚 Edit Publications", "Publications"),
        ]

        for button_text, section in edit_buttons:
            if st.button(button_text, use_container_width=True):
                st.session_state.current_section = section
                st.session_state.main_section = "Edit CV"  # Switch to Edit CV section
                st.rerun()

        st.divider()

        # Export section
        st.markdown("### 📄 Export CV")

        if st.button("📥 Export Options", type="primary", use_container_width=True):
            st.session_state.current_section = "Export Options"
            st.session_state.main_section = "Edit CV"  # Switch to Edit CV section
            st.rerun()

        # Quick stats
        st.markdown("### 📊 CV Stats")
        stats_data = {
            "Education": len(cv_data["education"]),
            "Experience": len(cv_data["experience"]),
            "Projects": len(cv_data["projects"]),
            "Publications": len(cv_data["publications"]),
            "Certifications": len(cv_data["certifications"]),
            "Awards": len(cv_data["awards"]),
        }

        for stat_name, count in stats_data.items():
            if count > 0:
                st.markdown(f"**{stat_name}:** {count}")


def export_section():
    """Separated export functionality"""
    st.markdown(
        '<h2 class="section-header">📄 Export & Import</h2>', unsafe_allow_html=True
    )

    cv_data = st.session_state.cv_data
    personal = cv_data["personal_info"]

    # PDF Template Selection
    st.subheader("📄 PDF Export Templates")
    template_col1, template_col2 = st.columns(2)

    with template_col1:
        pdf_template = st.selectbox(
            "Choose PDF Template Style:",
            [
                "Professional Blue",
                "Academic Classic",
                "Modern Minimal",
                "Scientific Research",
            ],
            help="Select a template that best fits your career focus",
        )

    with template_col2:
        pdf_format = st.selectbox(
            "PDF Format:", ["A4", "Letter"], help="Choose page size for your CV"
        )

    # Export buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📄 Generate & Download PDF", type="primary"):
            pdf_file = generate_pdf_cv(
                cv_data, template=pdf_template, page_format=pdf_format
            )
            if pdf_file:
                filename = (
                    f"{personal['full_name'].replace(' ', '_')}_CV_"
                    f"{pdf_template.replace(' ', '_')}.pdf"
                )
                st.download_button(
                    label="⬇️ Download PDF",
                    data=pdf_file,
                    file_name=filename,
                    mime="application/pdf",
                )

    with col2:
        # Export as JSON
        json_data = json.dumps(cv_data, indent=2, default=str)
        st.download_button(
            label="💾 Export Data (JSON)",
            data=json_data,
            file_name=(f"{personal['full_name'].replace(' ', '_')}_CV_data.json"),
            mime="application/json",
        )

    with col3:
        # Import JSON data
        uploaded_json = st.file_uploader("📂 Import CV Data", type=["json"])
        if uploaded_json is not None:
            try:
                imported_data = json.load(uploaded_json)
                st.session_state.cv_data = imported_data
                st.success("CV data imported successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error importing data: {e}")


def personal_info_section():
    st.markdown(
        '<h2 class="section-header">👤 Personal Information</h2>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📸 Profile Photo")
        uploaded_file = st.file_uploader(
            "Upload your professional photo", type=["png", "jpg", "jpeg"]
        )

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Your Photo", width=200)
            st.session_state.cv_data["photo"] = uploaded_file
        elif st.session_state.cv_data.get("photo"):
            st.image(
                st.session_state.cv_data["photo"], caption="Current Photo", width=200
            )

    with col2:
        st.subheader("📝 Basic Information")

        personal_info = st.session_state.cv_data["personal_info"]

        personal_info["full_name"] = st.text_input(
            "Full Name", value=personal_info["full_name"]
        )
        personal_info["title"] = st.text_input(
            "Professional Title",
            value=personal_info["title"],
            placeholder=(
                "e.g., PhD Bioinformatician | Computational Biology Researcher"
            ),
        )

        col2_1, col2_2 = st.columns(2)
        with col2_1:
            personal_info["email"] = st.text_input(
                "Email", value=personal_info["email"]
            )
            personal_info["phone"] = st.text_input(
                "Phone", value=personal_info["phone"]
            )

        with col2_2:
            personal_info["location"] = st.text_input(
                "Location", value=personal_info["location"]
            )
            personal_info["linkedin"] = st.text_input(
                "LinkedIn", value=personal_info["linkedin"]
            )

        personal_info["github"] = st.text_input("GitHub", value=personal_info["github"])
        personal_info["orcid"] = st.text_input("ORCID ID", value=personal_info["orcid"])
        personal_info["website"] = st.text_input(
            "Personal Website", value=personal_info["website"]
        )

        personal_info["summary"] = st.text_area(
            "Professional Summary",
            value=personal_info["summary"],
            height=150,
            placeholder=(
                "Write a compelling summary of your expertise in bioinformatics, "
                "computational biology, and programming..."
            ),
        )


def education_section():
    st.markdown('<h2 class="section-header">🎓 Education</h2>', unsafe_allow_html=True)

    education_list = st.session_state.cv_data["education"]

    # Add new education entry
    with st.expander("➕ Add New Education Entry"):
        with st.form("education_form"):
            degree = st.text_input("Degree", placeholder="e.g., PhD in Bioinformatics")
            institution = st.text_input(
                "Institution", placeholder="e.g., University Name"
            )
            location = st.text_input("Location", placeholder="City, Country")
            start_year = st.number_input(
                "Start Year", min_value=1900, max_value=2030, value=2020
            )
            end_year = st.number_input(
                "End Year", min_value=1900, max_value=2030, value=2024
            )
            thesis_title = st.text_input("Thesis/Dissertation Title (if applicable)")
            advisor = st.text_input("Advisor/Supervisor (if applicable)")
            gpa = st.text_input("GPA/Grade (optional)")
            description = st.text_area(
                "Description/Achievements",
                placeholder="Key courses, research focus, honors, etc.",
            )

            if st.form_submit_button("Add Education Entry"):
                new_education = {
                    "degree": degree,
                    "institution": institution,
                    "location": location,
                    "start_year": start_year,
                    "end_year": end_year,
                    "thesis_title": thesis_title,
                    "advisor": advisor,
                    "gpa": gpa,
                    "description": description,
                }
                education_list.append(new_education)
                st.success("Education entry added!")
                st.rerun()

    # Display existing education entries
    if education_list:
        st.subheader("Current Education Entries:")
        for i, edu in enumerate(education_list):
            with st.container():
                st.markdown(f"**{edu['degree']}** - {edu['institution']}")
                st.write(
                    f"📅 {edu['start_year']} - {edu['end_year']} | 📍 {edu['location']}"
                )
                if edu["thesis_title"]:
                    st.write(f"📋 Thesis: {edu['thesis_title']}")
                if edu["advisor"]:
                    st.write(f"👨‍🏫 Advisor: {edu['advisor']}")
                if edu["gpa"]:
                    st.write(f"📊 GPA: {edu['gpa']}")
                if edu["description"]:
                    st.write(edu["description"])

                if st.button("🗑️ Remove", key=f"remove_edu_{i}"):
                    education_list.pop(i)
                    st.rerun()
                st.divider()


def experience_section():
    st.markdown(
        '<h2 class="section-header">💼 Work Experience</h2>', unsafe_allow_html=True
    )

    experience_list = st.session_state.cv_data["experience"]

    # Add new experience entry
    with st.expander("➕ Add New Work Experience"):
        with st.form("experience_form"):
            job_title = st.text_input(
                "Job Title", placeholder="e.g., Senior Bioinformatics Analyst"
            )
            company = st.text_input(
                "Company/Institution", placeholder="e.g., Biotech Company"
            )
            location = st.text_input("Location", placeholder="City, Country")
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")
            current_job = st.checkbox("This is my current position")
            job_type = st.selectbox(
                "Job Type",
                [
                    "Full-time",
                    "Part-time",
                    "Contract",
                    "Internship",
                    "Fellowship",
                    "Postdoc",
                ],
            )
            description = st.text_area(
                "Job Description & Achievements",
                height=150,
                placeholder=(
                    "• Analyzed genomic data using Python and R\n"
                    "• Developed bioinformatics pipelines\n"
                    "• Published research findings..."
                ),
            )

            if st.form_submit_button("Add Experience"):
                new_experience = {
                    "job_title": job_title,
                    "company": company,
                    "location": location,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": (
                        "Present" if current_job else end_date.strftime("%Y-%m-%d")
                    ),
                    "job_type": job_type,
                    "description": description,
                }
                experience_list.append(new_experience)
                st.success("Experience added!")
                st.rerun()

    # Display existing experience
    if experience_list:
        st.subheader("Current Work Experience:")
        for i, exp in enumerate(experience_list):
            with st.container():
                st.markdown(f"**{exp['job_title']}** - {exp['company']}")
                st.write(
                    f"📅 {exp['start_date']} - {exp['end_date']} | "
                    f"📍 {exp['location']} | 💼 {exp['job_type']}"
                )
                st.write(exp["description"])

                if st.button("🗑️ Remove", key=f"remove_exp_{i}"):
                    experience_list.pop(i)
                    st.rerun()
                st.divider()


def skills_section():
    st.markdown(
        '<h2 class="section-header">🛠️ Technical Skills</h2>', unsafe_allow_html=True
    )

    skills = st.session_state.cv_data["skills"]

    # Programming Languages
    st.subheader("💻 Programming Languages")
    prog_langs_input = st.text_area(
        "Programming Languages (one per line)",
        value="\n".join(skills["programming_languages"]),
        placeholder="Python\nR\nJava\nC++\nJavaScript\nSQL",
    )
    skills["programming_languages"] = [
        lang.strip() for lang in prog_langs_input.split("\n") if lang.strip()
    ]

    # Bioinformatics Tools
    st.subheader("🧬 Bioinformatics Tools & Software")
    bioinfo_tools_input = st.text_area(
        "Bioinformatics Tools (one per line)",
        value="\n".join(skills["bioinformatics_tools"]),
        placeholder="BLAST\nBioconductor\nGalaxy\nGATK\nSamtools\nBedtools",
    )
    skills["bioinformatics_tools"] = [
        tool.strip() for tool in bioinfo_tools_input.split("\n") if tool.strip()
    ]

    # Statistical Software
    st.subheader("📊 Statistical Software")
    stats_software_input = st.text_area(
        "Statistical Software (one per line)",
        value="\n".join(skills["statistical_software"]),
        placeholder="SPSS\nSAS\nStata\nPRISM\nMatlab",
    )
    skills["statistical_software"] = [
        soft.strip() for soft in stats_software_input.split("\n") if soft.strip()
    ]

    # Databases
    st.subheader("🗄️ Databases")
    databases_input = st.text_area(
        "Databases (one per line)",
        value="\n".join(skills["databases"]),
        placeholder="MySQL\nPostgreSQL\nMongoDB\nNCBI\nEnsembl\nUniProt",
    )
    skills["databases"] = [
        db.strip() for db in databases_input.split("\n") if db.strip()
    ]

    # Cloud Platforms
    st.subheader("☁️ Cloud Platforms")
    cloud_input = st.text_area(
        "Cloud Platforms (one per line)",
        value="\n".join(skills["cloud_platforms"]),
        placeholder="AWS\nGoogle Cloud Platform\nMicrosoft Azure\nDocker\nKubernetes",
    )
    skills["cloud_platforms"] = [
        cloud.strip() for cloud in cloud_input.split("\n") if cloud.strip()
    ]

    # Other Technical Skills
    st.subheader("🔧 Other Technical Skills")
    other_input = st.text_area(
        "Other Technical Skills (one per line)",
        value="\n".join(skills["other_technical"]),
        placeholder=(
            "Git/GitHub\nLinux/Unix\nHPC Computing\n"
            "Machine Learning\nData Visualization"
        ),
    )
    skills["other_technical"] = [
        skill.strip() for skill in other_input.split("\n") if skill.strip()
    ]


def projects_section():
    st.markdown('<h2 class="section-header">🚀 Projects</h2>', unsafe_allow_html=True)

    projects_list = st.session_state.cv_data["projects"]

    # Add new project
    with st.expander("➕ Add New Project"):
        with st.form("project_form"):
            project_name = st.text_input("Project Name")
            project_type = st.selectbox(
                "Project Type",
                [
                    "Research Project",
                    "Software Development",
                    "Data Analysis",
                    "Web Application",
                    "Publication",
                    "Other",
                ],
            )
            start_date = st.date_input("Start Date", key="proj_start")
            end_date = st.date_input("End Date", key="proj_end")
            ongoing = st.checkbox("Ongoing Project")
            technologies = st.text_input(
                "Technologies Used", placeholder="Python, R, Docker, AWS, etc."
            )
            github_link = st.text_input("GitHub/Repository Link (optional)")
            publication_link = st.text_input("Publication/Demo Link (optional)")
            description = st.text_area(
                "Project Description",
                height=120,
                placeholder=(
                    "Describe the project objectives, methods, results, and impact..."
                ),
            )

            if st.form_submit_button("Add Project"):
                new_project = {
                    "name": project_name,
                    "type": project_type,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": "Ongoing" if ongoing else end_date.strftime("%Y-%m-%d"),
                    "technologies": technologies,
                    "github_link": github_link,
                    "publication_link": publication_link,
                    "description": description,
                }
                projects_list.append(new_project)
                st.success("Project added!")
                st.rerun()

    # Display projects
    if projects_list:
        st.subheader("Current Projects:")
        for i, project in enumerate(projects_list):
            with st.container():
                st.markdown(f"**{project['name']}** - {project['type']}")
                st.write(f"📅 {project['start_date']} - {project['end_date']}")
                if project["technologies"]:
                    st.write(f"🛠️ Technologies: {project['technologies']}")
                if project["github_link"]:
                    st.write(f"🔗 [GitHub Repository]({project['github_link']})")
                if project["publication_link"]:
                    st.write(f"📄 [Publication/Demo]({project['publication_link']})")
                st.write(project["description"])

                if st.button("🗑️ Remove", key=f"remove_proj_{i}"):
                    projects_list.pop(i)
                    st.rerun()
                st.divider()


def publications_section():
    st.markdown(
        '<h2 class="section-header">📚 Publications</h2>', unsafe_allow_html=True
    )

    publications_list = st.session_state.cv_data["publications"]

    # Add new publication
    with st.expander("➕ Add New Publication"):
        with st.form("publication_form"):
            title = st.text_input("Title")
            authors = st.text_input("Authors", placeholder="Last, F., Last, F., etc.")
            journal = st.text_input("Journal/Conference")
            year = st.number_input("Year", min_value=1900, max_value=2030, value=2024)
            volume = st.text_input("Volume (optional)")
            pages = st.text_input("Pages (optional)")
            doi = st.text_input("DOI (optional)")
            pmid = st.text_input("PMID (optional)")
            url = st.text_input("URL/Link (optional)")
            pub_type = st.selectbox(
                "Publication Type",
                [
                    "Journal Article",
                    "Conference Paper",
                    "Book Chapter",
                    "Preprint",
                    "Poster",
                    "Abstract",
                ],
            )

            if st.form_submit_button("Add Publication"):
                new_publication = {
                    "title": title,
                    "authors": authors,
                    "journal": journal,
                    "year": year,
                    "volume": volume,
                    "pages": pages,
                    "doi": doi,
                    "pmid": pmid,
                    "url": url,
                    "type": pub_type,
                }
                publications_list.append(new_publication)
                st.success("Publication added!")
                st.rerun()

    # Display publications
    if publications_list:
        st.subheader("Publications:")
        for i, pub in enumerate(publications_list):
            with st.container():
                st.markdown(f"**{pub['title']}**")
                st.write(f"👥 {pub['authors']}")
                st.write(f"📖 {pub['journal']} ({pub['year']})")
                if pub["volume"] and pub["pages"]:
                    st.write(f"📄 Vol. {pub['volume']}, pp. {pub['pages']}")
                if pub["doi"]:
                    st.write(f"🔗 DOI: {pub['doi']}")
                if pub["url"]:
                    st.write(f"🌐 [Link]({pub['url']})")
                st.write(f"📋 Type: {pub['type']}")

                if st.button("🗑️ Remove", key=f"remove_pub_{i}"):
                    publications_list.pop(i)
                    st.rerun()
                st.divider()


def certifications_awards_section():
    st.markdown(
        '<h2 class="section-header">🏆 Certifications & Awards</h2>',
        unsafe_allow_html=True,
    )

    # Certifications
    st.subheader("📜 Certifications")
    certifications_list = st.session_state.cv_data["certifications"]

    with st.expander("➕ Add New Certification"):
        with st.form("certification_form"):
            cert_name = st.text_input("Certification Name")
            issuing_org = st.text_input("Issuing Organization")
            issue_date = st.date_input("Issue Date")
            expiry_date = st.date_input("Expiry Date (optional)")
            no_expiry = st.checkbox("No Expiry Date")
            credential_id = st.text_input("Credential ID (optional)")
            cert_url = st.text_input("Certification URL (optional)")

            if st.form_submit_button("Add Certification"):
                new_cert = {
                    "name": cert_name,
                    "issuing_org": issuing_org,
                    "issue_date": issue_date.strftime("%Y-%m-%d"),
                    "expiry_date": (
                        "No Expiry" if no_expiry else expiry_date.strftime("%Y-%m-%d")
                    ),
                    "credential_id": credential_id,
                    "url": cert_url,
                }
                certifications_list.append(new_cert)
                st.success("Certification added!")
                st.rerun()

    if certifications_list:
        for i, cert in enumerate(certifications_list):
            with st.container():
                st.markdown(f"**{cert['name']}**")
                st.write(f"🏢 {cert['issuing_org']}")
                st.write(
                    f"📅 Issued: {cert['issue_date']} | Expires: {cert['expiry_date']}"
                )
                if cert["credential_id"]:
                    st.write(f"🆔 Credential ID: {cert['credential_id']}")
                if cert["url"]:
                    st.write(f"🔗 [View Credential]({cert['url']})")

                if st.button("🗑️ Remove", key=f"remove_cert_{i}"):
                    certifications_list.pop(i)
                    st.rerun()
                st.divider()

    # Awards
    st.subheader("🏅 Awards & Honors")
    awards_list = st.session_state.cv_data["awards"]

    with st.expander("➕ Add New Award"):
        with st.form("award_form"):
            award_name = st.text_input("Award Name")
            awarding_org = st.text_input("Awarding Organization")
            award_date = st.date_input("Date Received")
            award_description = st.text_area("Description (optional)")

            if st.form_submit_button("Add Award"):
                new_award = {
                    "name": award_name,
                    "awarding_org": awarding_org,
                    "date": award_date.strftime("%Y-%m-%d"),
                    "description": award_description,
                }
                awards_list.append(new_award)
                st.success("Award added!")
                st.rerun()

    if awards_list:
        for i, award in enumerate(awards_list):
            with st.container():
                st.markdown(f"**{award['name']}**")
                st.write(f"🏢 {award['awarding_org']}")
                st.write(f"📅 {award['date']}")
                if award["description"]:
                    st.write(award["description"])

                if st.button("🗑️ Remove", key=f"remove_award_{i}"):
                    awards_list.pop(i)
                    st.rerun()
                st.divider()


def generate_pdf_cv(cv_data, template="Professional Blue", page_format="A4"):
    """Generate comprehensive PDF version of the CV with template options"""
    try:
        from io import BytesIO

        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER
        from reportlab.lib.pagesizes import A4, letter
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import inch
        from reportlab.platypus import (
            Paragraph,
            SimpleDocTemplate,
            Spacer,
            Table,
            TableStyle,
        )

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

        # Template-specific color schemes
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

        colors_scheme = template_colors.get(
            template, template_colors["Professional Blue"]
        )

        # Custom styles
        styles = getSampleStyleSheet()

        # Define custom styles based on template
        title_style = ParagraphStyle(
            "CustomTitle",
            parent=styles["Heading1"],
            fontSize=24 if template != "Modern Minimal" else 22,
            spaceAfter=6,
            alignment=TA_CENTER,
            textColor=colors.HexColor(colors_scheme["title"]),
        )

        subtitle_style = ParagraphStyle(
            "CustomSubtitle",
            parent=styles["Heading2"],
            fontSize=14,
            spaceAfter=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor(colors_scheme["subtitle"]),
        )

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

        body_style = ParagraphStyle(
            "CustomBody",
            parent=styles["Normal"],
            fontSize=10,
            spaceBefore=3,
            spaceAfter=3,
            leftIndent=0,
        )

        story = []
        personal = cv_data["personal_info"]

        # Header Section
        if personal["full_name"]:
            title = Paragraph(f"<b>{personal['full_name']}</b>", title_style)
            story.append(title)

        if personal["title"]:
            subtitle = Paragraph(personal["title"], subtitle_style)
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
            story.append(Paragraph("<b>PROFESSIONAL SUMMARY</b>", section_style))
            summary = Paragraph(personal["summary"], body_style)
            story.append(summary)
            story.append(Spacer(1, 6))

        # Technical Skills
        if any(cv_data["skills"].values()):
            story.append(Paragraph("<b>TECHNICAL SKILLS</b>", section_style))

            for category, skills_list in cv_data["skills"].items():
                if skills_list:
                    category_name = category.replace("_", " ").title()
                    skills_text = f"<b>{category_name}:</b> {', '.join(skills_list)}"
                    skills_para = Paragraph(skills_text, body_style)
                    story.append(skills_para)
            story.append(Spacer(1, 6))

        # Education
        if cv_data["education"]:
            story.append(Paragraph("<b>EDUCATION</b>", section_style))
            for edu in cv_data["education"]:
                edu_title = f"<b>{edu['degree']}</b> - {edu['institution']}"
                story.append(Paragraph(edu_title, body_style))

                edu_details = (
                    f"{edu['start_year']} - {edu['end_year']} | {edu['location']}"
                )
                story.append(Paragraph(edu_details, body_style))

                if edu["thesis_title"]:
                    thesis = f"<i>Thesis:</i> {edu['thesis_title']}"
                    story.append(Paragraph(thesis, body_style))

                if edu["advisor"]:
                    advisor = f"<i>Advisor:</i> {edu['advisor']}"
                    story.append(Paragraph(advisor, body_style))

                if edu["gpa"]:
                    gpa = f"<i>GPA:</i> {edu['gpa']}"
                    story.append(Paragraph(gpa, body_style))

                if edu["description"]:
                    story.append(Paragraph(edu["description"], body_style))

                story.append(Spacer(1, 6))

        # Work Experience
        if cv_data["experience"]:
            story.append(Paragraph("<b>WORK EXPERIENCE</b>", section_style))
            for exp in cv_data["experience"]:
                exp_title = f"<b>{exp['job_title']}</b> - {exp['company']}"
                story.append(Paragraph(exp_title, body_style))

                exp_details = (
                    f"{exp['start_date']} - {exp['end_date']} | "
                    f"{exp['location']} | {exp['job_type']}"
                )
                story.append(Paragraph(exp_details, body_style))

                if exp["description"]:
                    story.append(Paragraph(exp["description"], body_style))

                story.append(Spacer(1, 6))

        # Projects
        if cv_data["projects"]:
            story.append(Paragraph("<b>PROJECTS</b>", section_style))
            for project in cv_data["projects"]:
                project_title = f"<b>{project['name']}</b> - {project['type']}"
                story.append(Paragraph(project_title, body_style))

                project_details = f"{project['start_date']} - {project['end_date']}"
                if project["technologies"]:
                    project_details += f" | Technologies: {project['technologies']}"
                story.append(Paragraph(project_details, body_style))

                if project["description"]:
                    story.append(Paragraph(project["description"], body_style))

                if project["github_link"]:
                    github = f"Repository: {project['github_link']}"
                    story.append(Paragraph(github, body_style))

                story.append(Spacer(1, 6))

        # Publications
        if cv_data["publications"]:
            story.append(Paragraph("<b>PUBLICATIONS</b>", section_style))
            for pub in cv_data["publications"]:
                pub_title = f"<b>{pub['title']}</b>"
                story.append(Paragraph(pub_title, body_style))

                pub_details = f"{pub['authors']} ({pub['year']}). {pub['journal']}"
                if pub["volume"] and pub["pages"]:
                    pub_details += f", Vol. {pub['volume']}, pp. {pub['pages']}"
                story.append(Paragraph(pub_details, body_style))

                if pub["doi"]:
                    doi = f"DOI: {pub['doi']}"
                    story.append(Paragraph(doi, body_style))

                story.append(Spacer(1, 6))

        # Certifications
        if cv_data["certifications"]:
            story.append(Paragraph("<b>CERTIFICATIONS</b>", section_style))
            for cert in cv_data["certifications"]:
                cert_title = f"<b>{cert['name']}</b> - {cert['issuing_org']}"
                story.append(Paragraph(cert_title, body_style))

                cert_details = (
                    f"Issued: {cert['issue_date']} | Expires: {cert['expiry_date']}"
                )
                story.append(Paragraph(cert_details, body_style))

                story.append(Spacer(1, 6))

        # Awards
        if cv_data["awards"]:
            story.append(Paragraph("<b>AWARDS & HONORS</b>", section_style))
            for award in cv_data["awards"]:
                award_title = f"<b>{award['name']}</b> - {award['awarding_org']}"
                story.append(Paragraph(award_title, body_style))

                award_details = f"Date: {award['date']}"
                story.append(Paragraph(award_details, body_style))

                if award["description"]:
                    story.append(Paragraph(award["description"], body_style))

                story.append(Spacer(1, 6))

        # Build the PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()

    except Exception as e:
        st.error(f"Error generating PDF: {e}")
        return None


if __name__ == "__main__":
    main()
