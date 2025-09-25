"""
Technical Skills section for CV Builder.
"""

import streamlit as st
from src.utils.styles import display_section_header

def skills_section():
    """Render the technical skills section"""
    display_section_header("🛠️ Technical Skills")

    skills = st.session_state.cv_data['skills']

    st.markdown("""
    **Instructions:** Enter your skills one per line in each category. Focus on tools and technologies
    relevant to bioinformatics and computational biology.
    """)

    col1, col2 = st.columns(2)

    with col1:
        # Programming Languages
        st.subheader("💻 Programming Languages")
        prog_langs_input = st.text_area(
            "Programming Languages (one per line)",
            value="\n".join(skills['programming_languages']),
            placeholder="Python\nR\nJava\nC++\nJavaScript\nSQL",
            height=120,
            help="List programming languages you're proficient in"
        )
        skills['programming_languages'] = [lang.strip() for lang in prog_langs_input.split('\n') if lang.strip()]

        # Bioinformatics Tools
        st.subheader("🧬 Bioinformatics Tools & Software")
        bioinfo_tools_input = st.text_area(
            "Bioinformatics Tools (one per line)",
            value="\n".join(skills['bioinformatics_tools']),
            placeholder="BLAST\nBioconductor\nGalaxy\nGATK\nSamtools\nBedtools\nIGV\nCytoscape",
            height=120,
            help="Bioinformatics software and tools you've used"
        )
        skills['bioinformatics_tools'] = [tool.strip() for tool in bioinfo_tools_input.split('\n') if tool.strip()]

        # Statistical Software
        st.subheader("📊 Statistical Software")
        stats_software_input = st.text_area(
            "Statistical Software (one per line)",
            value="\n".join(skills['statistical_software']),
            placeholder="SPSS\nSAS\nStata\nPRISM\nMatlab\nOrigin",
            height=100,
            help="Statistical analysis software you've used"
        )
        skills['statistical_software'] = [soft.strip() for soft in stats_software_input.split('\n') if soft.strip()]

    with col2:
        # Databases
        st.subheader("🗄️ Databases")
        databases_input = st.text_area(
            "Databases (one per line)",
            value="\n".join(skills['databases']),
            placeholder="MySQL\nPostgreSQL\nMongoDB\nNCBI\nEnsembl\nUniProt\nPDB\nGEO",
            height=120,
            help="Database systems and biological databases you've worked with"
        )
        skills['databases'] = [db.strip() for db in databases_input.split('\n') if db.strip()]

        # Cloud Platforms
        st.subheader("☁️ Cloud Platforms")
        cloud_input = st.text_area(
            "Cloud Platforms (one per line)",
            value="\n".join(skills['cloud_platforms']),
            placeholder="AWS\nGoogle Cloud Platform\nMicrosoft Azure\nDocker\nKubernetes\nSingularity",
            height=120,
            help="Cloud computing platforms and containerization tools"
        )
        skills['cloud_platforms'] = [cloud.strip() for cloud in cloud_input.split('\n') if cloud.strip()]

        # Other Technical Skills
        st.subheader("🔧 Other Technical Skills")
        other_input = st.text_area(
            "Other Technical Skills (one per line)",
            value="\n".join(skills['other_technical']),
            placeholder="Git/GitHub\nLinux/Unix\nHPC Computing\nMachine Learning\nData Visualization\nNextflow\nSnakemake",
            height=100,
            help="Additional technical skills and tools"
        )
        skills['other_technical'] = [skill.strip() for skill in other_input.split('\n') if skill.strip()]

    # Skills Summary
    if any(skills.values()):
        st.subheader("📋 Skills Summary")
        total_skills = sum(len(skill_list) for skill_list in skills.values())
        st.metric("Total Skills Listed", total_skills)

        # Display skills by category in a more compact format
        for category, skills_list in skills.items():
            if skills_list:
                category_name = category.replace('_', ' ').title()
                with st.expander(f"{category_name} ({len(skills_list)} skills)"):
                    # Display as tags
                    skills_text = ""
                    for skill in skills_list:
                        skills_text += f'<span style="background-color: #dbeafe; color: #1e40af; padding: 2px 8px; border-radius: 12px; margin: 2px; display: inline-block; font-size: 0.9em;">{skill}</span> '
                    st.markdown(skills_text, unsafe_allow_html=True)

    return skills