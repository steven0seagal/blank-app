"""
Projects section for CV Builder.
"""

import streamlit as st
from datetime import datetime
from src.utils.styles import display_section_header, display_success_message
from src.models.cv_data import validate_project_entry

def projects_section():
    """Render the projects section"""
    display_section_header("🚀 Projects")

    projects_list = st.session_state.cv_data['projects']

    # Add new project
    with st.expander("➕ Add New Project"):
        with st.form("project_form"):
            st.markdown("### Add Project Details")

            col1, col2 = st.columns(2)
            with col1:
                project_name = st.text_input(
                    "Project Name",
                    help="Name of your project or research"
                )
                project_type = st.selectbox(
                    "Project Type",
                    ["Research Project", "Software Development", "Data Analysis", "Web Application", "Publication", "Other"],
                    help="Category that best describes your project"
                )

            with col2:
                start_date = st.date_input(
                    "Start Date",
                    key="proj_start",
                    help="When you started working on this project"
                )
                end_date = st.date_input(
                    "End Date",
                    key="proj_end",
                    value=datetime.now(),
                    help="When the project was completed"
                )
                ongoing = st.checkbox(
                    "Ongoing Project",
                    help="Check if the project is still in progress"
                )

            technologies = st.text_input(
                "Technologies Used",
                placeholder="Python, R, Docker, AWS, etc.",
                help="List the main technologies, tools, and platforms used"
            )

            col3, col4 = st.columns(2)
            with col3:
                github_link = st.text_input(
                    "GitHub/Repository Link (optional)",
                    help="Link to the project repository"
                )
            with col4:
                publication_link = st.text_input(
                    "Publication/Demo Link (optional)",
                    help="Link to publication, demo, or project page"
                )

            description = st.text_area(
                "Project Description",
                height=120,
                placeholder="Describe the project objectives, methods, results, and impact...",
                help="Detailed description of what the project involved and what you accomplished"
            )

            if st.form_submit_button("Add Project", type="primary"):
                new_project = {
                    'name': project_name,
                    'type': project_type,
                    'start_date': start_date.strftime("%Y-%m-%d"),
                    'end_date': "Ongoing" if ongoing else end_date.strftime("%Y-%m-%d"),
                    'technologies': technologies,
                    'github_link': github_link,
                    'publication_link': publication_link,
                    'description': description
                }

                # Validate entry
                errors = validate_project_entry(new_project)
                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    projects_list.append(new_project)
                    display_success_message("Project added successfully!")
                    st.rerun()

    # Display projects
    if projects_list:
        st.subheader("Current Projects:")
        for i, project in enumerate(projects_list):
            with st.container():
                col1, col2 = st.columns([4, 1])

                with col1:
                    st.markdown(f"**{project['name']}** - {project['type']}")
                    st.write(f"📅 {project['start_date']} - {project['end_date']}")

                    if project['technologies']:
                        st.write(f"🛠️ **Technologies:** {project['technologies']}")

                    if project['github_link']:
                        st.write(f"🔗 [GitHub Repository]({project['github_link']})")

                    if project['publication_link']:
                        st.write(f"📄 [Publication/Demo]({project['publication_link']})")

                    if project['description']:
                        st.write(project['description'])

                with col2:
                    if st.button(f"🗑️ Remove", key=f"remove_proj_{i}"):
                        projects_list.pop(i)
                        st.rerun()

                st.divider()
    else:
        st.info("No projects added yet. Use the form above to showcase your research and development work.")

    return projects_list