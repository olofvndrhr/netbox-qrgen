#!/usr/bin/env just --justfile

default: show_receipts

set shell := ["bash", "-uc"]
set dotenv-load := true
#set export

# aliases
alias s := show_receipts
alias i := show_system_info
alias p := prepare_workspace
alias l := lint
alias b := build

# variables
export asdf_version := "v0.11.2"

# default recipe to display help information
show_receipts:
    @just --list

show_system_info:
    @echo "=================================="
    @echo "os : {{os()}}"
    @echo "arch: {{arch()}}"
    @echo "home: ${HOME}"
    @echo "project dir: {{justfile_directory()}}"
    @echo "=================================="

install_asdf:
    @if asdf --version; then \
        echo "asdf already installed installed"; exit 1 \
    ;fi
    @echo "installing asdf"
    @echo "asdf version: ${asdf_version}"
    @git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch "${asdf_version}"
    @echo "adding asdf to .bashrc"
    @if ! grep -q ".asdf/asdf.sh" "${HOME}/.bashrc"; then \
        echo -e '\n# source asdf' >> "${HOME}/.bashrc" \
        ;echo 'source "${HOME}/.asdf/asdf.sh"' >> "${HOME}/.bashrc" \
        ;echo -e 'source "${HOME}/.asdf/completions/asdf.bash"\n' >> "${HOME}/.bashrc" \
    ;fi
    @echo "to load asdf either restart your shell or do: 'source \${HOME}/.bashrc'"

setup_asdf:
    @echo "installing asdf bins"
    # add plugins
    -@asdf plugin add python
    -@asdf plugin add just
    -@asdf plugin add direnv
    # install bins
    @asdf install
    # setup direnv
    @asdf direnv setup --shell bash --version latest

setup_hooks:
    @echo "preparing repo hooks"
    @if ! lefthook version; then \
        echo "lefthook not installed. please install it: https://github.com/evilmartians/lefthook"; exit 1 \
    ;fi
    @echo "installing pre-commit hooks" \
    @lefthook install

create_venv:
    @echo "creating venv"
    @python3 -m pip install --upgrade pip setuptools wheel
    @python3 -m venv venv

install_deps:
    @echo "installing dependencies"
    @pip3 install -r requirements.txt

install_deps_dev:
    @echo "installing dev dependencies"
    @pip3 install -r requirements_dev.txt

create_reqs:
    @echo "creating requirements"
    @pipreqs --mode gt --force

test_shfmt:
    @find . -type f \( -name "**.sh" -and -not -path "./.**" -and -not -path "./venv**" \) -exec shfmt -d -i 4 -bn -ci -sr "{}" \+;

test_black:
    @python3 -m black --check --diff netbox_qrgen/

test_pyright:
    @python3 -m pyright netbox_qrgen/

test_ruff:
    @python3 -m ruff --diff netbox_qrgen/

test_ci_conf:
    @woodpecker-cli lint .woodpecker/

test_pytest:
    @python3 -m tox -e basic

test_coverage:
    @python3 -m tox -e coverage

test_tox:
    @python3 -m tox

build_package:
    @python3 -m hatch build --clean

build_container:
    @docker build . -f development/Dockerfile -t netbox-dev:3.5

# install dependecies and set everything up
prepare_workspace:
    just show_system_info
    -just install_asdf
    just setup_asdf
    just create_venv
    just setup_hooks
    @echo -e "\n\033[0;32m=== ALL DONE ===\033[0m\n"

lint:
    just show_system_info
    -just test_ci_conf
    just test_black
    just test_pyright
    just test_ruff
    @echo -e "\n\033[0;32m=== ALL DONE ===\033[0m\n"

build:
    just build_container
    @echo -e "\n\033[0;32m=== ALL DONE ===\033[0m\n"
