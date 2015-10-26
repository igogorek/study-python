# coding: utf-8
__author__ = 'igogor'


def parse_props(lines_list):
    props = {}
    for line in lines_list:
        key, _, value_and_comment = line.strip().partition('=')
        if value_and_comment:
            value, _, comment = value_and_comment.partition('#')
            props[key] = value
    return props

def merge_props(source, patch, dest):
    with open(source) as source_file:
        source_props = parse_props(source_file.readlines())
    patch_props = parse_props(patch.split('\n'))
    source_props.update(patch_props)
    with open(dest, 'w+') as dest_file:
        for key, value in source_props.iteritems():
            dest_file.write('{}={}\n'.format(key, value))

source_path = 'D:\projects\study\study-python\props\source'
patch_ex = 'market.checkout.pushapi.url=http://ololo.ru:39015\n' \
           'market.search.url=http://lslb.market.yandex.net:17051/yandsearch\n' \
           '\n' \
           'ololo.property=popyachsya\n'
dest_path = 'D:\projects\study\study-python\props\dest'

merge_props(source_path, patch_ex, dest_path)