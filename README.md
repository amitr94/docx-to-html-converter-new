# DOCX to HTML Converter

A fully functional web application that converts Microsoft Word (.docx) documents to clean HTML with advanced formatting and interactive features.

## Features

### ✨ Core Functionality
- **DOCX to HTML Conversion**: Upload .docx files and convert them to clean, semantic HTML
- **H3 Heading Styles**: All headings are converted to h3 tags with beautiful blue underline styling
- **Read More/Read Less**: Dynamic content expansion for sections with more than 2 paragraphs
- **Responsive Design**: Modern, mobile-friendly interface with gradient backgrounds
- **File Upload**: Drag-and-drop style file upload with validation

### 🎨 Design Features
- Modern gradient background (purple to blue)
- Professional card-based layout with rounded corners and shadows
- Smooth hover effects and transitions
- Color-coded buttons with gradient backgrounds
- Clean typography using Segoe UI font family
- Mobile-responsive design

### 🔧 Technical Features
- Flask backend with CORS support
- Python-docx for document processing
- Automatic paragraph grouping for read more functionality
- Unique section IDs to prevent conflicts
- Error handling and user feedback
- File size limits (16MB max)

## Live Demo

The application is currently running at:
**https://5000-i4ojesqojgk6l9kp1euv9-9ea9520d.manusvm.computer**

## Installation & Setup

### Prerequisites
- Python 3.11+
- pip package manager

### Local Development

1. **Clone or extract the project files**
2. **Navigate to the project directory**
   ```bash
   cd docx-html-converter
   ```

3. **Activate the virtual environment**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies** (if needed)
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python src/main.py
   ```

6. **Access the application**
   Open your browser and go to `http://localhost:5000`

## Project Structure

```
docx-html-converter/
├── src/
│   ├── main.py                 # Flask application entry point
│   ├── routes/
│   │   ├── converter.py        # DOCX conversion API endpoints
│   │   └── user.py            # User management endpoints (template)
│   ├── models/
│   │   └── user.py            # Database models (template)
│   ├── static/
│   │   └── index.html         # Frontend interface
│   └── database/
│       └── app.db             # SQLite database
├── venv/                      # Python virtual environment
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## API Endpoints

### POST /api/convert
Converts a DOCX file to HTML format.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (DOCX file)

**Response:**
```json
{
  "success": true,
  "html_content": ["<h3>Heading</h3>", "<p>Paragraph</p>", ...],
  "filename": "document.docx"
}
```

### GET /api/health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "DOCX to HTML Converter"
}
```

## How It Works

### 1. File Upload
- Users can select .docx files using the file input
- File validation ensures only DOCX files are accepted
- File size is limited to 16MB for performance

### 2. Document Processing
- The backend uses python-docx to parse the DOCX file
- All headings are converted to h3 tags for consistent styling
- Paragraphs are grouped by sections for read more functionality

### 3. Read More/Read Less Logic
- Sections with 2 or fewer paragraphs are displayed in full
- Sections with more than 2 paragraphs show the first 2 by default
- Additional paragraphs are hidden behind a "Read More" button
- Each section gets a unique ID to prevent conflicts
- JavaScript handles the toggle functionality

### 4. Styling
- H3 headings have blue underlines with gradient accents
- Read More buttons have gradient backgrounds
- Smooth transitions for expand/collapse animations
- Responsive design adapts to different screen sizes

## Customization

### Styling
Edit the CSS in `src/static/index.html` to customize:
- Colors and gradients
- Typography and fonts
- Button styles
- Layout and spacing

### Functionality
Modify `src/routes/converter.py` to:
- Change paragraph grouping logic
- Adjust heading level conversion
- Add new processing features

### Frontend
Update `src/static/index.html` to:
- Add new UI elements
- Modify the upload interface
- Change the display format

## Dependencies

- **Flask**: Web framework
- **Flask-CORS**: Cross-origin resource sharing
- **python-docx**: DOCX file processing
- **lxml**: XML processing (required by python-docx)
- **Werkzeug**: WSGI utilities

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Security Features

- File type validation (DOCX only)
- File size limits
- CORS configuration
- Secure file handling with temporary files

## Performance

- Efficient document processing
- Minimal memory usage with temporary file cleanup
- Responsive UI with smooth animations
- Optimized for files up to 16MB

## Troubleshooting

### Common Issues

1. **Import Error with lxml**
   - Ensure lxml is properly installed: `pip install lxml`
   - On some systems, you may need: `pip install --upgrade lxml`

2. **File Upload Not Working**
   - Check file size (must be under 16MB)
   - Ensure file has .docx extension
   - Verify CORS is enabled

3. **Read More Not Working**
   - Check browser console for JavaScript errors
   - Ensure unique section IDs are generated

### Development Tips

- Use the browser's developer tools to debug JavaScript
- Check the Flask console for backend errors
- Test with various DOCX file formats
- Verify responsive design on different screen sizes

## License

This project is provided as-is for educational and development purposes.

## Support

For issues or questions, please refer to the code comments and this documentation.

