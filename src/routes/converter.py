from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
import tempfile
from docx import Document
from docx.shared import Inches
import re

converter_bp = Blueprint('converter', __name__)

ALLOWED_EXTENSIONS = {'docx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_docx_to_html(docx_path):
    """Convert DOCX file to HTML with h3 headings and paragraph structure"""
    doc = Document(docx_path)
    html_content = []
    
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if not text:
            continue
            
        # Check if paragraph is a heading
        if paragraph.style.name.startswith('Heading'):
            # Convert all headings to h3 as requested
            html_content.append(f'<h3>{text}</h3>')
        else:
            # Regular paragraph
            html_content.append(f'<p>{text}</p>')
    
    # Group paragraphs for read more/less functionality
    grouped_content = group_paragraphs_for_readmore(html_content)
    
    return grouped_content

def group_paragraphs_for_readmore(html_content):
    """Group content to enable read more/less functionality"""
    grouped = []
    current_section = []
    paragraph_count = 0
    
    for item in html_content:
        if item.startswith('<h3>'):
            # If we have accumulated paragraphs, process them
            if current_section:
                grouped.extend(process_section_for_readmore(current_section))
                current_section = []
                paragraph_count = 0
            
            # Add the heading
            grouped.append(item)
        elif item.startswith('<p>'):
            current_section.append(item)
            paragraph_count += 1
    
    # Process the last section if it exists
    if current_section:
        grouped.extend(process_section_for_readmore(current_section))
    
    return grouped

def process_section_for_readmore(paragraphs):
    """Process a section of paragraphs to add read more/less functionality"""
    if len(paragraphs) < 2:
        # If less than 2 paragraphs, return as is
        return paragraphs
    
    # Show first 2 paragraphs by default, rest in read more
    visible_paragraphs = paragraphs[:2]
    hidden_paragraphs = paragraphs[2:]
    
    result = []
    
    # Add visible paragraphs
    for p in visible_paragraphs:
        result.append(p)
    
    if hidden_paragraphs:
        # Generate unique section ID based on timestamp and random number
        import time
        import random
        section_id = f"section_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"
        
        result.append(f'<div class="read-more-container">')
        result.append(f'<div class="hidden-content" id="hidden_{section_id}" style="display: none;">')
        
        for p in hidden_paragraphs:
            result.append(p)
        
        result.append('</div>')
        result.append(f'<button class="read-more-btn" onclick="toggleReadMore(\'{section_id}\')">Read More</button>')
        result.append('</div>')
    
    return result

@converter_bp.route('/convert', methods=['POST'])
def convert_file():
    """Handle DOCX file upload and conversion to HTML"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Only DOCX files are allowed'}), 400
    
    try:
        # Create temporary file to save uploaded DOCX
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as temp_file:
            file.save(temp_file.name)
            
            # Convert DOCX to HTML
            html_content = convert_docx_to_html(temp_file.name)
            
            # Clean up temporary file
            os.unlink(temp_file.name)
            
            return jsonify({
                'success': True,
                'html_content': html_content,
                'filename': secure_filename(file.filename)
            })
    
    except Exception as e:
        return jsonify({'error': f'Conversion failed: {str(e)}'}), 500

@converter_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'DOCX to HTML Converter'})

