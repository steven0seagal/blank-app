"""
Data models and initialization for CV Builder application.
"""

def init_cv_data():
    """Initialize the CV data structure"""
    return {
        'personal_info': {
            'full_name': '',
            'title': '',
            'email': '',
            'phone': '',
            'location': '',
            'linkedin': '',
            'github': '',
            'orcid': '',
            'website': '',
            'summary': ''
        },
        'photo': None,
        'education': [],
        'experience': [],
        'skills': {
            'programming_languages': [],
            'bioinformatics_tools': [],
            'statistical_software': [],
            'databases': [],
            'cloud_platforms': [],
            'other_technical': []
        },
        'projects': [],
        'publications': [],
        'certifications': [],
        'awards': []
    }

def validate_personal_info(personal_info):
    """Validate personal information data"""
    required_fields = ['full_name', 'email']
    errors = []

    for field in required_fields:
        if not personal_info.get(field, '').strip():
            errors.append(f"{field.replace('_', ' ').title()} is required")

    # Email validation
    email = personal_info.get('email', '')
    if email and '@' not in email:
        errors.append("Please enter a valid email address")

    return errors

def validate_education_entry(education):
    """Validate education entry"""
    required_fields = ['degree', 'institution']
    errors = []

    for field in required_fields:
        if not education.get(field, '').strip():
            errors.append(f"{field.replace('_', ' ').title()} is required")

    # Year validation
    start_year = education.get('start_year', 0)
    end_year = education.get('end_year', 0)

    if start_year and end_year and start_year > end_year:
        errors.append("Start year cannot be greater than end year")

    return errors

def validate_experience_entry(experience):
    """Validate work experience entry"""
    required_fields = ['job_title', 'company']
    errors = []

    for field in required_fields:
        if not experience.get(field, '').strip():
            errors.append(f"{field.replace('_', ' ').title()} is required")

    return errors

def validate_project_entry(project):
    """Validate project entry"""
    required_fields = ['name', 'description']
    errors = []

    for field in required_fields:
        if not project.get(field, '').strip():
            errors.append(f"{field.replace('_', ' ').title()} is required")

    return errors

def validate_publication_entry(publication):
    """Validate publication entry"""
    required_fields = ['title', 'authors', 'journal', 'year']
    errors = []

    for field in required_fields:
        if not str(publication.get(field, '')).strip():
            errors.append(f"{field.replace('_', ' ').title()} is required")

    # Year validation
    year = publication.get('year', 0)
    if year and (year < 1900 or year > 2030):
        errors.append("Please enter a valid publication year")

    return errors