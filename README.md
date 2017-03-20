# Slack Export Viewer

The slack export viewer is a command line tool that lets you filter and render
a slack export into text files for easy analysis and reading.

![Preview](screenshot.png)


## Overview

`slack-export-viewer` is a useful tool for teams who are running a free slack instance, and might have to produce a report covering the conversations, or at least read it in a standard text browser


## Usage

### 1) Grab your Slack team's export

* Visit [https://my.slack.com/services/export](https://my.slack.com/services/export)
* Create an export
* Wait for it to complete
* Refresh the page and download the export (.zip file) into whatever directory

### 2) Point `slack-export-viewer` to it

Point slack-export-viewer to the .zip file and let it do its magic

```bash
slack-export-viewer -z /path/to/export/zip
```

If everything went well, your archive will have been extracted, processed, and browser window will have opened showing your *#general* channel from the export.


## Installation

I recommend [`pipsi`](https://github.com/mitsuhiko/pipsi) for a nice
isolated install.

```bash
pipsi install slack-export-viewer
```

Or just feel free to use `pip` as you like.

```bash
pip install slack-export-viewer
```

`slack-export-viewer` will be installed as an entry-point; run from anywhere.

```bash
$ slack-export-viewer --help
Usage: slack-export-viewer [OPTIONS]

Options:
  -p, --port INTEGER  Host port to serve your content on
  -z, --archive PATH  Path to your Slack export archive (.zip file)
                      [required]
  -I, --ip TEXT       Host IP to serve your content on
  --no-browser        If you do not want a browser to open automatically, set
                      this.
  --debug
  --help              Show this message and exit.
```


## Acknowledgements

Credit to Pieter Levels whose [blog post](https://levels.io/slack-export-to-html/) and PHP script I used as a jumping off point for this.

### Improvements over Pieter's script

 `slack-export-viewer` is similar in core functionality but adds several things on top to make it nicer to use:

* An installable application
* Automated archive extraction and retention
* A Slack-like sidebar that lets you switch channels easily
* Much more "sophisticated" rendering of messages
* A Flask server which lets you serve the archive contents as opposed to a PHP script which does static file generation
