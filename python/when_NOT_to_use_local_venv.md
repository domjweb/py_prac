# **When NOT to use current directory venv (./venv)**

## **❌ Don't use ./venv when:**
### **Multiple related projects**
```shell
workspace/
├── project1/  # Flask app
├── project2/  # Flask API  
└── project3/  # Flask microservice
```

All use same Flask version - one `~/venvs/flask-dev` is better

### **Temporary/throwaway code**

- Quick scripts like your 121525.py
- One-off data analysis
- Testing snippets

### **Shared development**

- Team projects where everyone uses same environment path
- Docker containers that expect specific venv locations
- CI/CD that references ~/venvs/project-name

### **Disk space concerns**

- Limited storage (each venv ~20-50MB)
- Working on many small projects
- Frequently creating/deleting project folders
- System-wide tools

### **System-wide tools**

```shell
~/venvs/tools     # For black, flake8, pytest
~/venvs/jupyter   # For data science notebooks
```




