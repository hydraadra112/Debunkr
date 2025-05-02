module.exports = {
    content: ['./index.html', './src/**/*.{js,ts,jsx,tsx,svelte}'],
    theme: {
      extend: {
        fontFamily: {
          body: ['var(--font-body)'],
          heading: ['var(--font-heading)'],
          title: ['var(--font-title)'],
          mono: ['var(--font-mono)'],
        },
        colors: {
          c1: '#E2C275',
          c2: 'var(--color-c2)',
          c3: 'var(--color-c3)',
          c4: 'var(--color-c4)',
          error: 'var(--color-error)',
          success: 'var(--color-success)',
        },
      },
    },
    plugins: [
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),
    ],
  };
  