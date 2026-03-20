# ISA-GRAND

ISA-GRAND is a Django-based web platform that combines:
- user account management for different roles (personal user, employer, advisor),
- course and vacancy search/publishing,
- digest/news recommendations,
- CV generation supported by AI prompts.

## Technologies Used

### Backend
- **Python 3**
- **Django 5.1.3**
- **SQLite** (default local database)
- **python-dotenv** for environment variables
- **Requests** for HTTP integrations
- **OpenAI Python SDK** for AI-powered text processing
- **PyMuPDF (fitz)** for PDF/CV generation

### Frontend
- **Django Templates**
- **HTML5 / CSS3 / JavaScript**

### Project Structure
- `sagyzIsa/authApp` — authentication and user roles
- `sagyzIsa/search` — vacancies and courses
- `sagyzIsa/digest` — digest/news endpoints and homepage aggregation
- `sagyzIsa/cv` — CV questionnaire and PDF generation
- `sagyzIsa/sagyzIsa` — Django project config (settings, urls, wsgi, asgi)

## Security Notes

As part of this repository update, security-oriented defaults were improved in Django settings:
- `DEBUG` is now configurable via environment variable (instead of hardcoded `True`).
- `ALLOWED_HOSTS` is configurable via environment variable.
- `SECRET_KEY` now enforces explicit configuration when `DEBUG=False`.
- Production-focused security settings are enabled when `DEBUG=False` (secure cookies, HSTS, content type sniffing protection, SSL redirect, strict frame policy).

Use `.env.example` as a template for local configuration.
