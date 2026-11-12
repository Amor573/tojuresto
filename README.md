# Toju Resto — Django food-ordering application

An existing Django web application prototype exploring food listings, customer-facing pages, cart management and payment flows. The source includes the application modules `tojuweb`, `cart` and `payment`, plus Django views and templates.

**Portfolio status:** source project requiring security cleanup and fresh end-to-end validation. It is **not presented here as a currently audited production service**.

## Architecture

```text
Browser / HTML templates
        |
    Django URLs
       / | \
  tojuweb cart payment
       \ | /
      Data layer
```

The repository demonstrates backend routing, sessions/cart logic, templates, Django models, payment-flow design and container configuration. The code predates the current portfolio verification work and should be reviewed before deployment.

## Review or test safely

Use a disposable local environment and a new, non-sensitive database. Do not start the repository against real customer data. Review `toju_food/settings.py` for environment-based settings before running `manage.py` commands. After hardening, a suitable verification sequence is:

```bash
python -m venv .venv
# Activate the environment on your OS
python -m pip install -r requirements.txt
python manage.py check --deploy
python manage.py test
```

The commands above are *acceptance criteria*, not a claim they currently pass. The repository contains legacy tracked local artifacts; a `.gitignore` now limits new accidental commits but **does not remove files from the current branch or Git history**.

## Publication checklist

1. Audit tracked files and **Git history** for private data and credentials; rotate any exposed secrets and keys outside GitHub.
2. Replace hardcoded secrets and debug configuration with reviewed environment-driven settings without breaking any active deployment.
3. Remove runtime artifacts from version control in a reviewed cleanup change; carefully inspect historical data-removal requirements.
4. Add isolated automated tests for cart, checkout and failed payment paths.
5. Validate deployment behavior, permissions and payment callbacks in a non-production environment.
6. Capture sanitized screenshots demonstrating the actual user journey and architecture. Never publish customer information or payment identifiers.

See [portfolio evidence criteria](docs/portfolio-proof.md) for safe screenshot guidance.
