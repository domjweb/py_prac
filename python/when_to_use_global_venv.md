# **When to use global venv**
## **Multi-project environments**

When you have multiple related projects that share the same dependencies:
```shell
~/venvs/web-dev    # Used across Flask, Django projects

~/venvs/data-sci   # Used across pandas, jupyter projects

~/venvs/testing    # Used for general experimentation
```
## **System organization**

- Keeps all venvs in one predictable location
- Easier to manage and clean up unused environments
- Better for developers who work on many small projects

## **Shared development environments**

- Team environments where everyone uses the same venv setup
- CI/CD pipelines that reference specific environment paths
- When switching between multiple versions of the same project

## **Personal workflow preferences**

Some developers prefer: