"""
Publications section for CV Builder.
"""

import streamlit as st
from src.utils.styles import display_section_header, display_success_message
from src.models.cv_data import validate_publication_entry


def publications_section():
    """Render the publications section"""
    display_section_header("📚 Publications")

    publications_list = st.session_state.cv_data["publications"]

    # Add new publication
    with st.expander("➕ Add New Publication"):
        with st.form("publication_form"):
            st.markdown("### Add Publication Details")

            title = st.text_input("Title", help="Full title of the publication")

            authors = st.text_input(
                "Authors",
                placeholder="Last, F., Last, F., etc.",
                help="List all authors in the format: Last name, First initial.",
            )

            col1, col2 = st.columns(2)
            with col1:
                journal = st.text_input(
                    "Journal/Conference",
                    help="Name of the journal, conference, or publisher",
                )
                year = st.number_input(
                    "Year",
                    min_value=1900,
                    max_value=2030,
                    value=2024,
                    help="Year of publication",
                )

            with col2:
                volume = st.text_input(
                    "Volume (optional)", help="Journal volume number"
                )
                pages = st.text_input(
                    "Pages (optional)",
                    placeholder="e.g., 123-145 or e12345",
                    help="Page numbers or article number",
                )

            col3, col4 = st.columns(2)
            with col3:
                doi = st.text_input(
                    "DOI (optional)",
                    placeholder="10.1000/xyz123",
                    help="Digital Object Identifier",
                )
                pmid = st.text_input("PMID (optional)", help="PubMed ID if applicable")

            with col4:
                url = st.text_input(
                    "URL/Link (optional)", help="Direct link to the publication"
                )

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
                    help="Type of publication",
                )

            if st.form_submit_button("Add Publication", type="primary"):
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

                # Validate entry
                errors = validate_publication_entry(new_publication)
                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    publications_list.append(new_publication)
                    display_success_message("Publication added successfully!")
                    st.rerun()

    # Display publications
    if publications_list:
        st.subheader("Publications:")

        # Sort publications by year (newest first)
        sorted_publications = sorted(
            publications_list, key=lambda x: x["year"], reverse=True
        )

        for i, pub in enumerate(sorted_publications):
            # Find the original index for removal
            original_index = publications_list.index(pub)

            with st.container():
                col1, col2 = st.columns([4, 1])

                with col1:
                    # Format publication in academic style
                    st.markdown(f"**{pub['title']}**")
                    st.write(f"👥 {pub['authors']}")

                    # Journal information
                    journal_info = f"📖 {pub['journal']} ({pub['year']})"
                    if pub["volume"] and pub["pages"]:
                        journal_info += f", Vol. {pub['volume']}, pp. {pub['pages']}"
                    elif pub["volume"]:
                        journal_info += f", Vol. {pub['volume']}"
                    elif pub["pages"]:
                        journal_info += f", pp. {pub['pages']}"
                    st.write(journal_info)

                    # Additional identifiers
                    identifiers = []
                    if pub["doi"]:
                        identifiers.append(f"DOI: {pub['doi']}")
                    if pub["pmid"]:
                        identifiers.append(f"PMID: {pub['pmid']}")

                    if identifiers:
                        st.write(f"🔗 {' | '.join(identifiers)}")

                    if pub["url"]:
                        st.write(f"🌐 [View Publication]({pub['url']})")

                    # Publication type badge
                    type_colors = {
                        "Journal Article": "#10b981",
                        "Conference Paper": "#3b82f6",
                        "Book Chapter": "#8b5cf6",
                        "Preprint": "#f59e0b",
                        "Poster": "#ef4444",
                        "Abstract": "#6b7280",
                    }
                    color = type_colors.get(pub["type"], "#6b7280")
                    st.markdown(
                        f'<span style="background-color: {color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8em;">{pub["type"]}</span>',
                        unsafe_allow_html=True,
                    )

                with col2:
                    if st.button(f"🗑️ Remove", key=f"remove_pub_{original_index}"):
                        publications_list.pop(original_index)
                        st.rerun()

                st.divider()

        # Publication statistics
        st.subheader("📊 Publication Statistics")
        stats_col1, stats_col2, stats_col3 = st.columns(3)

        with stats_col1:
            st.metric("Total Publications", len(publications_list))

        with stats_col2:
            if publications_list:
                latest_year = max(pub["year"] for pub in publications_list)
                st.metric("Latest Publication", latest_year)

        with stats_col3:
            # Count by type
            type_counts = {}
            for pub in publications_list:
                pub_type = pub["type"]
                type_counts[pub_type] = type_counts.get(pub_type, 0) + 1

            most_common_type = (
                max(type_counts, key=type_counts.get) if type_counts else "None"
            )
            st.metric("Most Common Type", most_common_type)

    else:
        st.info(
            "No publications added yet. Use the form above to add your academic publications and research papers."
        )

    return publications_list
