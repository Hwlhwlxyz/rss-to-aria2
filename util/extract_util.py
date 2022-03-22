

def dmhy_extract(entry):
    # print(entry)
    for l in entry.links:
        if (l['type']=='application/x-bittorrent'):
            # print('download link:',l)
            return {
                'title': entry['title'],
                'link': l['href'],
                'pubDate': entry.published
                }

if __name__ == '__main__':
    print("extract")
    