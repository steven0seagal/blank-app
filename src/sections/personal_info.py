"""
Personal Information section for CV Builder.
"""

import streamlit as st
from PIL import Image
from src.utils.styles import display_section_header


def personal_info_section():
    """Render the personal information section"""
    display_section_header("👤 Personal Information")

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
            "Full Name",
            value=personal_info["full_name"],
            help="Enter your full professional name",
        )

        personal_info["title"] = st.text_input(
            "Professional Title",
            value=personal_info["title"],
            placeholder="e.g., PhD Bioinformatician | Computational Biology Researcher",
            help="Your current title or the position you're seeking",
        )

        col2_1, col2_2 = st.columns(2)
        with col2_1:
            personal_info["email"] = st.text_input(
                "Email", value=personal_info["email"], help="Professional email address"
            )
            personal_info["phone"] = st.text_input(
                "Phone", value=personal_info["phone"], help="Contact phone number"
            )

        with col2_2:
            personal_info["location"] = st.text_input(
                "Location", value=personal_info["location"], help="City, State/Country"
            )
            personal_info["linkedin"] = st.text_input(
                "LinkedIn",
                value=personal_info["linkedin"],
                placeholder="https://linkedin.com/in/username",
                help="LinkedIn profile URL",
            )

            # Display clickable LinkedIn link if provided
            if personal_info["linkedin"]:
                st.markdown(f"🔗 [View LinkedIn Profile]({personal_info['linkedin']})")

        personal_info["github"] = st.text_input(
            "GitHub",
            value=personal_info["github"],
            placeholder="https://github.com/username",
            help="GitHub profile URL",
        )

        # Display clickable GitHub link if provided
        if personal_info["github"]:
            st.markdown(f"🔗 [View GitHub Profile]({personal_info['github']})")

        personal_info["orcid"] = st.text_input(
            "ORCID ID",
            value=personal_info["orcid"],
            help="Your ORCID identifier for academic publications",
        )

        personal_info["website"] = st.text_input(
            "Personal Website",
            value=personal_info["website"],
            help="Personal or professional website URL",
        )

        personal_info["summary"] = st.text_area(
            "Professional Summary",
            value=personal_info["summary"],
            height=150,
            placeholder="Write a compelling summary of your expertise in bioinformatics, computational biology, and programming...",
            help="A brief overview of your professional background, key skills, and career objectives (2-3 sentences)",
        )

    return personal_info
