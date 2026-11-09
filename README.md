# Rapha Senior Independence Shared Living

A Flask website for Rapha Senior Independence Shared Living.

## Run locally

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment.
3. Install dependencies:

   ```powershell
   py -m pip install -r requirements.txt
   ```

4. Start the development server:

   ```powershell
   py app.py
   ```

5. Open <http://127.0.0.1:5000/>.

## Pages

- `/` — Home, FAQs, and Contact
- `/about` — About Us
- `/housing` — Housing, independent living, transportation, and resident information
- `/meals` — Meals and Food Services

## Deploy to Render

The included `render.yaml` configures a free Render web service using Gunicorn.
Push this project to a GitHub repository, then create a new Render Blueprint from
that repository. Render will build and start the Flask app from the configuration.
After deployment, add the custom domain in Render and follow the DNS instructions
Render provides at your domain's DNS provider.
