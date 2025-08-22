#!/usr/bin/env python3
"""
Fix styling in all HTML files to ensure consistent appearance.
This script ensures all HTML files have the complete CSS styling.
"""

import os
import re
import glob

def get_complete_css():
    """Get the complete CSS styling for all HTML files."""
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

    .nav-links {
        background: #f5f5f5;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        text-align: center;
    }

    .nav-links a {
        display: inline-block;
        margin: 0.5rem;
        padding: 0.7rem 1.2rem;
        background: #FCE834;
        color: #2c3e50;
        text-decoration: none;
        border-radius: 6px;
        font-weight: 600;
    }

    .nav-links a:hover {
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

    .module-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1.5rem 0;
        background: #fff;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    .module-table th {
        background: linear-gradient(135deg, #FCE834 0%, #f9e71e 100%);
        color: #2c3e50;
        padding: 1rem;
        text-align: left;
        font-weight: 600;
    }

    .module-table td {
        padding: 1rem;
        border-bottom: 1px solid #f5f5f5;
        vertical-align: top;
    }

    .module-table tr:hover {
        background-color: rgba(252, 232, 52, 0.1);
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
        color: #2c3e50;
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

    .level-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }

    .level-card {
        background: #fff;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }

    .level-card:hover {
        transform: translateY(-5px);
    }

    .level-beginner {
        border-left: 5px solid #28a745;
    }

    .level-easy {
        border-left: 5px solid #FCE834;
    }

    .level-medium {
        border-left: 5px solid #fd7e14;
    }

    .level-hard {
        border-left: 5px solid #dc3545;
    }

    .card-title {
        color: #2c3e50;
        margin-bottom: 1rem;
        font-size: 1.2rem;
        font-weight: 600;
    }

    .card-content {
        margin-bottom: 1rem;
    }

    .file-list {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }

    .file-list ul {
        margin: 0;
        padding-left: 1.5rem;
    }

    .file-list li {
        margin: 0.3rem 0;
        font-family: monospace;
        font-size: 0.9rem;
    }
    </style>
    """

def fix_html_file_styling(file_path):
    """Fix styling in a single HTML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if this file already has our complete styling
    if 'nav-breadcrumb' in content and 'module-table' in content and 'level-grid' in content:
        print(f"Styling already complete: {file_path}")
        return False
    
    # Extract existing content between <body> and </body>
    body_match = re.search(r'<body[^>]*>(.*)</body>', content, re.DOTALL)
    if not body_match:
        print(f"No body content found: {file_path}")
        return False
    
    body_content = body_match.group(1)
    
    # Extract title from existing content
    title_match = re.search(r'<title>([^<]+)</title>', content)
    title = title_match.group(1) if title_match else "Python Course"
    
    # Get relative path to determine navigation
    relative_path = os.path.relpath(file_path, os.getcwd())
    path_parts = relative_path.split(os.sep)[:-1]  # Remove filename
    
    # Build navigation based on location
    nav_links = ['<a href="../index.html">🏠 Home</a>']
    if 'Lecture_Notes' in path_parts:
        nav_links.append('<a href="index.html">📚 Lecture Notes</a>')
    elif 'Assignments' in path_parts:
        nav_links.append('<a href="index.html">📝 Assignments</a>')
    elif 'Coding' in path_parts:
        nav_links.append('<a href="index.html">💻 Coding</a>')
    
    navigation = f'<div class="nav-breadcrumb">{"".join(nav_links)}</div>'
    
    # Create complete HTML with proper styling
    complete_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {get_complete_css()}
</head>
<body>
    {navigation}
    <div class="content">
        {body_content.strip()}
    </div>
    
    <hr style="border: none; border-top: 3px solid #FCE834; margin: 3rem 0;">
    <p style="text-align: center; color: #2c3e50; font-style: italic;">
        <strong>Happy Learning! 🐍✨</strong>
    </p>
</body>
</html>"""
    
    # Write the updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(complete_html)
    
    print(f"Fixed styling: {file_path}")
    return True

def main():
    """Fix styling in all HTML files that need it."""
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html') and file != 'index.html':  # Skip main index
                html_files.append(os.path.join(root, file))
    
    print(f"Found {len(html_files)} HTML files to check:")
    
    fixed_count = 0
    for html_file in html_files:
        if fix_html_file_styling(html_file):
            fixed_count += 1
    
    print(f"\\nProcessed {len(html_files)} files, fixed styling in {fixed_count} files.")

if __name__ == "__main__":
    main()