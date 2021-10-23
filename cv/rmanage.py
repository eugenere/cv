#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

def main():
    """Run administrative tasks."""
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv.settings')

    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
