#!/usr/bin/env python
import os
import sys


def main():
    # Instructs Django which settings module to use if none is explicitly provided.
    # Replace 'project.settings' with 'your_project_name.settings' if different.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        # Import Django's command-line execution handler
        from django.core.management import execute_from_command_line
        # Provides a helpful error message if Django isn't installed or accessible
    except ImportError as exc:
        raise
    # Passes command-line arguments ( 'runserver', 'migrate') to Django's execution runner
    execute_from_command_line(sys.argv)

# Standard Python boilerplate to ensure main() runs only when this file is executed directly
if __name__ == '__main__':
    main()
