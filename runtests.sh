#!/bin/bash
set -ex

# python manage.py test --testrunner=django_nose.NoseTestSuiteRunner
python manage.py test golgoth --testrunner=django_behave.runner.DjangoBehaveTestSuiteRunner