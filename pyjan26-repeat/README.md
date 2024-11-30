# Repeat Page

A Pyjan26 plugin for generating repeated pages from collection data

## Setup

1. Install the plugin
```python
pip install pyjan26-repeat
```


2. Add to your settings.py

```python
PLUGIN_MODULES = [
    'pyjan26-repeat.repeat_page',
     ...
]
```

3. Add yaml frontmatter to your Markdown file
```yaml
---
layout: base.html
repeat_page: True 
data: all_tags # change this based on your collections data (must be a list)
title: Sample Repeated Page
---
```

## Output

if your collection all_tags contains:

```bash
all_tags = ['python', 'django', 'flask']
```

The plugin will generate pages with URLs like:
* /python/
* /django/
* /flask/

Each page will be populated w content based on the data (in this case, all_tags)



