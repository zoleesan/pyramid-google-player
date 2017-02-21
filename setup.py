from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'gmusicapi',
    'datetime',
]

setup(name='google_player',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = google_player:main
      """,
)
