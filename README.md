# Personal website

View at [lukeconibear.com](https://www.lukeconibear.com).

The published site is plain HTML and CSS in `docs/`. It has no build step,
package manager, project dependencies, JavaScript, or custom deployment
workflow.

Edit files in `docs/` directly. GitHub Pages should publish from the `main`
branch and `/docs` folder.

## Preview locally

This command is only for local previewing. GitHub Pages does not use it.

```bash
/usr/bin/python3 -m http.server 8000 --bind 127.0.0.1 --directory docs
```
