# Blog Site

A full-featured blogging platform built with Django. Readers can explore published posts, browse categories, search content, and join the discussion; authenticated users can manage content from a dedicated dashboard.

**Live site:** [blog-site-t39b.onrender.com](https://blog-site-t39b.onrender.com/)

## Highlights

- Featured and recent post feeds on the home page
- Post pages with image uploads and reader comments
- Category browsing and keyword search across titles, summaries, and post content
- Account registration, sign-in, sign-out, and optional Google authentication
- Dashboard for creating and managing posts, categories, and users
- Draft/published workflow and featured-post support
- Configured for deployment on Render

## Built with

- Python 3.11+
- Django 6.1
- SQLite
- Bootstrap 4 with Django Crispy Forms
- Pillow for image uploads
- Django Allauth for social authentication

## Project structure

```text
blog/
??? blog_main/       # Project settings, root URLs, static assets, authentication views
??? blogs/           # Blog, category, comment models and public-facing views
??? dashboards/      # Authenticated content-management dashboard
??? aboutUs/         # About section and social links
??? templates/       # Site and dashboard templates
??? media/           # Uploaded post images
??? requirements.txt # Python dependencies
??? build.sh         # Render build script
??? render.yaml      # Render service configuration
```

## Getting started

### 1. Clone and enter the project

```bash
git clone <your-repository-url>
cd blog
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=replace-with-a-long-random-secret
DEBUG=True
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000

# Optional: required only for Google sign-in
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### 5. Prepare the database and run the site

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser. The Django admin is available at `/admin/`, and the dashboard is at `/dashboard/` after sign-in.

## Managing content

1. Sign in and open `/dashboard/`.
2. Create one or more categories.
3. Add posts with a title, featured image, summary, body, and publication status.
4. Set a post as featured to show it in the home-page featured section.

Only posts marked **Published** are shown on public pages.

## Deployment

The repository includes a `render.yaml` blueprint and `build.sh` script for Render. The build process installs dependencies, collects static files, and applies migrations.

Set these environment variables in Render before deploying:

```text
SECRET_KEY=<generated-by-render-or-your-own-secret>
DEBUG=False
CSRF_TRUSTED_ORIGINS=https://your-service.onrender.com
GOOGLE_CLIENT_ID=<optional>
GOOGLE_CLIENT_SECRET=<optional>
```

## Useful commands

```bash
# Create database migrations after model changes
python manage.py makemigrations

# Apply migrations
