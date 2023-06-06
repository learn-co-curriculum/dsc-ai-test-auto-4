```python
import requests
import os
from dotenv import load_dotenv
load_dotenv()

import markdown
import markdown2
import re 

from canvasapi import Canvas
from canvas_to_git import *
```

## 1. Connect to Canvas API


Add Canvas credentials. 

* The API key should be stored in your `.env` file.
* Change to the relevant Canvas instance as needed. 


```python
canvas_api_key = os.environ.get('CANVAS_TOKEN')
canvas_instance = "https://learning.flatironschool.com"
```

Connect to Canvas API by creating a Canvas instance.


```python
canvas = Canvas(canvas_instance, canvas_api_key)
```

## 2. Locate Course
For all of the methods available for the Course class, see [the Course documentation](https://canvasapi.readthedocs.io/en/stable/course-ref.html#course).

**To work with an existing course, input a course number.**


```python
course_number = 6996
```


```python
course = canvas.get_course(course_number)
print(course.name)
```

## 3. Extract Content

First get the course pages from Canvas.


```python
content = course.get_pages()
```

Next, use lists to gather the relevant page IDs, page contents, titles, and URLs.


```python
titles = []
page_ids = []
urls = []
contents = []

for page in content:
    pid = page.page_id
    page_ids += [pid]
    p = course.get_page(pid)
    titles += [p.title]
    urls += [p.url]
    contents += [p.body]
```

Then, extract the titles of lessons and labs only, ignoring any housekeeping/admin pages.


```python
# sanity check
titles
```


```python
zipped_content = list(zip(titles, page_ids, urls, contents))

# I am using list comprehension here to filter my titles
# but you may want to use another method, or manually generate a list
adj_titles = [title for title in zipped_content 
                if title[0].startswith('📚 Reading:')
                 or title[0].startswith('🔎 Lab:')]
```


```python
# sanity check to see what the tuple looks like
adj_titles[0]
```

## 4. Mirror Canvas Lessons to GitHub

Run the cell below to create the repo for the first time. 

**Change this cell to your course prefix


```python
prefix = None # 'ai-course-XXXX...-'
org_name = 'learn-co-curriculum'
```


```python
for title in adj_titles:
    repository_name = f'{prefix}{title[2]}'
    organization_name = org_name
    print(repository_name)
    
    # comment out the line below after repos have already been created
    create_github_repository(repository_name, organization_name)
    
    # create/update README
    content = title[3]
    file_path = 'README.md'
    file_title = title[0]
    file_content = f'# {file_title}\n\n{content}'  # Updated content of the file
    commit_message = 'Update file'  # Commit message for the file operation
    create_or_update_file(repository_name, organization_name, file_path, file_content, commit_message)
```
