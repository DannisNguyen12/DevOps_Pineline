# DevOps Pipeline

This repository demonstrates a CI/CD pipeline for a simple Python application.

## 🚀 Project Overview

A simple Python project that demonstrates CI/CD pipeline concepts with:
- `hello.py` - A basic function returning "Hello, World!"
- `test.py` - Unit tests for the hello function
- `buildspec.yml` - AWS CodeBuild configuration
- `requirements.txt` - Python dependencies

## 🛠️ Local Development

### Prerequisites
- Python 3.8+
- pip

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest test.py -v

# Run with coverage
python -m pytest test.py --cov=hello --cov-report=term
```

### Validate Code
```bash
# Check syntax
python -m py_compile hello.py test.py

# Run tests
python -m pytest test.py -v
```

## 🔄 CI/CD Pipeline

### AWS CodeBuild Configuration

The `buildspec.yml` file defines the following phases:

#### Install Phase
- Sets up Python 3.11 runtime
- Upgrades pip
- Installs dependencies from `requirements.txt`
- Installs testing tools (pytest, pytest-cov)

#### Pre-build Phase
- Validates Python syntax compilation
- Checks that all imports work correctly

#### Build Phase
- Runs unit tests with verbose output
- Generates test coverage reports
- Requires minimum 80% code coverage

#### Post-build Phase
- Prepares build artifacts
- Generates coverage reports

### Build Artifacts
- `coverage.xml` - Test coverage report
- `test.py` - Test file
- `hello.py` - Source code

### Cache Configuration
- Caches pip dependencies for faster subsequent builds

## 🚀 Deployment

### AWS CodeBuild
1. Create a CodeBuild project
2. Use this repository as source
3. The `buildspec.yml` will handle the build process automatically

### Local Testing
```bash
# Test the build process locally
python -m pytest test.py -v --cov=hello --cov-report=xml
```

## 📊 Test Coverage

The build requires minimum 80% code coverage. Current coverage includes:
- Function return values
- Import validation
- Basic functionality tests

## 🔧 Extending the Build

### Add More Tests
```python
# Add to test.py
def test_hello_world_length():
    assert len(hello_world()) > 0

def test_hello_world_type():
    assert isinstance(hello_world(), str)
```

### Add Code Quality Checks
Update `buildspec.yml` to include:
```yaml
# In build phase
- flake8 hello.py test.py --max-line-length=88
- black --check hello.py test.py
```

### Add More Dependencies
Add to `requirements.txt`:
```
requests>=2.28.0
flask>=2.3.0
```

## 📝 License

This project is for educational purposes demonstrating CI/CD concepts.
