#!/usr/bin/env python3
"""
Startup validation script for interview-flow-AI2026 backend.
Checks environment configuration and dependencies before starting the server.
"""

import os
import sys
import importlib.util
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.10 or higher."""
    if sys.version_info < (3, 10):
        print("❌ Python 3.10+ required")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version_info.major}.{sys.version_info.minor}")
    return True


def check_environment_variables():
    """Check required environment variables."""
    required_vars = {
        'GITHUB_TOKEN': 'GitHub Models API token'
    }
    
    optional_vars = {
        'ENVIRONMENT': 'Environment mode (development/production)',
        'AZURE_OPENAI_KEY': 'Legacy Azure OpenAI key (optional)',
    }
    
    missing = []
    warnings = []
    
    for var, description in required_vars.items():
        if not os.getenv(var):
            missing.append(f"❌ {var}: {description}")
        else:
            print(f"✅ {var} is set")
    
    for var, description in optional_vars.items():
        if not os.getenv(var):
            warnings.append(f"⚠️  {var}: {description} (optional)")
        else:
            print(f"✅ {var} is set")
    
    if missing:
        print("\nMissing required environment variables:")
        for msg in missing:
            print(msg)
        print("\nRun: ./setup-env.sh to configure")
        return False
    
    if warnings:
        print("\nOptional environment variables not set:")
        for msg in warnings:
            print(msg)
    
    return True


def check_dependencies():
    """Check if required Python packages are installed."""
    required_packages = [
        'fastapi',
        'uvicorn',
        'openai',
        'python-dotenv',
        'pydantic',
        'slowapi',
    ]
    
    missing = []
    
    for package in required_packages:
        spec = importlib.util.find_spec(package)
        if spec is None:
            missing.append(f"❌ {package}")
        else:
            print(f"✅ {package} installed")
    
    if missing:
        print("\nMissing required packages:")
        for msg in missing:
            print(msg)
        print("\nRun: pip install -r requirements.txt")
        return False
    
    return True


def check_files():
    """Check if required files exist."""
    required_files = [
        'main.py',
        'prompts.py',
        'requirements.txt',
    ]
    
    missing = []
    
    for file in required_files:
        if not Path(file).exists():
            missing.append(f"❌ {file}")
        else:
            print(f"✅ {file} exists")
    
    if missing:
        print("\nMissing required files:")
        for msg in missing:
            print(msg)
        return False
    
    return True


def main():
    """Run all validation checks."""
    print("=" * 60)
    print("Interview-flow-AI2026 Backend Startup Validation")
    print("=" * 60)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("Required Files", check_files),
        ("Dependencies", check_dependencies),
        ("Environment Variables", check_environment_variables),
    ]
    
    all_passed = True
    
    for name, check_func in checks:
        print(f"\n--- {name} ---")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ All checks passed! You can start the server.")
        print("   Run: uvicorn main:app --reload")
        return 0
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
