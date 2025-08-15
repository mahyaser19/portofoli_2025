# Mahmoud Yasser Mohamed - Cybersecurity Portfolio

A professional portfolio website showcasing penetration testing expertise, security assessments, and cybersecurity skills. Built with Python Flask framework featuring a modern, dark-themed design perfect for cybersecurity professionals.

## 🌟 Features

- **Professional Portfolio**: Showcases penetration testing projects and cybersecurity expertise
- **Dark Security Theme**: Modern dark design with cybersecurity-focused styling
- **Flask Backend**: Python-powered web framework for robust functionality
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Project Showcase**: Detailed security assessment projects with technologies used
- **Contact Form**: Professional contact form with cybersecurity service options
- **Skills Display**: Comprehensive showcase of security tools and methodologies

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this project** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd WEBSITE
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your web browser** and go to:
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
WEBSITE/
├── app.py                 # Main Flask application with portfolio data
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation and footer
    ├── index.html        # Home page with hero section and skills
    ├── about.html        # About page with detailed skills and background
    ├── projects.html     # Projects showcase page
    ├── project.html      # Individual project detail page
    └── contact.html      # Contact page with service options
```

## 🎨 Pages

- **Home Page** (`/`): Hero section, core skills, featured projects, and certifications
- **About Page** (`/about`): Professional background, technical skills, and contact information
- **Projects Page** (`/projects`): Complete showcase of security assessment projects
- **Project Details** (`/project/<id>`): Detailed information about individual projects
- **Contact Page** (`/contact`): Professional contact form and service offerings

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **CSS Framework**: Bootstrap 5
- **Icons**: Font Awesome 6
- **Styling**: Custom dark theme with cybersecurity-focused design

## 🔧 Customization

### Personal Information

Update the portfolio information in `app.py`:
```python
portfolio_info = {
    'name': 'Your Name',
    'title': 'Your Title',
    'email': 'your.email@example.com',
    'phone': 'Your Phone Number',
    'location': 'Your Location',
    'about': 'Your professional description'
}
```

### Adding New Projects

Edit the `projects` list in `app.py`:
```python
projects = [
    {
        'id': 4,
        'title': 'Your New Project',
        'description': 'Project description...',
        'technologies': ['Tool1', 'Tool2', 'Tool3'],
        'category': 'Project Category',
        'date': '2024-01-20'
    }
]
```

### Modifying Skills

Update the `skills` dictionary in `app.py` to reflect your expertise:
```python
skills = {
    'penetration_testing': ['Your Skills'],
    'tools': ['Your Tools'],
    'programming': ['Your Languages'],
    'certifications': ['Your Certifications'],
    'frameworks': ['Your Frameworks']
}
```

### Customizing Styles

The main styles are in the `<style>` section of `templates/base.html`. You can customize:
- Color scheme (CSS variables in `:root`)
- Dark theme colors and gradients
- Typography and spacing
- Cybersecurity-themed elements

## 🌐 Deployment

### Local Development
The application runs on `http://localhost:5000` by default.

### Production Deployment
For production deployment, consider:
- Using a production WSGI server like Gunicorn
- Setting up a reverse proxy with Nginx
- Using environment variables for configuration
- Setting `debug=False` in production
- Adding SSL/TLS certificates for security

## 📝 Portfolio Content

### Current Projects Include:
1. **Web Application Security Assessment** - Financial application penetration testing
2. **Network Infrastructure Security Audit** - Corporate network security assessment
3. **Mobile Application Security Testing** - Mobile app reverse engineering and analysis

### Skills Showcased:
- **Penetration Testing**: Web, Network, Mobile, Social Engineering
- **Security Tools**: Burp Suite, OWASP ZAP, Metasploit, Nmap, Wireshark, SQLMap
- **Programming**: Python, Bash, PowerShell, JavaScript, SQL
- **Certifications**: CompTIA Security+, CEH (In Progress), OSCP (Planned)
- **Frameworks**: OWASP Top 10, NIST Cybersecurity Framework, MITRE ATT&CK

## 📞 Contact Information

- **Name**: Mahmoud Yasser Mohamed
- **Title**: Junior Penetration Tester
- **Email**: mhmoudyasser40@gmail.com
- **Phone**: +20 128 455 6922
- **Location**: Egypt

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests

## 📞 Support

If you have any questions or need help, please:
1. Check the documentation
2. Look at the code comments
3. Create an issue in the project repository

---

**Stay Secure! 🛡️🔒** 