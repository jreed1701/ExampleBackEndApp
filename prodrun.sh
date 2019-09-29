#!/usr/bin/env bash
rm db/*
export ENV=PROD
python main.py prod