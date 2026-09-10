# redpine-sdk

Python client for the Redpine search API. Python 3.10+, sync and async.

```bash
pip install redpine-sdk
```

```python
from redpine import Redpine, F

client = Redpine()  # reads REDPINE_API_KEY
r = client.search("crispr delivery", collections=["corpus"], filters=F("issn").eq("1664-302X"))
for hit in r.results:
    print(hit.id, hit.text[:80])
```

Docs: https://docs.redpine.ai/docs/sdks
