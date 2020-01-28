## <a href="https://lukeconibear.github.io/" target="_blank">Personal website</a>
### Development
- <a href="https://www.python.org/" target="_blank">Python</a>  
- <a href="https://palletsprojects.com/p/flask/" target="_blank">Flask</a>  
- If packages changes, then update `requirements.txt` using `pip freeze > requirements.txt`  

### Deployment
- <a href="https://pythonhosted.org/Frozen-Flask/" target="_blank">Frozen flask</a>  
  - Build command: `python freeze.py`  
  - Publish directory: `build`  
  - Copy over the newly built static index.html: `cp build/index.html .`  
  - Update git  
