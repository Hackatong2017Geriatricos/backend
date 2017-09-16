#!/usr/bin/env bash

conda remove --yes -n geriatrico35 --all
conda env create --force -f environment.yml
conda clean -y --all
