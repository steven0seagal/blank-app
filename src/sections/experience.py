"""
Work Experience section for CV Builder.
"""

import streamlit as st
from datetime import datetime
from src.utils.styles import display_section_header, display_success_message
from src.models.cv_data import validate_experience_entry


def experience_section():
    """Render the work experience section"""
    display_section_header("💼 Work Experience")

    experience_list = st.session_state.cv_data["experience"]

    # Add new experience entry
    with st.expander("➕ Add New Work Experience"):
        with st.form("experience_form"):
            st.markdown("### Add Work Experience")

            col1, col2 = st.columns(2)
            with col1:
                job_title = st.text_input(
                    "Job Title",
                    placeholder="e.g., Senior Bioinformatics Analyst",
                    help="Your official job title",
                )
                company = st.text_input(
                    "Company/Institution",
                    placeholder="e.g., Biotech Company",
                    help="Name of the organization",
                )
                location = st.text_input(
                    "Location",
                    placeholder="City, Country",
                    help="Location where you worked",
                )

            with col2:
                start_date = st.date_input(
                    "Start Date", help="When you started this position"
                )
                end_date = st.date_input(
                    "End Date",
                    value=datetime.now(),
                    help="When you left or will leave this position",
                )
                current_job = st.checkbox(
                    "This is my current position",
                    help="Check if you currently work in this role",
                )

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
                help="Type of employment",
            )

            description = st.text_area(
                "Job Description & Achievements",
                height=150,
                placeholder="• Analyzed genomic data using Python and R\n• Developed bioinformatics pipelines\n• Published research findings...",
                help="Detailed description of your responsibilities and achievements (use bullet points)",
            )

            if st.form_submit_button("Add Experience", type="primary"):
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

                # Validate entry
                errors = validate_experience_entry(new_experience)
                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    experience_list.append(new_experience)
                    display_success_message("Work experience added successfully!")
                    st.rerun()

    # Display existing experience
    if experience_list:
        st.subheader("Current Work Experience:")
        for i, exp in enumerate(experience_list):
            with st.container():
                col1, col2 = st.columns([4, 1])

                with col1:
                    st.markdown(f"**{exp['job_title']}** - {exp['company']}")
                    st.write(
                        f"📅 {exp['start_date']} - {exp['end_date']} | 📍 {exp['location']} | 💼 {exp['job_type']}"
                    )

                    if exp["description"]:
                        # Format description with proper line breaks
                        formatted_description = exp["description"].replace("\n", "\n\n")
                        st.markdown(formatted_description)

                with col2:
                    if st.button(f"🗑️ Remove", key=f"remove_exp_{i}"):
                        experience_list.pop(i)
                        st.rerun()

                st.divider()
    else:
        st.info(
            "No work experience entries added yet. Use the form above to add your professional experience."
        )

    return experience_list
