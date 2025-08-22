#!/usr/bin/env python3
"""
Convert markdown files to HTML with consistent styling.
This script converts all markdown files in the project to HTML while preserving
the styling and navigation structure.
"""

import os
import re
import markdown
from pathlib import Path

def get_base_css():
    """Extract CSS from the main index.html file."""
    return """
    <style>
    /* Inline CSS for immediate styling */
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 20px;
        background: #fff;
        max-width: 1200px;
        margin: 0 auto;
    }

    .header {
        background: linear-gradient(135deg, #FCE834 0%, #f9e71e 100%);
        padding: 2rem;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 2rem;
        border: 3px solid #2c3e50;
    }

    .header h1 {
        color: #2c3e50;
        margin: 0;
        font-size: 2.5rem;
    }

    .nav-breadcrumb {
        background: #f5f5f5;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        text-align: center;
    }

    .nav-breadcrumb a {
        display: inline-block;
        margin: 0.2rem;
        padding: 0.5rem 1rem;
        background: #FCE834;
        color: #2c3e50;
        text-decoration: none;
        border-radius: 6px;
        font-weight: 600;
    }

    .nav-breadcrumb a:hover {
        background: #2c3e50;
        color: #FCE834;
    }

    .btn {
        display: inline-block;
        padding: 0.5rem 1rem;
        margin: 0.2rem;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 500;
        transition: transform 0.2s ease;
    }

    .btn:hover {
        transform: translateY(-2px);
    }

    .btn-colab {
        background: linear-gradient(135deg, #4285f4 0%, #34a853 100%);
        color: white !important;
    }

    .btn-video {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white !important;
    }

    .btn-theory {
        background: #2c3e50;
        color: white !important;
    }

    .btn-principles {
        background: linear-gradient(135deg, #FCE834 0%, #f9e71e 100%);
        color: #2c3e50 !important;
        font-weight: 600;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50;
    }

    h1 {
        border-bottom: 3px solid #FCE834;
        padding-bottom: 0.5rem;
    }

    h2 {
        border-bottom: 2px solid #FCE834;
        padding-bottom: 0.5rem;
    }

    h3 {
        border-bottom: 1px solid #FCE834;
        padding-bottom: 0.3rem;
    }

    code {
        background: #f5f5f5;
        padding: 0.2rem 0.4rem;
        border-radius: 4px;
        font-family: 'Monaco', 'Menlo', 'Consolas', monospace;
    }

    pre {
        background: #f5f5f5;
        padding: 1rem;
        border-radius: 8px;
        overflow-x: auto;
        border-left: 4px solid #FCE834;
    }

    pre code {
        background: none;
        padding: 0;
    }

    blockquote {
        border-left: 4px solid #FCE834;
        margin: 0;
        padding: 1rem;
        background: #f9f9f9;
        font-style: italic;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin: 1.5rem 0;
        background: #fff;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    th {
        background: linear-gradient(135deg, #FCE834 0%, #f9e71e 100%);
        color: #2c3e50;
        padding: 1rem;
        text-align: left;
        font-weight: 600;
    }

    td {
        padding: 1rem;
        border-bottom: 1px solid #f5f5f5;
        vertical-align: top;
    }

    tr:hover {
        background-color: rgba(252, 232, 52, 0.1);
    }

    ul, ol {
        padding-left: 2rem;
    }

    li {
        margin: 0.5rem 0;
    }

    a {
        color: #2c3e50;
        font-weight: 500;
    }

    a:hover {
        color: #FCE834;
        background: #2c3e50;
        padding: 0.2rem 0.4rem;
        border-radius: 4px;
        text-decoration: none;
    }

    .practice-links {
        background: #f5f5f5;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }

    .practice-links h3 {
        margin-top: 0;
        color: #2c3e50;
    }
    </style>
    """

def convert_md_links_to_html(content):
    """Convert markdown file links to HTML file links."""
    # Convert .md links to .html, but preserve external links and colab links
    def replace_link(match):
        full_match = match.group(0)
        link_url = match.group(1) if match.group(1) else match.group(2)
        
        # Skip external links (http, https, colab)
        if link_url.startswith(('http://', 'https://', 'mailto:')):
            return full_match
        
        # Skip video files and other non-markdown files
        if not link_url.endswith('.md'):
            return full_match
        
        # Convert .md to .html
        new_link = link_url.replace('.md', '.html')
        return full_match.replace(link_url, new_link)
    
    # Pattern to match markdown links: [text](url) and <url>
    content = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', replace_link, content)
    content = re.sub(r'<([^>]+\.md)>', replace_link, content)
    
    return content

def create_navigation(current_file_path, root_path):
    """Create navigation breadcrumbs for the current page."""
    relative_path = os.path.relpath(current_file_path, root_path)
    path_parts = relative_path.split(os.sep)[:-1]  # Remove filename
    
    # Build breadcrumb navigation
    nav_links = ['<a href="../index.html">🏠 Home</a>']
    
    current_path = ".."
    for i, part in enumerate(path_parts):
        if part == "Lecture_Notes":
            nav_links.append(f'<a href="{current_path}/Lecture_Notes/index.html">📚 Lecture Notes</a>')
        elif part == "Assignments":
            nav_links.append(f'<a href="{current_path}/Assignments/index.html">📝 Assignments</a>')
        elif part == "Coding":
            nav_links.append(f'<a href="{current_path}/Coding/index.html">💻 Coding</a>')
        
        if i < len(path_parts) - 1:
            current_path += "/.."
    
    return f'<div class="nav-breadcrumb">{"".join(nav_links)}</div>'

def convert_markdown_to_html(md_file_path, root_path):
    """Convert a single markdown file to HTML."""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove YAML frontmatter if present
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2].strip()
    
    # Convert markdown links to HTML links
    content = convert_md_links_to_html(content)
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
    html_content = md.convert(content)
    
    # Create navigation
    navigation = create_navigation(md_file_path, root_path)
    
    # Get the title from the first h1 or use filename
    title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', html_content)
    if title_match:
        title = title_match.group(1)
    else:
        title = os.path.splitext(os.path.basename(md_file_path))[0]
    
    # Create complete HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Python Course</title>
    {get_base_css()}
</head>
<body>
    {navigation}
    <div class="content">
        {html_content}
    </div>
    
    <hr style="border: none; border-top: 3px solid #FCE834; margin: 3rem 0;">
    <p style="text-align: center; color: #2c3e50; font-style: italic;">
        <strong>Happy Learning! 🐍✨</strong>
    </p>
</body>
</html>"""
    
    # Write HTML file
    html_file_path = md_file_path.replace('.md', '.html')
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Converted: {md_file_path} -> {html_file_path}")

def create_index_files():
    """Create index.html files for directories that need them."""
    
    # Lecture Notes index
    lecture_notes_index = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture Notes - Python Course</title>
    """ + get_base_css() + """
</head>
<body>
    <div class="nav-breadcrumb">
        <a href="../index.html">🏠 Home</a>
    </div>
    
    <div class="header">
        <h1>📚 Lecture Notes</h1>
        <p>Comprehensive guides and documentation for each module</p>
    </div>
    
    <h2>Available Lecture Notes</h2>
    <ul>
        <li><a href="Python01-py101.html">🐍 Python 101 - Programming Basics</a></li>
        <li><a href="Python02-arrays.html">📊 Python Arrays - Lists and Data Structures</a></li>
        <li><a href="Python03-Pandas.html">🐼 Pandas - Data Manipulation</a></li>
        <li><a href="Python04-Plotting.html">📈 Data Visualization - Plotting</a></li>
        <li><a href="Git01-101.html">📋 Git 101 - Version Control</a></li>
        <li><a href="PythonE-Numpy.html">🔢 NumPy - Numerical Computing</a></li>
        <li><a href="PythonE-Datascience.html">🧪 Data Science</a></li>
        <li><a href="PythonE-GUI.html">🖼️ GUI Development</a></li>
        <li><a href="PythonE-Path and Filehandling.html">📁 File and Path Handling</a></li>
    </ul>
    
    <hr style="border: none; border-top: 3px solid #FCE834; margin: 3rem 0;">
    <p style="text-align: center; color: #2c3e50; font-style: italic;">
        <strong>Happy Learning! 🐍✨</strong>
    </p>
</body>
</html>"""
    
    # Assignments index
    assignments_index = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignments - Python Course</title>
    """ + get_base_css() + """
</head>
<body>
    <div class="nav-breadcrumb">
        <a href="../index.html">🏠 Home</a>
    </div>
    
    <div class="header">
        <h1>📝 Assignments</h1>
        <p>Practice problems and exercises to reinforce your learning</p>
    </div>
    
    <h2>Available Assignments</h2>
    <ul>
        <li><strong><a href="Py01-Assignments.html">Assignment 1: Python Basics</a></strong> - Variables, functions, and control flow</li>
        <li><strong><a href="Py02-Assignments.html">Assignment 2: Arrays</a></strong> - List operations and array manipulation</li>
        <li><strong><a href="Py03-Assignments.html">Assignment 3: Pandas</a></strong> - Data analysis with Pandas</li>
        <li><strong><a href="Py04-Assignments.html">Assignment 4: Visualization</a></strong> - Creating meaningful visualizations</li>
    </ul>
    
    <div class="practice-links">
        <h3>🎮 Interactive Practice</h3>
        <p>Work through the assignments in Google Colab:</p>
        <a href="https://colab.research.google.com/github/stawiskm/pythoncourse/blob/student/Assignments/Py02-Assignments.ipynb" class="btn btn-colab">📓 Assignment 2 Notebook</a>
        <a href="https://colab.research.google.com/github/stawiskm/pythoncourse/blob/student/Assignments/Py03-Assignments.ipynb" class="btn btn-colab">📓 Assignment 3 Notebook</a>
        <a href="https://colab.research.google.com/github/stawiskm/pythoncourse/blob/student/Assignments/Py04-Assignments.ipynb" class="btn btn-colab">📓 Assignment 4 Notebook</a>
    </div>
    
    <hr style="border: none; border-top: 3px solid #FCE834; margin: 3rem 0;">
    <p style="text-align: center; color: #2c3e50; font-style: italic;">
        <strong>Happy Learning! 🐍✨</strong>
    </p>
</body>
</html>"""
    
    # Write index files
    with open('Lecture_Notes/index.html', 'w', encoding='utf-8') as f:
        f.write(lecture_notes_index)
    
    with open('Assignments/index.html', 'w', encoding='utf-8') as f:
        f.write(assignments_index)
    
    print("Created index files for Lecture_Notes and Assignments")

def main():
    """Main function to convert all markdown files to HTML."""
    root_path = os.getcwd()
    
    # Find all markdown files
    md_files = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith('.md') and file not in ['README.md', 'readme.md']:
                md_files.append(os.path.join(root, file))
    
    print(f"Found {len(md_files)} markdown files to convert:")
    for md_file in md_files:
        print(f"  - {md_file}")
    
    # Convert all markdown files to HTML
    for md_file in md_files:
        convert_markdown_to_html(md_file, root_path)
    
    # Create index files for directories
    create_index_files()
    
    print(f"\\nConversion complete! Converted {len(md_files)} files to HTML.")
    print("\\nNext steps:")
    print("1. Update the main index.html to link to .html files instead of .md")
    print("2. Test all links and navigation")
    print("3. Optional: Remove .md files if no longer needed")

if __name__ == "__main__":
    main()