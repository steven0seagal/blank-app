"""
Certifications and Awards section for CV Builder.
"""

import streamlit as st
from datetime import datetime
from src.utils.styles import display_section_header, display_success_message


def certifications_awards_section():
    """Render the certifications and awards section"""
    display_section_header("🏆 Certifications & Awards")

    # Certifications
    st.subheader("📜 Certifications")
    certifications_list = st.session_state.cv_data["certifications"]

    with st.expander("➕ Add New Certification"):
        with st.form("certification_form"):
            st.markdown("### Add Certification Details")

            col1, col2 = st.columns(2)
            with col1:
                cert_name = st.text_input(
                    "Certification Name", help="Full name of the certification"
                )
                issuing_org = st.text_input(
                    "Issuing Organization",
                    help="Organization that issued the certification",
                )

            with col2:
                issue_date = st.date_input(
                    "Issue Date", help="When the certification was issued"
                )
                expiry_date = st.date_input(
                    "Expiry Date (optional)",
                    value=datetime.now(),
                    help="When the certification expires",
                )
                no_expiry = st.checkbox(
                    "No Expiry Date", help="Check if certification doesn't expire"
                )

            credential_id = st.text_input(
                "Credential ID (optional)",
                help="Unique identifier for the certification",
            )
            cert_url = st.text_input(
                "Certification URL (optional)",
                help="Link to verify or view the certification",
            )

            if st.form_submit_button("Add Certification", type="primary"):
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

                if not cert_name.strip() or not issuing_org.strip():
                    st.error(
                        "Certification name and issuing organization are required."
                    )
                else:
                    certifications_list.append(new_cert)
                    display_success_message("Certification added successfully!")
                    st.rerun()

    if certifications_list:
        for i, cert in enumerate(certifications_list):
            with st.container():
                col1, col2 = st.columns([4, 1])

                with col1:
                    st.markdown(f"**{cert['name']}**")
                    st.write(f"🏢 {cert['issuing_org']}")
                    st.write(
                        f"📅 Issued: {cert['issue_date']} | Expires: {cert['expiry_date']}"
                    )

                    if cert["credential_id"]:
                        st.write(f"🆔 **Credential ID:** {cert['credential_id']}")

                    if cert["url"]:
                        st.write(f"🔗 [View Credential]({cert['url']})")

                with col2:
                    if st.button(f"🗑️ Remove", key=f"remove_cert_{i}"):
                        certifications_list.pop(i)
                        st.rerun()

                st.divider()
    else:
        st.info("No certifications added yet.")

    # Awards
    st.subheader("🏅 Awards & Honors")
    awards_list = st.session_state.cv_data["awards"]

    with st.expander("➕ Add New Award"):
        with st.form("award_form"):
            st.markdown("### Add Award Details")

            col1, col2 = st.columns(2)
            with col1:
                award_name = st.text_input(
                    "Award Name", help="Name of the award or honor"
                )
                awarding_org = st.text_input(
                    "Awarding Organization", help="Organization that gave the award"
                )

            with col2:
                award_date = st.date_input(
                    "Date Received", help="When you received the award"
                )

            award_description = st.text_area(
                "Description (optional)",
                help="Brief description of the award and why you received it",
            )

            if st.form_submit_button("Add Award", type="primary"):
                new_award = {
                    "name": award_name,
                    "awarding_org": awarding_org,
                    "date": award_date.strftime("%Y-%m-%d"),
                    "description": award_description,
                }

                if not award_name.strip() or not awarding_org.strip():
                    st.error("Award name and awarding organization are required.")
                else:
                    awards_list.append(new_award)
                    display_success_message("Award added successfully!")
                    st.rerun()

    if awards_list:
        for i, award in enumerate(awards_list):
            with st.container():
                col1, col2 = st.columns([4, 1])

                with col1:
                    st.markdown(f"**{award['name']}**")
                    st.write(f"🏢 {award['awarding_org']}")
                    st.write(f"📅 {award['date']}")

                    if award["description"]:
                        st.write(award["description"])

                with col2:
                    if st.button(f"🗑️ Remove", key=f"remove_award_{i}"):
                        awards_list.pop(i)
                        st.rerun()

                st.divider()
    else:
        st.info("No awards added yet.")

    return certifications_list, awards_list
