---
layout: default
title: For developers
nav_order: 4
has_children: true
---


For developers
==============

Thanks for contributing :)


Setup
=====

This project has unit tests that help prevent regressions. Before you can run the tests, you must install a few dependencies:
```bash
poetry install
npm i
```

Tests
=====

```bash
make test
```

Formatting
=====
```bash
make format
```

mypy checks
=====
```bash
poetry run mypy
```

Everything above
=====
```bash
make all
```

Start the server
=====

```bash
poetry run lnbits
```
