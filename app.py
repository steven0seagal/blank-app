"""
Professional CV Builder for Bioinformaticians - Main Application
A comprehensive Streamlit-based CV builder specifically designed for PhD bioinformaticians,
computational biologists, and researchers.
"""

import streamlit as st
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.models.cv_data import init_cv_data
from src.utils.styles import load_css, display_main_header
from src.sections.personal_info import personal_info_section
from src.sections.education import education_section
from src.sections.experience import experience_section
from src.sections.skills import skills_section
from src.sections.projects import projects_section
from src.sections.publications import publications_section
from src.sections.certifications_awards import certifications_awards_section
from src.sections.preview_export import preview_export_section

# Page configuration
st.set_page_config(
    page_title="Professional CV Builder",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)


def init_session_state():
    """Initialize all session state variables"""
    if "cv_data" not in st.session_state:
        st.session_state.cv_data = init_cv_data()

    if "current_section" not in st.session_state:
        st.session_state.current_section = "Personal Information"


def main():
    """Main application function"""
    # Initialize session state and load CSS
    init_session_state()
    load_css()

    # Main title
    display_main_header("🧬 Professional CV Builder for Bioinformaticians")

    # Sidebar navigation
    st.sidebar.title("📋 CV Sections")
    st.sidebar.markdown(
        """
    Navigate through different sections to build your comprehensive CV.
    All data is automatically saved during your session.
    """
    )

    sections = [
        "Personal Information",
        "Education",
        "Work Experience",
        "Skills",
        "Projects",
        "Publications",
        "Certifications & Awards",
        "Preview & Export",
    ]

    selected_section = st.sidebar.radio(
        "Navigate to:", sections, help="Select a section to edit your CV"
    )
    st.session_state.current_section = selected_section

    # Progress indicator in sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Progress")

    # Calculate completion progress
    cv_data = st.session_state.cv_data
    personal = cv_data["personal_info"]

    progress_items = [
        ("Personal Info", bool(personal.get("full_name") and personal.get("email"))),
        ("Education", bool(cv_data["education"])),
        ("Experience", bool(cv_data["experience"])),
        ("Skills", bool(any(cv_data["skills"].values()))),
        ("Projects", bool(cv_data["projects"])),
        ("Publications", bool(cv_data["publications"])),
        ("Certifications", bool(cv_data["certifications"] or cv_data["awards"])),
    ]

    completed = sum(1 for _, status in progress_items if status)
    total = len(progress_items)
    progress_percentage = (completed / total) * 100

    st.sidebar.progress(progress_percentage / 100)
    st.sidebar.write(
        f"Completion: {completed}/{total} sections ({progress_percentage:.1f}%)"
    )

    # Show completion status for each section
    for item, status in progress_items:
        icon = "✅" if status else "⬜"
        st.sidebar.write(f"{icon} {item}")

    # Add helpful tips in sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("💡 Tips")

    tips = [
        "💾 Your data is automatically saved during your session",
        "📤 Export your data as JSON for backup",
        "📄 Choose from 4 professional PDF templates",
        "🔗 Add LinkedIn and GitHub links for networking",
        "🎓 Include your ORCID for academic credibility",
        "🚀 Showcase your bioinformatics projects with GitHub links",
    ]

    for tip in tips:
        st.sidebar.write(tip)

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
    elif selected_section == "Preview & Export":
        preview_export_section()

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #666; font-size: 0.9em; padding: 1em;">
            🧬 Professional CV Builder for Bioinformaticians<br>
            Built with ❤️ for the computational biology community<br>
            Powered by Streamlit | Export to PDF with multiple professional templates
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
