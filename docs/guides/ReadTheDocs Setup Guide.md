# ReadTheDocs Setup Guide

This guide will help you connect your GitHub repository to ReadTheDocs so your documentation is automatically built and published whenever you push changes.

## What is ReadTheDocs?

ReadTheDocs (RTD) is a free service that:
- Automatically builds your Sphinx documentation whenever you push to GitHub
- Hosts the documentation on a public URL
- Provides version management (latest, stable, and tagged versions)
- Generates PDF and ePub formats automatically
- Adds search functionality to your docs

**Your documentation will be available at:**
- `https://pipeworks-conditional-axis.readthedocs.io/en/latest/`

---

## Prerequisites

Before setting up ReadTheDocs, ensure:

- ✅ Your repository is pushed to GitHub
- ✅ The `.readthedocs.yaml` configuration file exists in the repository root
- ✅ The `docs/conf.py` Sphinx configuration exists
- ✅ The `docs/index.rst` entry point exists
- ✅ Documentation dependencies are listed in `pyproject.toml` under `[project.optional-dependencies]` → `docs`

All of these are already set up in this repository!

---

## Step-by-Step Setup

### 1. Create a ReadTheDocs Account

1. Go to [https://readthedocs.org/](https://readthedocs.org/)
2. Click **Sign Up** in the top right
3. Choose **Sign up with GitHub** (recommended for automatic integration)
4. Authorize ReadTheDocs to access your GitHub account
5. Select which repositories ReadTheDocs can access:
   - Either grant access to all repositories (easier)
   - Or select specific repositories including `pipeworks_entity_state_generation`

### 2. Import Your Project

1. After signing in, click **Import a Project** on your dashboard
2. You'll see a list of your GitHub repositories
3. Find `pipeworks_entity_state_generation` in the list
4. Click the **+** button next to it (or click **Import** if it shows that instead)

### 3. Configure the Project

On the project import page:

**Project Details:**
- **Name**: `pipeworks-conditional-axis` (or your preferred name)
- **Repository URL**: Should auto-fill from GitHub
- **Repository type**: Git
- **Default branch**: `main`
- **Default version**: `latest`

**Advanced Settings** (click Show Advanced Options if needed):
- **Programming Language**: Python
- **Documentation type**: Sphinx Html
- **Requirements file**: Leave blank (we use pyproject.toml)
- **Python configuration file**: Leave blank
- **Use system packages**: ❌ Unchecked
- **Privacy Level**: Public

Click **Next** to continue.

### 4. Verify Configuration

ReadTheDocs will automatically detect the `.readthedocs.yaml` file and use those settings:

```yaml
# .readthedocs.yaml specifies:
- Python 3.12
- Ubuntu 22.04 build environment
- Install from pyproject.toml with [docs] extras
- Build HTML, PDF, and ePub formats
```

You don't need to change anything in the web interface if `.readthedocs.yaml` is present!

### 5. Build the Documentation

1. Click **Build Version** button
2. ReadTheDocs will:
   - Clone your repository
   - Install Python 3.12
   - Install your package with `pip install -e ".[docs]"`
   - Run Sphinx to build the HTML docs
   - Generate PDF and ePub versions

3. Wait for the build to complete (usually 2-5 minutes)
4. Check the build log if there are any errors

### 6. View Your Documentation

Once the build succeeds:

1. Click **View Docs** button
2. Your documentation will be live at:
   - **Latest**: `https://pipeworks-conditional-axis.readthedocs.io/en/latest/`
   - **Direct link**: `https://<your-project-name>.readthedocs.io/`

---

## Automatic Builds

Now that ReadTheDocs is connected:

1. **Every push to GitHub** triggers a new documentation build
2. **Pull requests** can trigger preview builds (enable in settings)
3. **Tags** create versioned documentation (e.g., v1.0.0)

No manual deployment needed! Just push and ReadTheDocs handles the rest.

---

## Customizing Your ReadTheDocs Project

### Setting up Badges

Add a documentation badge to your README.md:

```markdown
[![Documentation Status](https://readthedocs.org/projects/pipeworks-conditional-axis/badge/?version=latest)](https://pipeworks-conditional-axis.readthedocs.io/en/latest/?badge=latest)
```

### Versioning

To create versioned documentation:

1. Create a git tag: `git tag -a v1.0.0 -m "Version 1.0.0"`
2. Push the tag: `git push origin v1.0.0`
3. ReadTheDocs will automatically build docs for that version
4. Users can select versions from a dropdown in the docs

### Custom Domains

To use a custom domain (e.g., `docs.yoursite.com`):

1. Go to **Admin** → **Domains** in your ReadTheDocs dashboard
2. Add your custom domain
3. Update your DNS records as instructed
4. ReadTheDocs will provision an SSL certificate automatically

### Environment Variables

If you need to pass secrets or environment variables to the build:

1. Go to **Admin** → **Environment Variables**
2. Add key-value pairs
3. Mark as **Secret** if they contain sensitive data
4. Access them in `conf.py` with `os.environ.get('VAR_NAME')`

---

## Troubleshooting

### Build Failed: Module Not Found

**Problem**: Build log shows `ModuleNotFoundError`

**Solution**: Ensure all dependencies are listed in `pyproject.toml` under `[project.optional-dependencies] → docs`

### Build Failed: Sphinx Configuration Error

**Problem**: `Config error: ...`

**Solution**: Test the build locally first:
```bash
cd docs
sphinx-build -b html . _build/html
```
Fix any errors locally before pushing.

### Documentation Not Updating

**Problem**: Changes aren't showing up on ReadTheDocs

**Solution**:
1. Check that you pushed to the correct branch (usually `main`)
2. Go to **Builds** in ReadTheDocs dashboard
3. Click **Build Version** to manually trigger a rebuild
4. Clear your browser cache (Ctrl+Shift+R or Cmd+Shift+R)

### Build is Slow

**Problem**: Documentation takes a long time to build

**Solution**:
- ReadTheDocs builds are usually slower than local builds (2-5 minutes is normal)
- Large projects with many pages may take longer
- Consider using `html_theme_options` in `conf.py` to disable features you don't need

### Want to Build Locally with Same Environment?

To replicate ReadTheDocs' build environment locally:

```bash
# Install exact dependencies
pip install -e ".[docs]"

# Build with same command ReadTheDocs uses
cd docs
sphinx-build -b html . _build/html

# View the result
open _build/html/index.html
```

---

## Additional Resources

- **ReadTheDocs Documentation**: [https://docs.readthedocs.io/](https://docs.readthedocs.io/)
- **ReadTheDocs Build Process**: [https://docs.readthedocs.io/en/stable/builds.html](https://docs.readthedocs.io/en/stable/builds.html)
- **Sphinx Documentation**: [https://www.sphinx-doc.org/](https://www.sphinx-doc.org/)
- **ReadTheDocs YAML Config**: [https://docs.readthedocs.io/en/stable/config-file/v2.html](https://docs.readthedocs.io/en/stable/config-file/v2.html)

---

## Quick Checklist

Before connecting to ReadTheDocs:

- [ ] Repository is on GitHub
- [ ] `.readthedocs.yaml` exists in repository root
- [ ] `docs/conf.py` Sphinx configuration is complete
- [ ] `docs/index.rst` entry point exists
- [ ] Documentation builds successfully locally
- [ ] All dependencies are in `pyproject.toml` under `docs` extras

After connecting:

- [ ] ReadTheDocs account created and linked to GitHub
- [ ] Project imported on ReadTheDocs
- [ ] First build completed successfully
- [ ] Documentation is accessible at the public URL
- [ ] Badge added to README.md (optional but recommended)

---

## Support

If you encounter issues:

1. Check the ReadTheDocs build logs first (most informative)
2. Test the build locally to isolate the problem
3. Consult [ReadTheDocs community support](https://docs.readthedocs.io/en/stable/support.html)
4. Check [Sphinx troubleshooting docs](https://www.sphinx-doc.org/en/master/usage/advanced/troubleshooting.html)

Happy documenting! 📚
