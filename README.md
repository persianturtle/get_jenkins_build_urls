# Quickly Retrieve Jenkins Build URLs

Retrieving all build URLs for a Jenkins job can be tedious. This script was created to solve that problem.

> Note: Only successful builds are retrieved.

## Usage

Place `get_jenkins_build_urls.py` into a directory of your choice. Make sure the user has executable permission for the script. 

Example URL: `http://jenkins.ic2.player.to/job/IC2_experimental/`

Run the script with:

`./get_jenkins_build_urls.py`

You will be asked to supply a Jenkins Job URL.  You may choose to include or exclude the URL's trailing slash.

## Dependencies

This script was tested with Python 2.7.6 and requires:

1. `requests`
2. `yaml`
3. `BeautifulSoup`
