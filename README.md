# CDG GRC (Governance, Risk, and Compliance) System

A GRC (Governance, Risk, and Compliance) management system that helps GDC manage their compliance frameworks, risk assessments, and project management.

## Features

- **Core Module**
  - Framework management
  - Control management
  - Evidence collection and tracking

- **Risk Assessment Module**
  - Risk identification and categorization
  - Risk assessment with impact and likelihood analysis
  - Risk mitigation planning

- **Project Management Module**
  - Project tracking
  - Task management
  - Milestone tracking

- **Audit Module**
  - Audit planning and scheduling
  - Audit findings management
  - Remediation tracking
  - Evidence collection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/iliasly/cdg-grc.git
cd cdg-grc
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

- `core/`: Core functionality for framework and control management
- `risk_assessment/`: Risk assessment and management
- `project_management/`: Project and task management
- `audit/`: Audit planning, findings, and remediation tracking

## License

This project is licensed under the MIT License - see the LICENSE file for details. 