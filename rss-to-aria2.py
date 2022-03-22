import config

import util.extract_util

import util.aria2_util

import json
import feedparser
import os

print("test")


def extract_function(function_name, entry):
    method_to_call = getattr(util.extract_util, 'dmhy_extract')
    return method_to_call(entry)


def aria2_download(aria2_config, source_to_download):
    method_to_call = getattr(util.aria2_util, 'aria2_download_uri')
    return method_to_call(aria2_config, source_to_download)


# def parse_feed(one_config, keyname):
#     one_config = config.config[keyname]
#     print("===", one_config)
#     d = feedparser.parse(one_config['source'])
#     download_list = []
#     print(d['feed']['title'])
#     print(d.feed.published)
#     for i in range(len(d.entries)):
#         download_list.append(extract_function(
#             one_config['extract_function'], d.entries[i]))

def get_history_filename(aria2_keyname, keyname):
    return 'history/'+aria2_keyname+'_'+keyname+'.txt'

# 每次只下载最新的一个链接
def download_latest_by_feed(aria2_keyname, keyname):
    one_config = config.source[keyname]
    print("===", one_config)
    d = feedparser.parse(one_config['source'])
    print(d.feed.title)
    print(d.feed.published)
    object_to_download = extract_function(one_config['extract_function'], d.entries[0])
    link_to_download = object_to_download['link']
    history_list = read_history(aria2_keyname, keyname)
    for d in history_list:
        print(d)

        if (d["link"]==link_to_download):
            print("already downloaded")
            return
    aria2_response = None
    aria2_response = aria2_download(config.aria2[aria2_keyname], link_to_download)
    print(aria2_response)
    object_to_download['response'] = aria2_response
    with open(get_history_filename(aria2_keyname, keyname), 'a+') as file:
        file.write(json.dumps(object_to_download)+'\n')


def read_history(aria2_keyname, keyname):
    history_list = []
    if not os.path.exists(get_history_filename(aria2_keyname, keyname)):
        if not os.path.exists('history'):
            os.makedirs('history')
        return []
    with open(get_history_filename(aria2_keyname, keyname), 'r') as file:
        for l in file.readlines():
            j = json.loads(l)
            history_list.append(j)
    return history_list

for c in config.config:
    print(c)
    download_latest_by_feed(c[0], c[1])
