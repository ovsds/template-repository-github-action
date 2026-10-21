#!/bin/bash

set -euo pipefail

# shellcheck source-path=SCRIPTDIR source=common.sh
source "$(dirname "${BASH_SOURCE[0]}")/common.sh"

function main() {
    INPUT_PLACEHOLDER=${INPUT_PLACEHOLDER:?"INPUT_PLACEHOLDER is not set"}
    set_output "placeholder" "${INPUT_PLACEHOLDER}"
}

main "$@"
