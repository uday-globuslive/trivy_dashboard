# Trivy Dashboard (Flask)

A simple Flask web application for uploading, storing, and visualizing Trivy vulnerability scan reports.

## Features
- Upload Trivy JSON reports via web interface
- View history of uploaded reports
- Visualize vulnerability counts by severity (bar chart)
- Simple, clean dashboard UI

## Project Structure
```
app.py                # Main Flask application
static/
  style.css           # CSS for dashboard styling
templates/
  dashboard.html      # Main dashboard HTML template
uploads/              # Directory for uploaded Trivy reports
```

## Getting Started

### 1. Install dependencies
```
pip install flask
```

### 2. Run the application
```
python app.py
```

### 3. Open in your browser
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the dashboard.

## Running on Linux with a Virtual Environment

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Access the dashboard from your browser:
   - On the same machine: http://127.0.0.1:5000/
   - On your local network: http://<your-linux-ip>:5000/

To find your Linux machine's IP address, run:
```bash
hostname -I
```

## Usage
- Use the upload form to add Trivy JSON reports.
- Uploaded reports are listed with their upload time.
- The dashboard displays a bar chart summarizing vulnerabilities by severity (CRITICAL, HIGH, MEDIUM, LOW, UNKNOWN).

## Notes
- Only JSON files are accepted for upload.
- Uploaded reports are stored in the `uploads/` directory.
- The dashboard uses Chart.js (via CDN) for data visualization.

## Customization
- You can extend the dashboard to show more detailed trends, per-report details, or additional charts as needed.

## License
MIT License
