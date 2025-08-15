from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Portfolio data
portfolio_info = {
    'name': 'Mahmoud Yasser Mohamed',
    'title': 'Junior Penetration Tester',
    'email': 'mhmoudyasser40@gmail.com',
    'phone': '+20 128 455 6922',
    'location': 'Egypt',
    'about': 'Passionate cybersecurity professional specializing in penetration testing, vulnerability assessment, and security research. Committed to helping organizations strengthen their security posture through ethical hacking and comprehensive security analysis.',
    'linkedin': '#',
    'github': '#',
    'twitter': '#'
}

# Sample projects - in a real app, you'd use a database
projects = [
    {
        'id': 1,
        'title': 'Web Application Security Assessment',
        'description': 'Conducted comprehensive penetration testing on a financial web application, identifying critical vulnerabilities including SQL injection and XSS.',
        'technologies': ['OWASP ZAP', 'Burp Suite', 'SQLMap', 'Nmap'],
        'category': 'Web Security',
        'date': '2024-01-15'
    },
    {
        'id': 2,
        'title': 'Network Infrastructure Security Audit',
        'description': 'Performed network penetration testing on corporate infrastructure, discovering misconfigurations and potential attack vectors.',
        'technologies': ['Nmap', 'Metasploit', 'Wireshark', 'Nessus'],
        'category': 'Network Security',
        'date': '2024-01-10'
    },
    {
        'id': 3,
        'title': 'Mobile Application Security Testing',
        'description': 'Analyzed mobile application security using reverse engineering techniques and identified data exposure vulnerabilities.',
        'technologies': ['APKTool', 'MobSF', 'Frida', 'Burp Suite'],
        'category': 'Mobile Security',
        'date': '2024-01-05'
    }
]

# Skills data
skills = {
    'penetration_testing': ['Web Application Testing', 'Network Penetration Testing', 'Mobile Security Testing', 'Social Engineering'],
    'tools': ['Burp Suite', 'OWASP ZAP', 'Metasploit', 'Nmap', 'Wireshark', 'SQLMap', 'John the Ripper', 'Hashcat'],
    'programming': ['Python', 'Bash', 'PowerShell', 'JavaScript', 'SQL'],
    'networking': ['CCNA', 'Network Fundamentals', 'TCP/IP', 'Routing & Switching', 'Network Security'],
    'certifications': ['CompTIA Security+', 'CCNA', 'CEH (In Progress)', 'OSCP (Planned)'],
    'frameworks': ['OWASP Top 10', 'NIST Cybersecurity Framework', 'MITRE ATT&CK']
}

@app.route('/')
def home():
    return render_template('index.html', portfolio=portfolio_info, projects=projects, skills=skills)

@app.route('/about')
def about():
    return render_template('about.html', portfolio=portfolio_info, skills=skills)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects, portfolio=portfolio_info)

@app.route('/contact')
def contact():
    return render_template('contact.html', portfolio=portfolio_info)

@app.route('/project/<int:project_id>')
def project(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        flash('Project not found!', 'error')
        return redirect(url_for('home'))
    return render_template('project.html', project=project, portfolio=portfolio_info, projects=projects)

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    if name and email and message:
        flash('Thank you for your message! I\'ll get back to you soon.', 'success')
    else:
        flash('Please fill in all fields.', 'error')
    
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 