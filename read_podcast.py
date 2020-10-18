#!/usr/bin/env python3

import yaml
from feedgen.feed import FeedGenerator
import glob
import os

fg = FeedGenerator()
fg.load_extension('podcast')
fg.podcast.itunes_category('Technology', 'Podcasting')


with open('podcast_meta.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    fg.title(data['title'])
    fg.link( href=data['link'], rel=data['rel'])
    fg.description(data['description'])
    fg.language(data['language'])

for filename in glob.glob('episodes/*.yaml'):
   with open(filename, 'r')  as f:
       fe = fg.add_entry()
       data = yaml.load(f, Loader=yaml.FullLoader)
       fe.id(data['id'])
       fe.description(data['description'])
       fe.enclosure(data['id'],0,data['format'])

fg.rss_str(pretty=True)
fg.rss_file('podcast.xml')