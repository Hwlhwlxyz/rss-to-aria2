requirements:

```
feedparser
```

运行

```
python3 rss-to-aria2.py
```

如果返回空
```
{'bozo': True, 'entries': [], 'feed': {}, 'headers': {}, 'bozo_exception': URLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1131)'))}

# 添加
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

```
