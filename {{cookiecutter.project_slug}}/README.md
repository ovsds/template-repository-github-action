# {{cookiecutter.project_name}}

[![CI](https://github.com/{{cookiecutter.owner_github_login}}/{{cookiecutter.project_slug}}/workflows/Check%20PR/badge.svg)](https://github.com/{{cookiecutter.owner_github_login}}/{{cookiecutter.project_slug}}/actions?query=workflow%3A%22%22Check+PR%22%22)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-{{ cookiecutter.marketplace_name.replace(' ',  '%20') }}-blue.svg)](https://github.com/marketplace/actions/{{cookiecutter.marketplace_slug}})

{{ cookiecutter.project_name }}

## Usage

### Example

```yaml
jobs:
  {{cookiecutter.marketplace_slug}}:
    steps:
      - name: {{cookiecutter.marketplace_name}}
        id: {{cookiecutter.marketplace_slug}}
        uses: {{cookiecutter.owner_github_login}}/{{cookiecutter.project_slug}}@v1
```

### Action Inputs

```yaml
inputs:
  placeholder:
    description: |
      Placeholder input to be replaced by real inputs
    required: true
    default: "placeholder"
```

### Action Outputs

```yaml
outputs:
  placeholder:
    description: |
      Placeholder output to be replaced by real outputs
{%- if cookiecutter.action_type == 'composite' %}
    value: ${{ "{{" }}steps.placeholder.outputs.placeholder }}
{%- endif %}
```

## Development

### Global dependencies

- [Taskfile](https://taskfile.dev/installation/)
- [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)
{%- if cookiecutter.with_zizmor == 'true' %}
- [zizmor](https://woodruffw.github.io/zizmor/installation/) - used for GHA security scanning
{%- endif %}

### Taskfile commands

For all commands see [Taskfile](Taskfile.yaml) or `task --list-all`.

## License

[MIT](LICENSE)
