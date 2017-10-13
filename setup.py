from setuptools import setup


setup(
    name='Boms-Away',
    app=['bomsaway.py'],
    options={'py2app': {'iconfile': 'Boms-Away.icns'}},
    install_requires=[
        'sqlalchemy',
        'wxpython',
    ],
    setup_requires=['py2app'],
)
