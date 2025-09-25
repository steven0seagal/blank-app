# 🧬 Professional CV Builder for Bioinformaticians

[![CI/CD Pipeline](https://github.com/USERNAME/REPOSITORY/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/USERNAME/REPOSITORY/actions/workflows/ci-cd.yml)
[![Docker Image](https://ghcr.io/USERNAME/REPOSITORY/badge.svg)](https://ghcr.io/USERNAME/REPOSITORY)
[![Security Scan](https://github.com/USERNAME/REPOSITORY/actions/workflows/security.yml/badge.svg)](https://github.com/USERNAME/REPOSITORY/actions/workflows/security.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0+-red.svg)](https://streamlit.io)
[![Docker](https://img.shields.io/badge/Docker-supported-blue.svg)](https://www.docker.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive **Streamlit-based CV Builder** specifically designed for PhD bioinformaticians, computational biologists, and researchers. Create, customize, and export professional academic and industry CVs with specialized sections for scientific careers.

## 🚀 Features

### 📋 **Comprehensive CV Sections**
- **👤 Personal Information**: Professional photo upload, contact details, ORCID, GitHub, LinkedIn integration
- **🎓 Education**: PhD details, thesis titles, advisor information, academic credentials
- **💼 Work Experience**: Academic and industry positions with detailed descriptions
- **🛠️ Technical Skills**: Categorized skills for programming, bioinformatics tools, databases, cloud platforms
- **🚀 Research Projects**: Project showcases with GitHub links and technology stacks
- **📚 Publications**: Academic papers with DOI, PMID, journal formatting
- **🏆 Certifications & Awards**: Professional certifications and academic honors

### 📄 **Advanced PDF Export**
- **4 Professional Templates**:
  - Professional Blue (Corporate/Industry focus)
  - Academic Classic (Traditional academic style)
  - Modern Minimal (Clean, contemporary design)
  - Scientific Research (Research-focused with green accents)
- **Multiple Formats**: A4 and Letter page sizes
- **Optimized Output**: Compressed PDFs with professional typography
- **Template Customization**: Color schemes and layouts tailored to career focus

### 💾 **Data Management**
- **Session Persistence**: Data saved during your session
- **Export/Import**: JSON format for backup and transfer between sessions
- **Form Validation**: Comprehensive input validation and error handling
- **Dynamic Content**: Add/remove entries for each section

### 🎨 **Professional Design**
- **Responsive Layout**: Optimized for desktop and tablet viewing
- **Sidebar Navigation**: Intuitive section-based navigation
- **Scientific Focus**: Placeholders and examples tailored to bioinformatics careers
- **Professional Styling**: Clean, academic-appropriate interface design

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd blank-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   # New modular version (recommended)
   streamlit run app.py

   # Or legacy monolithic version
   streamlit run streamlit_app.py
   ```

4. **Access the application**
   Open your web browser and navigate to `http://localhost:8501`

## 🐳 Docker Deployment

### Quick Start with Docker

```bash
# Pull and run from GitHub Container Registry
docker run -p 8501:8501 ghcr.io/USERNAME/REPOSITORY:latest
```

### Build Locally

```bash
# Clone repository
git clone <repository-url>
cd blank-app

# Build Docker image
docker build -t cv-builder .

# Run container
docker run -p 8501:8501 cv-builder
```

### Docker Compose (Recommended)

```bash
# Development mode
docker-compose up

# Production mode with nginx proxy
docker-compose --profile production up

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f cv-builder

# Stop containers
docker-compose down
```

### Production Deployment

The application includes a comprehensive CI/CD pipeline that:
- ✅ Runs tests across Python 3.9, 3.10, and 3.11
- ✅ Performs security scanning with Trivy
- ✅ Builds multi-architecture Docker images (AMD64/ARM64)
- ✅ Pushes to GitHub Container Registry
- ✅ Supports staging and production deployments
- ✅ Creates automatic releases for version tags

### Alternative Installation (Virtual Environment)

```bash
# Create virtual environment
python -m venv cv_builder_env

# Activate virtual environment
# On Windows:
cv_builder_env\Scripts\activate
# On macOS/Linux:
source cv_builder_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run streamlit_app.py
```

## 📖 User Guide

### Getting Started

1. **Personal Information**: Start by adding your basic information and uploading a professional photo
2. **Education**: Add your PhD and other academic credentials with detailed information
3. **Work Experience**: Include both academic and industry positions
4. **Skills**: Categorize your technical skills across different domains
5. **Projects**: Showcase your research projects and software development work
6. **Publications**: Add your academic publications with proper citations
7. **Certifications**: Include professional certifications and awards
8. **Preview & Export**: Review your CV and export to PDF

### PDF Export Guide

1. Navigate to the "Preview & Export" section
2. Choose your preferred template style:
   - **Professional Blue**: Best for industry applications
   - **Academic Classic**: Traditional format for academic positions
   - **Modern Minimal**: Contemporary style for interdisciplinary roles
   - **Scientific Research**: Ideal for research-focused positions
3. Select page format (A4 or Letter)
4. Click "Generate & Download PDF"
5. Download your professionally formatted CV

### Data Management

- **Save Work**: Your data is automatically saved in the browser session
- **Export Data**: Use "Export Data (JSON)" to backup your information
- **Import Data**: Use "Import CV Data" to restore from a previous backup
- **Transfer Between Devices**: Export JSON on one device, import on another

## 🔧 Technical Architecture

### Application Structure

#### Modular Version (Recommended)
```
app.py                     # Main application (120 lines)
└── src/
    ├── models/
    │   └── cv_data.py     # Data models and validation
    ├── sections/          # Modular UI components
    │   ├── personal_info.py      # Personal information with links
    │   ├── education.py          # Academic credentials
    │   ├── experience.py         # Work history
    │   ├── skills.py             # Technical skills
    │   ├── projects.py           # Research projects
    │   ├── publications.py       # Academic papers
    │   ├── certifications_awards.py  # Certifications & awards
    │   └── preview_export.py     # Preview and export
    └── utils/
        ├── styles.py      # CSS styles and UI utilities
        └── pdf_generator.py # Multi-template PDF generation
```

#### Legacy Version (Still Available)
```
streamlit_app.py          # Monolithic application (882 lines)
```

### Key Dependencies
- **Streamlit**: Web application framework
- **ReportLab**: PDF generation with professional formatting
- **Pillow (PIL)**: Image processing for photo uploads
- **Plotly**: Interactive visualizations (future enhancements)

### Data Model
```python
cv_data = {
    'personal_info': dict,      # Basic information
    'photo': file,              # Profile photo
    'education': list,          # Academic credentials
    'experience': list,         # Work history
    'skills': dict,             # Categorized technical skills
    'projects': list,           # Research/software projects
    'publications': list,       # Academic publications
    'certifications': list,     # Professional certifications
    'awards': list             # Academic/professional awards
}
```

## 🎯 Target Audience

This CV builder is specifically designed for:
- **PhD Bioinformaticians** transitioning to industry or academic positions
- **Computational Biologists** in research institutions
- **Bioinformatics Researchers** seeking academic or industry roles
- **Data Scientists** in life sciences and biotechnology
- **Scientific Programmers** in genomics and proteomics

## 🔍 Specialized Features for Bioinformatics

### Technical Skills Categories
- **Programming Languages**: Python, R, Java, C++, JavaScript, SQL
- **Bioinformatics Tools**: BLAST, Bioconductor, Galaxy, GATK, Samtools
- **Statistical Software**: SPSS, SAS, Stata, PRISM, MATLAB
- **Databases**: MySQL, PostgreSQL, MongoDB, NCBI, Ensembl, UniProt
- **Cloud Platforms**: AWS, Google Cloud, Azure, Docker, Kubernetes

### Academic Integration
- **ORCID Support**: Direct integration for researcher identification
- **Publication Management**: DOI, PMID, citation formatting
- **Research Projects**: GitHub repository linking
- **Academic Timeline**: Thesis defense dates, advisor information

### Enhanced Features (Modular Version)
- **Clickable Links**: Direct access to LinkedIn and GitHub profiles
- **Progress Tracking**: Visual completion indicators and tips in sidebar
- **Enhanced Validation**: Real-time form validation with helpful error messages
- **Modular Architecture**: Maintainable code structure with 14 separate modules
- **Improved UI**: Better styling, success messages, and user feedback
- **Statistics Dashboard**: Publication counts, completion metrics, and CV statistics

## 🐛 Troubleshooting

### Common Issues

**1. Application won't start**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (3.8+ required)
- Try running in a virtual environment

**2. PDF export not working**
- Verify ReportLab installation: `pip install reportlab`
- Check file permissions in the working directory
- Ensure sufficient disk space for PDF generation

**3. Photo upload issues**
- Supported formats: PNG, JPG, JPEG
- Maximum file size: 10MB (automatically resized)
- Ensure proper file permissions

**4. Session data lost**
- Export your data regularly using JSON export
- Browser cache clearing may reset session data
- Use the import function to restore from backup

### Performance Optimization
- Close unused browser tabs to free memory
- Export large datasets before adding more content
- Use compressed image formats for photos

## 📚 Additional Resources

- **Streamlit Documentation**: [https://docs.streamlit.io/](https://docs.streamlit.io/)
- **ReportLab User Guide**: [https://www.reportlab.com/docs/reportlab-userguide.pdf](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- **CV Writing Best Practices**: Academic and industry-specific guidelines

## 🤝 Contributing

Contributions are welcome! Please read the contributing guidelines before submitting pull requests.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make changes and test thoroughly
4. Submit a pull request with detailed description

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support, bug reports, or feature requests:
- Create an issue in the repository
- Check existing issues for similar problems
- Review the troubleshooting section above

---

**Built with ❤️ for the bioinformatics and computational biology community**
