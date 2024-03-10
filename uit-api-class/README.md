# **Poetry Installation & Fast Api With Poetry**

### **Step 1: Install pipx**

- Open your terminal In Your Working Folder.
- Install pipx using pip: Write this command in your terminal: python -m pip install --user pipx

### **Step 2: Ensure pipx's binary directory is in your PATH: python Write this command in your terminal:**
- -m pipx ensurepath

### **Step 3:** 
- After step 2 Restart your terminal to apply the PATH update.

### **Step 4:**
- run the command pipx install poetry

### **Step 5:**
- To check the version run poetry --version

### **Step 6:**
- Create a new project with poetry new uit-api-class --name uitclass

### **Step 7:**
- open the sub folder inside of the parent folder, in this case uitclass

### **Step 8:** 
- Now create a new file named main.py

### **Step 9: After creating main.py file run command:** 
- poetry install in your terminal

### **Step 9 (optional):** 
- Check the version of python with the command poetry run python --version

### **Step 10:** 
- poetry add fastapi

### **Step 11:**
- poetry add uvicorn[standard]

### **Step 12:** 
- poetry run uvicorn uitclass.main:app to run your api on localhost server
