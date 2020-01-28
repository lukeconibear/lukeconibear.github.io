## <a href="https://lukeconibear.github.io/" target="_blank">Personal website</a>
### Development
- <a href="https://www.python.org/" target="_blank">Python</a>  
- <a href="https://palletsprojects.com/p/flask/" target="_blank">Flask</a>  
- If packages changes, then update `requirements.txt` using `pip freeze > requirements.txt`  
- Based on the helpful guide by <a href="https://medium.com/@francescaguiducci/how-to-build-a-simple-personal-website-with-python-flask-and-netlify-d800c97c283d" target="_blank">Francesca Guiducci</a>  

### Deployment
- <a href="https://pythonhosted.org/Frozen-Flask/" target="_blank">Frozen flask</a>  
  - Build command: `python freeze.py`  
  - Publish directory: `build`  
  - Copy over the newly built static index.html: `cp build/index.html .`  
  - Update git  
