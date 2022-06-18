import os

""" OS ENV """
DEBUG = os.getenv('DEBUG', default='False') == 'True'
ENV_NAME = os.getenv('ENV_NAME', default='local')

# Docker ENV variables
PORT = os.getenv('PORT', default='5534')

AZURE_CONNECTION = ''

