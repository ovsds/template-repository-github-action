# Cookiecutter Template for GitHub Actions Repository

[![CI](https://github.com/ovsds/template-repository-github-action/workflows/Check%20PR/badge.svg)](https://github.com/ovsds/template-repository-github-action/actions?query=workflow%3A%22%22Check+PR%22%22)

Cookiecutter template that scaffolds a GitHub Action repository — composite (bash) or Node (TypeScript) — with CI, end-to-end tests, and release tagging wired up for the GitHub Marketplace.

For non-Action repos, see the sister template [`ovsds/template-repository`](https://github.com/ovsds/template-repository).

## What you get

A new repo with:

- `action.yaml` carrying Marketplace metadata and a placeholder input/output you replace.
- One of two action runtimes, chosen via the `action_type` prompt:
  - **`composite`** — `src/main.sh` shell entrypoint wired into `action.yaml` as a composite action.
  - **`node`** — TypeScript sources under `src/` (`action.ts`, `input.ts`, `main.ts`, `utils/`) bundled via `@vercel/ncc`, plus Vitest unit tests, ESLint config, and a `dist/` cleanliness check in CI. Runs on `node24` by default.
- Workflows under `.github/workflows/`:
  - `check-pr` — lint, plus tests and `dist/` verification for node actions.
  - `check-pr-title` — conventional-commit PR title check.
  - `e2e` — invokes the action against itself with a placeholder input and asserts the output.
  - `push-version-tags` — on release, publishes version tags via [`ovsds/push-version-tags-action`](https://github.com/ovsds/push-version-tags-action).
- A reusable `setup_environment` composite under `.github/actions/`.
- Tooling: `Taskfile.yaml`, `nvm`, `npm`, Prettier, `lint-staged`, Husky pre-commit, commitlint.
- A `task update-from-template` that re-runs cookiecutter against the existing repo to absorb upstream template changes.

Optional flags in `cookiecutter.json`:

- `with_zizmor` — adds [zizmor](https://woodruffw.github.io/zizmor/) GHA security scanning to `task lint`.
- `with_shellcheck` — adds shellcheck for `*.sh` files to lint and `lint-staged`.

## Quickstart

### Global dependencies

- [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

### Generate a new repo

```shell
cookiecutter https://github.com/ovsds/template-repository-github-action
```

You'll be prompted for the project name, marketplace name, action type (`composite` or `node`), Node version, and the optional flags above.

### Generate from inside an already-cloned repo

```shell
cookiecutter \
  --overwrite-if-exists \
  --output-dir ../ \
  https://github.com/ovsds/template-repository-github-action
```

## Development

### Global dependencies

- [Taskfile](https://taskfile.dev/installation/)
- [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)
- [zizmor](https://woodruffw.github.io/zizmor/installation/) - used for GHA security scanning

### Taskfile commands

For all commands see [Taskfile](Taskfile.yaml) or `task --list-all`.

## License

[MIT](LICENSE)
