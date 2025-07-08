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
   python script.py
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