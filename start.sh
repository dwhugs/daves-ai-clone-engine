#!/bin/bash

echo "👉 Setting up EMO models..."
python emo/download_models.py

echo "🚀 Starting Dave AI Clone..."
python davesaiclone.py
