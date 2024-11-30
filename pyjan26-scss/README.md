# SCSS to CSS

A plugin for compiling SCSS files into CSS during the build process in Pyjan26

## Setup

1. Install the plugin
```python
pip install pyjan26-scss
```

2. Add to your settings.py

```python

PLUGIN_MODULES = [
    'pyjan26-scss.scss2css',
     ...
]

# Define scss files to convert to css
SCSS_CSS_PATTERNS = ['assets/*.scss']
```

## Output

Assuming your SCSS file style1.sccss contains
```css
$primary-color: #333;

body {
  color: $primary-color;
}
```

The plugin will compile it into CSS like this
```css
body {
	color: #333
}



