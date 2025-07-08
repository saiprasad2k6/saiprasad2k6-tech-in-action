# saiprasad2k6-tech-in-action



## Python Setup

### Setting Up Virtual Environment

#### 1. Create a Virtual Environment

```bash
# Create a virtual environment named 'venv'
python3 -m venv venv
```

#### 2. Activate the Virtual Environment

```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

#### 3. Deactivate the Virtual Environment

```bash
deactivate
```

### Managing Dependencies

#### 1. Install Packages

```bash
# Install a specific package
pip install package_name

# Install from requirements.txt
pip install -r requirements.txt
```

#### 2. Create/Update requirements.txt

```bash
# Generate requirements.txt with current packages
pip freeze > requirements.txt
```

#### 3. Install Development Dependencies

```bash
# Install packages for development (optional)
pip install -r requirements-dev.txt
```

### Common Workflow

1. **Initial Setup:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Daily Work:**
   ```bash
   source venv/bin/activate
   # Run your Python programs
   python your_script.py
   ```

3. **Adding New Dependencies:**
   ```bash
   pip install new_package
   pip freeze > requirements.txt
   ```

4. **End of Session:**
   ```bash
   deactivate
   ```

