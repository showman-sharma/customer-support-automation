# Customer Support Email Automation

> **Historical project / learning prototype.** This repository is preserved as an earlier exploration of combining email automation with ML-based message classification. It is not presented as a production-ready customer-support system.

## Overview

This project explores a simple support workflow built around the Gmail API:

1. authenticate a user's mailbox,
2. collect incoming support emails,
3. classify the message into a support category,
4. select and send a relevant response,
5. capture user feedback, and
6. either mark the issue resolved or route it for human follow-up.

The repository predates my current production-AI work and is useful mainly as a record of an earlier attempt to connect **ML inference with a real application workflow**, rather than as an example of my current engineering standards.

## Repository structure

The codebase includes modules for:

- Gmail authentication and message handling,
- email classification,
- response generation / templates,
- user feedback handling,
- simple workflow orchestration.

## Security note

Do **not** commit OAuth credentials, access tokens, refresh tokens, API keys, or private certificates to the repository. Local credential files are intentionally excluded through `.gitignore`.

If you fork or reuse this project, create new credentials for your own Google Cloud project and keep them outside version control.

## Status

**Archived in spirit, retained for learning history.**

For more recent AI systems work, see:

- [agentic_rag](https://github.com/showman-sharma/agentic_rag)
- [drug_ae_reasoner](https://github.com/showman-sharma/drug_ae_reasoner)
- [ai_blog_workflow](https://github.com/showman-sharma/ai_blog_workflow)
