# Portfolio study: ragJ_platform

This repository is an attributed fork of [chongliujia/ragJ_platform](https://github.com/chongliujia/ragJ_platform).

## What I added

- Added this portfolio review and integration plan in 2026.
- Audited the upstream architecture, setup path, configuration boundary, and deployment concerns.
- Added `portfolio/healthcheck.py`, a dependency-free local healthcheck template that reports required environment keys without printing their values.
- Recorded concrete extension and evaluation work below.

## Upstream attribution and license

The upstream repository and its contributors retain authorship of upstream code. This fork preserves upstream license and copyright files. GitHub metadata reports: `MIT`. Review all nested dependencies and notices before redistribution. This profile does not claim authorship of upstream code.

## Extension plan

1. Reproduce the upstream quickstart in an isolated environment and capture dependency/version failures.
2. Add a thin authenticated integration boundary rather than changing upstream business logic.
3. Add fixture-based tests for authorization, prompt/data separation, retrieval citations, and failure handling.
4. Measure latency, retrieval quality, cost, and groundedness on a consented, versioned evaluation set.
5. Keep secrets in deployment configuration; never commit API keys or private documents.

## Scope

This is a learning, customization, and integration study. It is not the original project, employer work, or a claim that every upstream feature was independently implemented by Shoaib Hassan.
