import urllib.request
import json
import base64
import time
# https://manpages.ubuntu.com/manpages/jammy/en/man1/aria2c.1.html


# def aria2_download_torrent():
#     torrent = base64.b64encode(open('file.torrent').read())
#     jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 'asdf',
#                           'method': 'aria2.addTorrent', 'params': [torrent]})
#     c = urllib.request.urlopen('http://localhost:6800/jsonrpc', jsonreq)
#     return c.read()


def aria2_download_uri(config, uri):
    print('config', config, 'token:'+config['token'])
    print(uri)

    aria2_headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'Cache-Control': 'no-cache'
    }
    jsonreq = json.dumps({'jsonrpc': '2.0',
                          'id': str(int(time.time())),
                          'method': 'aria2.addUri',
                          'params': [
                              'token:'+config['token'],
                              [uri],
                              {'dir': config['download_dir']}
                          ]}).encode()
    aria2_host_url = config['host']+':'+config['rpc_port']+'/jsonrpc'
    req = urllib.request.Request(
        aria2_host_url, method='POST', headers=aria2_headers, data=jsonreq)
    c = urllib.request.urlopen(req)
    return c.read().decode()


if __name__ == '__main__':
    print("aria2_util")
