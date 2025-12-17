
# **When to use current directory venv (./venv)**
Based on your current file structure, here's when a local venv makes sense:

## **✅ Use ./venv when:**
Learning/Practice projects (like your current setup)

- Individual exercise files like 121525.py
- Temporary code experiments
- Tutorial follow-alongs

## **Self-contained projects**

- Single-purpose applications
- Projects with unique dependencies
- When sharing code via git (venv stays with project)

## **Different Python versions per project**

- Project A needs Python 3.9
- Project B needs Python 3.11

## **Conflicting dependencies**

- Project needs Django 3.x
- Another project needs Django 4.x

## **For your current workspace:**

```shell
# From /home/domjweb/workspace/Python/Practice/
python3 -m venv ./venv && source ./venv/bin/activate
```

This creates:
```shell
Practice/
├── python/
│   └── print_statements/
│       └── 121525.py
└── venv/              # Isolated to this practice folder
    ├── bin/
    └── lib/
```

## **Benefits for your use case:**
- Keeps practice environment separate from other projects
- Easy cleanup (just delete the Practice folder)
- VS Code automatically detects local venvs
- Dependencies won't interfere with other Python work
