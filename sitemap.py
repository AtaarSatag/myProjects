import os
import pandas as pd

WEBSITE_ROOT_DIR = './' # Adapt this path to your root directory of your website tree
DOMAIN = 'https://example.domain/' # Adapt this domain to your (do not forget a URL schema of protocol, like http(s))
PATH_TO_SAVE = './' # Adapt a path to save a sitemap (do not forget a trailing slash)

# Search for paths of website files
paths = []
for path in os.walk(WEBSITE_ROOT_DIR):
    [paths.append(os.path.join(path[0], dirname)) for dirname in path[1]]
    [paths.append(os.path.join(path[0], name)) for name in path[2]]

# The following two lines exclude specific paths of the tree
paths = [path for path in paths if (path.find('../dir1') > 0) ^ (path.find('../dir1') == -1)]
paths = [path for path in paths if (path.find('../dir2') > 0) ^ (path.find('../dir2') == -1)]

# The loop make URL with the found paths
for i in range(len(paths)):
    paths[i] = paths[i].replace(WEBSITE_ROOT_DIR, DOMAIN)

with open(f'{PATH_TO_SAVE}sitemap.txt', 'w') as txt_sitemap:
    for line in paths:
        txt_sitemap.write(line+'\n')

urls = pd.DataFrame(paths, columns=['loc'])
urls = urls.to_xml(root_name='urlset', row_name='url', namespaces = {'': 'http://www.sitemaps.org/schemas/sitemap/0.9'})

with open(f'{PATH_TO_SAVE}sitemap.xml', 'w') as xml_sitemap:
    xml_sitemap.write(urls)
