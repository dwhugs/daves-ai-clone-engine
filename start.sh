#!/bin/bash

echo "Running first-time EMO model setup..."
python emo/download_models.py

echo "Starting Dave AI Clone..."
python davesaiclone.py
