#!/usr/bin/env python3
"""
Fix internal markdown links in HTML files to point to HTML files instead.
"""

import os
import re
import glob

def fix_internal_links_in_html(file_path):
    """Fix internal links in a single HTML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix local markdown links (not external URLs)
    def replace_md_link(match):
        href = match.group(1)
        
        # Skip external URLs
        if href.startswith(('http://', 'https://', 'mailto:', '#')):
            return match.group(0)
        
        # Skip video files and other non-markdown files  
        if not href.endswith('.md'):
            return match.group(0)
        
        # Convert .md to .html
        new_href = href.replace('.md', '.html')
        return f'href="{new_href}"'
    
    # Pattern to match href="something.md" but not external URLs
    content = re.sub(r'href="([^"]*\.md)"', replace_md_link, content)
    
    # Also fix plain markdown links in the content
    def replace_plain_md_link(match):
        full_link = match.group(0)
        link_text = match.group(1)
        link_url = match.group(2)
        
        # Skip external URLs
        if link_url.startswith(('http://', 'https://', 'mailto:', '#')):
            return full_link
        
        # Skip video files and other non-markdown files
        if not link_url.endswith('.md'):
            return full_link
        
        # Convert .md to .html
        new_url = link_url.replace('.md', '.html')
        return f'<a href="{new_url}">{link_text}</a>'
    
    # Pattern to match <a href="something.md">text</a>
    content = re.sub(r'<a href="([^"]*\.md)">([^<]*)</a>', replace_plain_md_link, content)
    
    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed links in: {file_path}")
        return True
    return False

def main():
    """Fix internal links in all HTML files."""
    html_files = glob.glob("**/*.html", recursive=True)
    
    # Skip the main index.html as it's already correct
    html_files = [f for f in html_files if not f.endswith('/index.html') and f != 'index.html']
    
    print(f"Found {len(html_files)} HTML files to process:")
    
    fixed_count = 0
    for html_file in html_files:
        if fix_internal_links_in_html(html_file):
            fixed_count += 1
    
    print(f"\\nProcessed {len(html_files)} files, fixed links in {fixed_count} files.")

if __name__ == "__main__":
    main()