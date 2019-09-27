## Adding your publication

You can add your app by creating [new file in `_publications`](https://github.com/NAIST-SE/code-review.github.io/new/master?filename=docs/_publications/your-publication-name.md)

```yaml
---
layout: publication
#  Your publication name
title: Title of the Publication
# The author of your publication
authors: You, second author, third author...
# A short description of what your publication does
description: What your app does
# A short conference name that has your publication
conference: ICSE
# A published year of your publication
year: 2019
methodology:
- Validation
- Solution
# Kinds of contributions for researcher or practitioner
practitioner:
- Potential benefits
researcher:
- Automation
- Program comprehension
summary: Summary of the paper
---

Any documentation can go here. Many publications just use their abstract here.
```
