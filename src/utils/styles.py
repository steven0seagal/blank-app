"""
CSS styles and UI utilities for the CV Builder application.
"""

import streamlit as st

def load_css():
    """Load custom CSS styles for the application"""
    st.markdown("""
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

    .success-message {
        background-color: #d1fae5;
        color: #065f46;
        padding: 0.8em;
        border-radius: 0.5em;
        border-left: 4px solid #10b981;
        margin: 1em 0;
    }

    .error-message {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 0.8em;
        border-radius: 0.5em;
        border-left: 4px solid #ef4444;
        margin: 1em 0;
    }

    .warning-message {
        background-color: #fef3c7;
        color: #92400e;
        padding: 0.8em;
        border-radius: 0.5em;
        border-left: 4px solid #f59e0b;
        margin: 1em 0;
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f8fafc;
    }

    /* Form styling */
    .stForm {
        background-color: #ffffff;
        padding: 1.5em;
        border-radius: 0.5em;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    /* Preview section styling */
    .cv-preview {
        background-color: #ffffff;
        padding: 2em;
        border-radius: 0.5em;
        border: 1px solid #d1d5db;
        margin: 1em 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Export section styling */
    .export-section {
        background-color: #f9fafb;
        padding: 1.5em;
        border-radius: 0.5em;
        border: 1px solid #d1d5db;
        margin: 1em 0;
    }
    </style>
    """, unsafe_allow_html=True)

def display_success_message(message):
    """Display a success message with custom styling"""
    st.markdown(f'<div class="success-message">✅ {message}</div>', unsafe_allow_html=True)

def display_error_message(message):
    """Display an error message with custom styling"""
    st.markdown(f'<div class="error-message">❌ {message}</div>', unsafe_allow_html=True)

def display_warning_message(message):
    """Display a warning message with custom styling"""
    st.markdown(f'<div class="warning-message">⚠️ {message}</div>', unsafe_allow_html=True)

def display_section_header(title):
    """Display a styled section header"""
    st.markdown(f'<h2 class="section-header">{title}</h2>', unsafe_allow_html=True)

def display_main_header(title):
    """Display the main application header"""
    st.markdown(f'<h1 class="main-header">{title}</h1>', unsafe_allow_html=True)