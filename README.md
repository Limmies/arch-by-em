# arch.by.em

Emma Steyn’s architectural portfolio. Plain HTML, CSS and JavaScript; no build or dependencies. The complete website is in `dist/`.

## GitHub Pages

Create a public repository and upload this project, including `.github/workflows/pages.yml`. In repository **Settings → Pages**, select **GitHub Actions** as the source. Each push to `main` publishes `dist/`. The deployment’s URL appears in the Actions run and Pages settings.

All asset URLs are relative, so the website works at a repository subpath such as `/arch-by-em/`.

## Local preview

Run `python3 -m http.server 8080 --directory dist` and open `http://localhost:8080`.

## Editing imagery

Project details and gallery image filenames are at the top of `dist/app.js`. `slides` puts selected renders before portfolio spreads. Covers reference files in `dist/assets/`; the hero is in `dist/index.html`. Add `imageFit: 'contain'` for drawings and models that should remain fully visible.

The supplied portfolio PDFs are downloadable website content. Source project PDFs are not needed to serve the website. Image selection is provisional pending Emma’s review.
