#!/usr/bin/env python3
"""
Clean up duplicated elements in HTML files.
"""

import os
import re
import glob

def cleanup_html_file(file_path):
    """Clean up duplicated navigation and footer elements."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove duplicate nav-breadcrumb divs (keep only the first one after <body>)
    # Pattern to match duplicate nav-breadcrumb after content div starts
    content = re.sub(
        r'(<div class="content">\s*)<div class="nav-breadcrumb">[^<]*(?:<a[^>]*>[^<]*</a>)*[^<]*</div>\s*<div class="content">',
        r'\1',
        content,
        flags=re.DOTALL
    )
    
    # Remove duplicate closing content divs and footers
    # Find the first footer and remove any subsequent ones
    footer_pattern = r'<hr style="border: none; border-top: 3px solid #FCE834; margin: 3rem 0;">\s*<p style="text-align: center; color: #2c3e50; font-style: italic;">\s*<strong>Happy Learning! 🐍✨</strong>\s*</p>'
    
    # Count footer occurrences
    footer_matches = list(re.finditer(footer_pattern, content, re.DOTALL))
    
    if len(footer_matches) > 1:
        # Keep only the first footer, remove the rest
        for i in range(len(footer_matches) - 1, 0, -1):  # Remove from last to first
            match = footer_matches[i]
            content = content[:match.start()] + content[match.end():]
    
    # Remove duplicate closing </div> tags before </body>
    # Count content divs and make sure we have matching closing tags
    content_div_count = content.count('<div class="content">')
    content_close_count = content.count('</div>')
    
    # Find the position before </body>
    body_end = content.rfind('</body>')
    if body_end > 0:
        # Count closing divs before body end
        content_before_body = content[:body_end]
        content_close_before_body = content_before_body.count('</div>')
        
        # If we have too many closing divs, remove the extras
        if content_close_before_body > content_div_count + 1:  # +1 for nav-breadcrumb
            # Remove extra closing div tags before the footer
            content = re.sub(r'\s*</div>\s*(<hr style="border: none)', r'\n    \1', content)
    
    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned up: {file_path}")
        return True
    return False

def main():
    """Clean up all HTML files."""
    html_files = glob.glob("**/*.html", recursive=True)
    
    # Skip the main index.html
    html_files = [f for f in html_files if not f.endswith('/index.html') and f != 'index.html']
    
    print(f"Found {len(html_files)} HTML files to clean up:")
    
    cleaned_count = 0
    for html_file in html_files:
        if cleanup_html_file(html_file):
            cleaned_count += 1
    
    print(f"\\nProcessed {len(html_files)} files, cleaned up {cleaned_count} files.")

if __name__ == "__main__":
    main()