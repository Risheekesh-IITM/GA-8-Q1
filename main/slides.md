---

marp: true
theme: custom
paginate: true
class: lead
-----------

<!--- Custom theme CSS for Marp -->

<!---
You can keep this file under version control (e.g., `slides.md`) and use the raw GitHub URL to render it with Marp CLI or online viewers.
--->

<style>
/* Custom theme: define colors, fonts, and page-number styling */
section {
  font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
}
:root {
  --brand-bg: #0b1220;
  --brand-accent: #06b6d4;
  --muted: #94a3b8;
}

/* Headings */
section h1, section h2, section h3 {
  color: white;
  text-shadow: 0 1px 0 rgba(0,0,0,0.25);
}

/* Body text */
section p, section li {
  color: #e6eef6;
}

/* Accent rule */
hr {
  border: 0;
  height: 3px;
  background: linear-gradient(90deg,var(--brand-accent),transparent);
  margin: 1rem 0 2rem 0;
}

/* Page number positioning (works together with `paginate: true`) */
.marpit-footer {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 0.5rem;
  color: var(--muted);
  font-size: 0.85rem;
  padding-right: 1.25rem;
}

/* Code block styling */
pre code {
  background: rgba(0,0,0,0.45);
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 0.9rem;
}

/* Small callout block */
.callout {
  background: rgba(255,255,255,0.03);
  border-left: 4px solid var(--brand-accent);
  padding: 0.6rem 0.8rem;
  border-radius: 4px;
  color: #dff6fb;
}
</style>

---

<!-- Title slide -->

# Product Documentation

> Maintainable Marp slides for product docs

* **Author:** Technical Writing Team
* **Contact:** [24f1001771@ds.study.iitm.ac.in](mailto:24f1001771@ds.study.iitm.ac.in)

---

<!-- Agenda -->

## Agenda

1. Overview
2. Installation & Usage
3. Architecture & API
4. Algorithm / Complexity
5. Release Notes & Maintenance
6. Contact

---

<!-- Overview slide with small callout -->

## Overview

This documentation covers the core product features, quickstart instructions, API surface, and algorithmic details required by engineers and integrators.

> **Why Marp?**
>
> * Keeps slides as plain Markdown (great for version control).
> * Easy to convert to PDF, HTML, PPTX using Marp CLI or CI.

---

## Installation & Quickstart

```bash
# clone repo
git clone https://github.com/your-username/product-docs.git
cd product-docs
# render slides to PDF using Marp CLI
npx @marp-team/marp-cli slides.md --pdf --theme-set ./ --allow-local-files
```

---

<!-- Background image slide -->

---

backgroundImage: url('[https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80](https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80)')
backgroundSize: cover
backgroundPosition: center

# Architecture Overview

> High-level diagram and flow (see repository `assets/architecture.png` for the editable source)

---

## API Surface

* `POST /v1/auth` — returns JWT
* `GET /v1/resources` — list resources
* `POST /v1/resources` — create resource

```json
{
  "id": "resource_123",
  "name": "Example"
}
```

---

## Algorithmic Complexity

We use a divide-and-conquer algorithm for batch reconciliation. The recurrence relation for the time complexity is:

$$
T(n) = 2,T\left(\frac{n}{2}\right) + n,\log n
$$

By the Master Theorem (case 2 with extra poly-log factor), the asymptotic bound is:

$$
T(n) = \Theta(n,\log n,\log n) = \Theta(n,(\log n)^2).
$$

**Space complexity:** $$S(n) = O(n)$$

---

## Release Notes & Maintenance

* Keep slide file `slides.md` under `main` branch (or `docs` branch if you prefer).
* Store assets (images, diagrams) in `assets/` and reference them with relative links when possible.

---

## Contributing

1. Edit `slides.md` in a feature branch.
2. Commit and open a PR targeting `main`.
3. CI should run `npx @marp-team/marp-cli slides.md --html` to validate rendering.

---

## Contact & License

If you have questions, email: **[24f1001771@ds.study.iitm.ac.in](mailto:24f1001771@ds.study.iitm.ac.in)**

* License: MIT

---

<!-- End slide with small footer note -->

footer: "Product Documentation — Technical Writing"
