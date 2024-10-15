# {{cookiecutter.project_name}}

[![CI](https://github.com/{{cookiecutter.owner_github_login}}/{{cookiecutter.project_slug}}/workflows/Check%20PR/badge.svg)](https://github.com/{{cookiecutter.owner_github_login}}/{{cookiecutter.project_slug}}/actions?query=workflow%3A%22%22Check+PR%22%22)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-{{ cookiecutter.marketplace_name.replace(' ',  '%20') }}-blue.svg)](https://github.com/marketplace/actions/{{cookiecutter.marketplace_slug}})

{{cookiecutter.project_description}}

## Usage

### Example

```yaml
jobs:
  {{cookiecutter.marketplace_slug}}:
    permissions:
      contents: read

    steps:
      - name: {{cookiecutter.marketplace_name}}
        id: {{cookiecutter.marketplace_slug}}
        uses: {{cookiecutter.owner_github_login}}/{{cookiecutter.project_slug}}@v1
```

### Action Inputs

| Name          | Description  | Default |
| ------------- | ------------ | ------- |
| `placeholder` | Placeholder. |         |

### Action Outputs

| Name          | Description  |
| ------------- | ------------ |
| `placeholder` | Placeholder. |

## Development

### Global dependencies

- [Taskfile](https://taskfile.dev/installation/)
- [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)

### Taskfile commands

For all commands see [Taskfile](Taskfile.yaml) or `task --list-all`.

## License

[MIT](LICENSE)
