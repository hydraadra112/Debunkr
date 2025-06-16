# Notes from Manns
For our front-end development, it is crucial that we adhere to the standards that have been set by professionals. So that, subong palang, ma amat amat na naton refine aton skills and work on our habits.

This is to ensure that we avoid the common mistakes that amateur web developers make. **Which is spaghetti, unmaintainable, and unmodularized code**. To avoid it, I propose a few rules para maging organized kita.

- All pages should be in a folder `$routes/page_name/` with a `+page.svelte` as the source code.
- All components that are being reused at least **twice** on multiple pages should be put under `$routes/components/`.
- Create a components folder `$routes/page_name/components/` for a specific page if it is only used in that page, and is used at least twice.
- Color palettes, typefaces, sizing, etc., should be defined globally (`global.css`) to ensure consistent styling.

These are simple spells, but they're quite unbreakable. These rules will return a greater investment in the future.

## Setup Development
To properly set up the front-end, run the following code:

```bash
npm install # installs all dependencies you will need

npm run dev -- --open # To run the front-end locally
```

For more information, visit the [SvelteKit](https://svelte.dev/docs/kit/introduction) documentation.

## Building
When we finish code and ready to deploy the app, we run:

```bash
npm run build
```

You can preview the production build with `npm run preview`.