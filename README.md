# Differenpy

##### A difference calculator is a program that determines the difference between two data structures.

[![Github CI](https://github.com/notabu/python-project-lvl2/actions/workflows/ci.yml/badge.svg)](https://github.com/notabu/python-project-lvl2/actions/workflows/ci.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/80babc02ce31b73413bf/maintainability)](https://codeclimate.com/github/notabu/python-project-lvl2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/80babc02ce31b73413bf/test_coverage)](https://codeclimate.com/github/notabu/python-project-lvl2/test_coverage)

## Installation

```bash
pip install differenpy
```

or upgrade

```bash
pip install differenpy --upgrade
```

## Quick Start

A full set of examples can be found in the [online documentation](http://spotipy.readthedocs.org/) and in the [Differenpy examples directory](https://github.com/plamere/spotipy/tree/master/examples).

To get started, install spotipy and create an app on https://developers.spotify.com/.
Add your new ID and SECRET to your environment:

### Without user authentication

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
```

### With user authentication

```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
                                               client_secret="YOUR_APP_CLIENT_SECRET",
                                               redirect_uri="YOUR_APP_REDIRECT_URI",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
```

## Reporting Issues

For common questions please check our [FAQ](FAQ.md).

You can ask questions about Differenpy on
[Stack Overflow](http://stackoverflow.com/questions/ask).
Don’t forget to add the *Differenpy* tag, and any other relevant tags as well, before posting.

If you have suggestions, bugs or other issues specific to this library,
file them [here](https://github.com/znhv/differenpy/issues).
Or just send a pull request.