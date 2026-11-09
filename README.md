# CS184 Homework 3 — Path Tracing

Stephanie Yao and William Xu. The course repository remains the editable source for the report and original render images.

## Local review

Open `index.html`, or run `python3 -m http.server 8000` and visit http://localhost:8000.

The design uses a fixed light theme, Spectral/EB Garamond typography inspired by Stephanie's blog, and a simple academic report layout. All required experiments and image sets remain included. Images link to their original resolution. Print styles hide navigation and keep image/caption pairs together.

## Hosting plan (prepared, not activated)

- Final URL: https://suniyao.github.io/cs184/hw3/
- Existing course URL: https://cal-cs184-student.github.io/hw3-steph-writeup/
- `redirect.html` is a staged redirect, **not the current homepage**.
- `scripts/prepare-hosting.py` copies the report into `public/cs184/hw3/` in `/Users/stephanieyao/Desktop/personal-website/`. The existing Next.js static-export workflow will publish those public files. No global site styles or existing routes are changed.

Stage updates:

```sh
python3 scripts/prepare-hosting.py /Users/stephanieyao/Desktop/personal-website
```

After review, commit and publish the personal-site changes first. Verify the destination page and all images online. Only then activate the redirect:

```sh
python3 scripts/prepare-hosting.py /Users/stephanieyao/Desktop/personal-website --activate-redirect
```

This retains a readable course-repository backup as `report.html` and makes `index.html` redirect to the personal site. Commit and publish the course repository afterward. The redirect preserves section hashes with JavaScript and has a no-JavaScript fallback link. No deployment occurs merely by running the staging script.

Use the Desktop website checkout for all site work. Before rerunning the staging script, compare the report copies and preserve any edits made in that checkout. After redirect activation, `report.html` is the course-repository source.

## Experiments

Part 2 timings use 320 × 240, one sample/pixel, one thread, normal shading, excluding loading/construction. Raw measurements: `assets/bvh-timings.csv`. Part 4 images use fixed samples, before adaptive sampling. Part 5 uses a 2048-sample cap, 64-sample batches, tolerance 0.05, one light sample, and depth 5.

The course requires a PDF export of the complete webpage; inspect all images before submitting. No private assignment code is included in this repository.
