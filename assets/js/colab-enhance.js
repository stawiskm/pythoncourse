// Enhanced Colab Link Functionality
document.addEventListener('DOMContentLoaded', function() {
    
    // Add Colab badges to all Colab links
    document.querySelectorAll('a[href*="colab.research.google.com"]').forEach(function(link) {
        // Create Colab icon
        const icon = document.createElement('img');
        icon.src = 'https://colab.research.google.com/assets/colab-badge.svg';
        icon.alt = 'Open In Colab';
        icon.style.height = '20px';
        icon.style.marginRight = '5px';
        icon.style.verticalAlign = 'middle';
        
        // Insert icon at the beginning of the link
        link.insertBefore(icon, link.firstChild);
        
        // Add tracking (if analytics is available)
        link.addEventListener('click', function() {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'click', {
                    event_category: 'Colab',
                    event_label: this.href,
                    transport_type: 'beacon'
                });
            }
        });
    });

    // Add video icons to video links
    document.querySelectorAll('a[href$=".mp4"]').forEach(function(link) {
        const icon = document.createElement('span');
        icon.innerHTML = '🎥 ';
        icon.style.marginRight = '5px';
        link.insertBefore(icon, link.firstChild);
        
        // Add video tracking
        link.addEventListener('click', function() {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'click', {
                    event_category: 'Video',
                    event_label: this.href,
                    transport_type: 'beacon'
                });
            }
        });
    });

    // Enhanced table responsiveness
    document.querySelectorAll('table').forEach(function(table) {
        const wrapper = document.createElement('div');
        wrapper.style.overflowX = 'auto';
        wrapper.style.marginBottom = '1rem';
        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(table);
    });

    // Add difficulty badges
    document.querySelectorAll('a').forEach(function(link) {
        const href = link.getAttribute('href');
        if (href && href.includes('Level%200')) {
            link.classList.add('difficulty-beginner');
        } else if (href && href.includes('Level%201')) {
            link.classList.add('difficulty-easy');
        } else if (href && href.includes('Level%202')) {
            link.classList.add('difficulty-medium');
        } else if (href && href.includes('Level%203')) {
            link.classList.add('difficulty-hard');
        }
    });

    // Progress persistence for checkboxes
    const pageId = window.location.pathname;
    document.querySelectorAll('input[type="checkbox"]').forEach(function(checkbox, index) {
        const checkboxId = pageId + '_checkbox_' + index;
        
        // Restore saved state
        const saved = localStorage.getItem(checkboxId);
        if (saved === 'true') {
            checkbox.checked = true;
        }
        
        // Save state on change
        checkbox.addEventListener('change', function() {
            localStorage.setItem(checkboxId, this.checked);
            
            // Track progress
            const total = document.querySelectorAll('input[type="checkbox"]').length;
            const checked = document.querySelectorAll('input[type="checkbox"]:checked').length;
            const progress = Math.round((checked / total) * 100);
            
            if (typeof gtag !== 'undefined') {
                gtag('event', 'progress', {
                    event_category: 'Learning',
                    value: progress,
                    custom_parameter: pageId
                });
            }
        });
    });

    // Add copy buttons to code blocks
    document.querySelectorAll('pre code').forEach(function(codeBlock) {
        const pre = codeBlock.parentElement;
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.innerHTML = '📋 Copy';
        button.style.cssText = `
            position: absolute;
            top: 8px;
            right: 8px;
            background: var(--primary-yellow);
            border: none;
            padding: 4px 8px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
            color: var(--dark-blue);
            font-weight: 600;
            z-index: 1;
            opacity: 0.8;
            transition: opacity 0.3s ease;
        `;
        
        pre.style.position = 'relative';
        pre.appendChild(button);
        
        button.addEventListener('mouseenter', function() {
            this.style.opacity = '1';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.opacity = '0.8';
        });
        
        button.addEventListener('click', function() {
            const text = codeBlock.textContent;
            navigator.clipboard.writeText(text).then(function() {
                button.innerHTML = '✅ Copied!';
                setTimeout(function() {
                    button.innerHTML = '📋 Copy';
                }, 2000);
            }).catch(function() {
                // Fallback for older browsers
                const textArea = document.createElement('textarea');
                textArea.value = text;
                document.body.appendChild(textArea);
                textArea.select();
                try {
                    document.execCommand('copy');
                    button.innerHTML = '✅ Copied!';
                    setTimeout(function() {
                        button.innerHTML = '📋 Copy';
                    }, 2000);
                } catch (err) {
                    console.error('Copy failed:', err);
                }
                document.body.removeChild(textArea);
            });
        });
    });
});