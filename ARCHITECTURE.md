# 🏗️ CV Builder - Application Architecture

## Overview

The Professional CV Builder for Bioinformaticians has been refactored into a modular architecture for better maintainability, extensibility, and code organization. This document outlines the structure and design decisions.

## 🗂️ Directory Structure

```
blank-app/
├── app.py                      # New modular main application
├── streamlit_app.py           # Legacy monolithic version (882 lines)
├── requirements.txt           # Dependencies
├── README.md                  # User documentation
├── ARCHITECTURE.md           # This file
├── CLAUDE.md                 # Claude Code documentation
├── cv_todo_list.md           # Development roadmap
├── LICENSE                   # MIT License
└── src/                      # Source code modules
    ├── __init__.py
    ├── models/               # Data models and validation
    │   ├── __init__.py
    │   └── cv_data.py       # CV data structure and validation
    ├── sections/            # UI sections (modular components)
    │   ├── __init__.py
    │   ├── personal_info.py      # Personal information section
    │   ├── education.py          # Education section
    │   ├── experience.py         # Work experience section
    │   ├── skills.py             # Technical skills section
    │   ├── projects.py           # Projects section
    │   ├── publications.py       # Publications section
    │   ├── certifications_awards.py  # Certifications & awards
    │   └── preview_export.py     # Preview and export section
    └── utils/               # Utilities and helpers
        ├── __init__.py
        ├── styles.py        # CSS styles and UI utilities
        └── pdf_generator.py # PDF generation with templates
```

## 🎯 Design Principles

### 1. Separation of Concerns
- **Models**: Data structure, validation, and business logic
- **Views**: UI components and user interaction
- **Utils**: Shared utilities and helper functions

### 2. Modularity
- Each CV section is a separate, self-contained module
- Easy to add new sections or modify existing ones
- Clear interfaces between components

### 3. Reusability
- Shared utilities for styling and common operations
- Consistent validation patterns
- Template-based PDF generation

### 4. Maintainability
- Small, focused files (50-200 lines each vs. 882 lines monolith)
- Clear naming conventions
- Comprehensive documentation

## 📊 Component Details

### Data Models (`src/models/`)

#### `cv_data.py`
- **Purpose**: Define data structure and validation rules
- **Key Functions**:
  - `init_cv_data()`: Initialize empty CV data structure
  - `validate_*()`: Validation functions for each section
- **Responsibilities**:
  - Data schema definition
  - Input validation
  - Error message generation

### UI Sections (`src/sections/`)

Each section module follows a consistent pattern:
- **Function Name**: `{section}_section()`
- **Return Value**: The modified data for that section
- **Responsibilities**:
  - Render UI components
  - Handle user input
  - Validate data using model functions
  - Update session state

#### Section Modules:
1. **`personal_info.py`** (110 lines)
   - Personal details, photo upload
   - Contact information with clickable links
   - Professional summary

2. **`education.py`** (120 lines)
   - Academic credentials
   - Thesis and advisor information
   - GPA and achievements

3. **`experience.py`** (115 lines)
   - Work history with timeline
   - Job descriptions and achievements
   - Support for current positions

4. **`skills.py`** (130 lines)
   - Categorized technical skills
   - Bioinformatics-specific categories
   - Skills summary with visual tags

5. **`projects.py`** (110 lines)
   - Research and software projects
   - GitHub integration
   - Technology stack tracking

6. **`publications.py`** (140 lines)
   - Academic publications
   - DOI, PMID, and citation support
   - Publication statistics

7. **`certifications_awards.py`** (100 lines)
   - Professional certifications
   - Awards and honors
   - Credential verification links

8. **`preview_export.py`** (150 lines)
   - CV preview with styling
   - Multi-template PDF export
   - Data import/export
   - Completion tracking

### Utilities (`src/utils/`)

#### `styles.py` (90 lines)
- **Purpose**: CSS styling and UI helper functions
- **Key Functions**:
  - `load_css()`: Load custom CSS styles
  - `display_*_message()`: Styled message displays
  - `display_section_header()`: Consistent section headers

#### `pdf_generator.py` (200 lines)
- **Purpose**: PDF generation with multiple templates
- **Key Functions**:
  - `generate_pdf_cv()`: Main PDF generation function
  - `get_template_colors()`: Template-specific styling
  - `add_*_section()`: Section-specific PDF formatting
- **Templates**:
  - Professional Blue (Corporate/Industry)
  - Academic Classic (Traditional academic)
  - Modern Minimal (Clean contemporary)
  - Scientific Research (Research-focused)

### Main Application (`app.py`)

#### Structure (120 lines)
- **Session Management**: Initialize CV data and state
- **Navigation**: Sidebar with section selection
- **Progress Tracking**: Visual completion indicators
- **Section Routing**: Dynamic content based on selection
- **Tips and Help**: Contextual user guidance

## 🔄 Data Flow

```
User Interaction → Section Module → Validation → Session State → PDF Export
                                        ↓
                                   Error Messages
```

1. **User Input**: User interacts with form elements in section modules
2. **Validation**: Input validated using functions from `cv_data.py`
3. **State Update**: Valid data stored in `st.session_state.cv_data`
4. **Visual Feedback**: Success/error messages displayed using `styles.py`
5. **Export**: Data processed through `pdf_generator.py` for PDF output

## 🎨 Styling Architecture

### CSS Organization
- **Global Styles**: Main headers, buttons, layout
- **Component Styles**: Section-specific styling
- **State Styles**: Success, error, warning messages
- **Export Styles**: PDF preview and export areas

### Theme Consistency
- **Color Palette**: Blue-based professional theme
- **Typography**: Consistent font sizes and weights
- **Spacing**: Standardized margins and padding
- **Interactive Elements**: Hover states and transitions

## 📈 Benefits of Modular Architecture

### Development Benefits
1. **Faster Development**: Smaller files are easier to work with
2. **Parallel Development**: Multiple developers can work on different sections
3. **Easier Testing**: Individual components can be tested in isolation
4. **Code Reuse**: Utilities can be shared across components

### Maintenance Benefits
1. **Bug Isolation**: Issues are contained within specific modules
2. **Feature Addition**: New sections can be added without touching existing code
3. **Code Navigation**: Clear structure makes finding code faster
4. **Refactoring**: Changes to one component don't affect others

### User Experience Benefits
1. **Performance**: Modular loading can improve perceived performance
2. **Reliability**: Errors in one section don't crash the entire app
3. **Consistency**: Shared utilities ensure consistent behavior
4. **Features**: Easier to add new features and templates

## 🚀 Running the Application

### Modular Version (Recommended)
```bash
streamlit run app.py
```

### Legacy Monolithic Version
```bash
streamlit run streamlit_app.py
```

## 🔮 Future Enhancements

The modular architecture enables easy extension:

1. **New Sections**: Add research interests, languages, conferences
2. **New Templates**: Create industry-specific PDF templates
3. **Data Sources**: Import from LinkedIn, ORCID APIs
4. **Export Formats**: Add Word, LaTeX export options
5. **Collaboration**: Multi-user editing and sharing
6. **Analytics**: Track CV performance and usage

## 📝 Migration Notes

- **Backward Compatibility**: The legacy `streamlit_app.py` remains functional
- **Data Compatibility**: Session state structure is identical
- **Feature Parity**: All original features are preserved
- **Enhanced Features**: Added LinkedIn/GitHub links, improved validation

The modular architecture provides a solid foundation for continued development while maintaining the existing user experience and functionality.