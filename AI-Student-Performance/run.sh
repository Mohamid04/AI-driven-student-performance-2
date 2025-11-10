#!/bin/bash

# AI-Driven Assessment of Student Performance Trends
# Linux/Mac Startup Script

echo ""
echo "============================================================"
echo "AI-Driven Assessment of Student Performance Trends"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3 from https://www.python.org/"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "ERROR: pip3 is not installed"
    echo "Please install pip3"
    exit 1
fi

echo "Checking dependencies..."

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install dependencies"
        exit 1
    fi
fi

echo ""
echo "Starting Flask server..."
echo ""
echo "Visit: http://localhost:5000"
echo ""
echo "Demo Credentials:"
echo "  Email: arjun@gmail.com"
echo "  Password: any password"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
