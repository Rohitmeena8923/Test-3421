from datetime import datetime
from pathlib import Path

def get_mock_test_html():
    html = f"""
    <html>
    <head><title>Mock Test</title></head>
    <body>
        <h1>Mock Test - GK & Current Affairs</h1>
        <p><strong>Timer:</strong> 30:00 (Simulated Testbook Timer)</p>
        <ol>
            <li>Which is the capital of France?<br> A) Paris B) Berlin C) Rome D) Madrid</li>
            <li>Who is the current PM of India?<br> A) Modi B) Gandhi C) Kejriwal D) Shah</li>
        </ol>
    </body>
    </html>
    """
    file = Path("mock_test.html")
    file.write_text(html)
    return str(file)

def get_analysis_html():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    html = f"""
    <html>
    <head><title>Mock Test Analysis</title></head>
    <body>
        <h1>Test Analysis</h1>
        <p><strong>Date:</strong> {now}</p>
        <ul>
            <li>Questions Attempted: 2</li>
            <li>Correct: 1</li>
            <li>Incorrect: 1</li>
            <li>Accuracy: 50%</li>
            <li>Time Taken: 10:25</li>
        </ul>
    </body>
    </html>
    """
    file = Path("analysis.html")
    file.write_text(html)
    return str(file)