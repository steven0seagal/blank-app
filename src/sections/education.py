"""
Education section for CV Builder.
"""

import streamlit as st
from src.utils.styles import display_section_header, display_success_message
from src.models.cv_data import validate_education_entry


def education_section():
    """Render the education section"""
    display_section_header("🎓 Education")

    education_list = st.session_state.cv_data["education"]

    # Add new education entry
    with st.expander("➕ Add New Education Entry"):
        with st.form("education_form"):
            st.markdown("### Add Education Details")

            col1, col2 = st.columns(2)
            with col1:
                degree = st.text_input(
                    "Degree",
                    placeholder="e.g., PhD in Bioinformatics",
                    help="Full degree title",
                )
                institution = st.text_input(
                    "Institution",
                    placeholder="e.g., University Name",
                    help="Name of the educational institution",
                )
                location = st.text_input(
                    "Location",
                    placeholder="City, Country",
                    help="Location of the institution",
                )

            with col2:
                start_year = st.number_input(
                    "Start Year",
                    min_value=1900,
                    max_value=2030,
                    value=2020,
                    help="Year you started the program",
                )
                end_year = st.number_input(
                    "End Year",
                    min_value=1900,
                    max_value=2030,
                    value=2024,
                    help="Year you completed/will complete",
                )
                gpa = st.text_input(
                    "GPA/Grade (optional)", help="Your GPA or final grade if notable"
                )

            thesis_title = st.text_input(
                "Thesis/Dissertation Title (if applicable)",
                help="Title of your thesis or dissertation",
            )
            advisor = st.text_input(
                "Advisor/Supervisor (if applicable)",
                help="Name of your thesis advisor or supervisor",
            )

            description = st.text_area(
                "Description/Achievements",
                placeholder="Key courses, research focus, honors, etc.",
                help="Notable coursework, research areas, academic achievements",
            )

            if st.form_submit_button("Add Education Entry", type="primary"):
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

                # Validate entry
                errors = validate_education_entry(new_education)
                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    education_list.append(new_education)
                    display_success_message("Education entry added successfully!")
                    st.rerun()

    # Display existing education entries
    if education_list:
        st.subheader("Current Education Entries:")
        for i, edu in enumerate(education_list):
            with st.container():
                col1, col2 = st.columns([4, 1])

                with col1:
                    st.markdown(f"**{edu['degree']}** - {edu['institution']}")
                    st.write(
                        f"📅 {edu['start_year']} - {edu['end_year']} | 📍 {edu['location']}"
                    )

                    if edu["thesis_title"]:
                        st.write(f"📋 **Thesis:** {edu['thesis_title']}")
                    if edu["advisor"]:
                        st.write(f"👨‍🏫 **Advisor:** {edu['advisor']}")
                    if edu["gpa"]:
                        st.write(f"📊 **GPA:** {edu['gpa']}")
                    if edu["description"]:
                        st.write(edu["description"])

                with col2:
                    if st.button(f"🗑️ Remove", key=f"remove_edu_{i}"):
                        education_list.pop(i)
                        st.rerun()

                st.divider()
    else:
        st.info(
            "No education entries added yet. Use the form above to add your academic credentials."
        )

    return education_list
