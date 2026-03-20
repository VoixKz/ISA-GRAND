# ISA-GRAND

ISA-GRAND is a Django-based web platform that combines:

- user account management for different roles (personal user, employer, advisor),
- course and vacancy search/publishing,
- digest/news recommendations,
- CV generation supported by AI prompts.

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/DJANGO-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/SQLite-%234ea94b.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI%20SDK-412991?style=for-the-badge&logo=openai&logoColor=white) ![PyMuPDF](https://img.shields.io/badge/PyMuPDF-fitz-009688?style=for-the-badge&logo=adobeacrobatreader&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### Project Structure

- `sagyzIsa/authApp` — authentication and user roles
- `sagyzIsa/search` — vacancies and courses
- `sagyzIsa/digest` — digest/news endpoints and homepage aggregation
- `sagyzIsa/cv` — CV questionnaire and PDF generation
- `sagyzIsa/sagyzIsa` — Django project configs
