# Sitemap

This plugin generates a dynamic sitemap for projects built w Pyjan26.
It creates a sitemap XML file annd integrates custom collections into the sitemap

## Setup

1. Install the plugin
```python
pip install pyjan26-sitemap
```

2. Add to your settings.py

```python

PLUGIN_MODULES = [
    'pyjan26-sitemap.sitemap',
     ...
]

SITE_NAME = 'https://example.com'
SITEMAP_CONFIG = [
	{'collection': 'articles', 'changefreq': 'daily', 'priority': 1.0}
] 
```

## Output

Sitemap saved at
```bash
<output_dir>/sitemap.xml
```


