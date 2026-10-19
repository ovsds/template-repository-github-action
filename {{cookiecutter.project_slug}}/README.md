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

- [mise](https://mise.jdx.dev/installing-mise.html), activated in the shell (`eval "$(mise activate zsh)"`)

All other tools are pinned in [mise.toml](mise.toml).

### mise tasks

For all commands see [mise.toml](mise.toml) or `mise tasks ls`.

## License

[MIT](LICENSE)
