"""Load rasters into Geoserver."""
import os
import sys
import logging
import argparse
import glob

import requests

LOGGER = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format=('%(message)s'),
    stream=sys.stdout)
LOGGER = logging.getLogger(__name__)

REQUEST_TIMEOUT = 5.0


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description='Ecoshard geoserver.')
    parser.add_argument('username', help='username')
    parser.add_argument('password', help='password')
    args = parser.parse_args()

    session = requests.Session()
    session.auth = (args.username, args.password)

    parent_path = '/mnt/disks/geoserver_data/'
    for filepath in glob.glob(
            '/mnt/disks/geoserver_data/data/cv_sld_files/*.sld'):
        style_path = filepath[len(parent_path):]
        LOGGER.debug(style_path)
        style_name = os.path.splitext(os.path.basename(filepath))[0]
        payload = {
          "style": {
            "name": style_name,
            "filename": style_path
          }
        }
        LOGGER.debug(payload)
    #response = session.get('http://localhost:8080/geoserver/rest/workspaces/cv_coastal_points_output_md5_69641307c3c7b4c7d23faa8637e30f83/styles/rhab.json', timeout=REQUEST_TIMEOUT)

    #LOGGER.info(response)
    #LOGGER.info(response.json())


if __name__ == '__main__':
    main()
