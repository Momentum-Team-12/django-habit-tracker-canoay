# Habit Tracker Notes

## Getting Started - additional comments

- `django-environ` - [follow install steps](https://pypi.org/project/django-environ/)
- `django-debug-toolbar` -[follow install steps](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
- `django-extensions` - [follow install steps](https://django-extensions.readthedocs.io/en/latest/installation_instructions.html)
- `django-registration-redux` - [install steps & one-step backend set-up](https://django-registration-redux.readthedocs.io/en/latest/simple-backend.html)
  <br>
  <br>

---

### Take environment variables from .env file, in settings.py

---

environ.Env.read_env(BASE_DIR / '.env') - reads the file at the base directory. Leaving it empty inside the parentheses will look for it alongside the settings.py location.
