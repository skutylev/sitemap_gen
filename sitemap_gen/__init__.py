# -*- coding: utf-8 -*-
import yaml
import gzip
from jinja2 import Environment, PackageLoader
from jinja2.exceptions import TemplateNotFound

with open("sitemap_gen/default_config.yml", 'r') as conf_file:
    conf = yaml.load(conf_file)


try:
    env = Environment(loader=PackageLoader('sitemap_gen', 'templates'))
except FileNotFoundError:
    print('"templates" dir not found')


def gen_sitemap(response):
    try:
        sitemap_template = env.get_template('sitemap.xml.j2')
        sitemap_output = sitemap_template.render(response)

        with gzip.open('sitemaps/sitemap.xml.gz', 'wb') as sitemap:
            sitemap.write(bytes(sitemap_output, encoding='utf-8'))

    except TemplateNotFound:
        print('Error: sitemap.xml.j2 not found')


def gen_sitemap_index(response):
    try:
        sitemap_index_template = env.get_template('sitemap_index.xml.j2')
        sitemap_index_output = str(sitemap_index_template.render(response))

        with gzip.open('sitemaps/sitemap_index.xml.gz', 'wb') as sitemap:
            sitemap.write(sitemap_index_output)

    except TemplateNotFound:
        print('Error: sitemap_index.xml.j2 not found')
