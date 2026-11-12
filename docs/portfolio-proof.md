# Portfolio evidence to collect for Toju Resto

## Show a complete, reproducible customer journey

Capture from a clean demo database with synthetic customers and products:

1. Product listing and product detail page showing the interface.
2. Cart item addition, quantity adjustment and subtotal.
3. Checkout confirmation **using a test-mode payment flow only**.
4. Clear transaction state in Django admin or a test fixture.
5. Successful test run, CI job URL, commit SHA and Django version.

For technical reviewers, describe the Django app boundaries, data model, session/cart decisions, validation rules, payment callbacks and deployment topology.

## Screenshot rules

Never publish customer names, phone numbers, addresses, real transaction identifiers, API keys, email addresses, session cookies, admin URLs, exposed service IP addresses or internal business records. Crop or redact those details before images are committed. Screenshots of a payment UI must clearly show a sandbox or synthetic environment.

## Evidence status

No validated screenshots from the user's local Windows `Screenshots` folder are currently included. A public repository proves source availability, not a successful end-to-end deployment.