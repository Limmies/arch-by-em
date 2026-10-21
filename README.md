# arch.by.em

Emma Steyn’s architectural portfolio. Plain HTML, CSS and JavaScript; no build or dependencies. The complete website is in `dist/`.

## GitHub Pages

The public website is https://limmies.github.io/arch-by-em/. Pushes to `main` publish `dist/` through the existing GitHub Actions workflow.

All asset URLs are relative, so the website works at a repository subpath such as `/arch-by-em/`.

## Local preview

Run `python3 -m http.server 8080 --directory dist` and open `http://localhost:8080`.

## Editing imagery

Project details and gallery image filenames are at the top of `dist/app.js`. `slides` puts selected renders before portfolio spreads. Covers reference files in `dist/assets/`; the hero is in `dist/index.html`. Add `imageFit: 'contain'` for drawings and models that should remain fully visible.

The supplied portfolio PDFs are downloadable website content. Source project PDFs are not needed to serve the website. Image selection is provisional pending Emma’s review.

## Contact form

The contact form posts to FormSubmit for delivery to emmasteyn4@icloud.com. On the first submission, Emma must follow the activation link emailed by FormSubmit before inbox delivery is enabled. The form keeps the default CAPTCHA, adds a honeypot, and uses the visitor’s email as Reply-To. Successful submissions return to `thank-you.html`. No email API key is stored in the website.

## Mobile verification

Phone layouts use 44px navigation targets, 48px gallery controls, a full-screen dialog, swipe navigation and 16px form inputs. Responsive WebP covers in `dist/assets/responsive/` preserve the original gallery images. Browser checks cover widths 320, 375, 390, 430, 768, 1024 and 1440px, overflow, gallery navigation and required-field validation.

Contact delivery verified on 21 October 2026: a labelled test submitted through the actual form was accepted by FormSubmit and the user confirmed receipt in Emma’s inbox.

## Kelp Line / Kommetjie

Added from Emma’s supplied `ste0st24 Kommetjie Presentation.pdf` (11 September 2026). The project’s selected renders and drawings are `dist/assets/kommetjie-*`; its complete web-optimized presentation is `dist/assets/kelp-line-kommetjie-presentation.pdf`. The cover is cropped from page 2 and has responsive WebP variants.

## Instagram photo strip

Eight selected public posts from @arch.by.em are stored locally in `dist/assets/instagram/`, with their original post URLs in `posts.json`. The strip advances every 4 seconds when visible, pauses on hover/focus and manual interaction, and provides previous, next and play/pause controls. Reduced-motion users start with autoplay off. This is a curated selection; importing new Instagram posts requires updating the assets and markup.
