"""
AI-Driven Assessment of Student Performance Trends
Backend API using Flask
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_cors import CORS
import csv
import os
from datetime import datetime
import hashlib
from functools import wraps

app = Flask(__name__, template_folder='templates')
app.secret_key = 'your-secret-key-change-in-production'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
CORS(app)

# Configuration
APP_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(APP_DIR, 'students.csv')
UPLOAD_FOLDER = os.path.join(APP_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==================== Helper Functions ====================

def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_students_data():
    """Load student data from CSV file"""
    students = {}
    if not os.path.exists(CSV_FILE):
        return students
    
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row and 'email' in row:
                    activities = row.get('activities', '').split(';') if row.get('activities') else []
                    students[row['email'].lower()] = {
                        'student_id': row.get('student_id', ''),
                        'name': row.get('name', ''),
                        'email': row.get('email', ''),
                        'branch': row.get('branch', ''),
                        'roll_no': row.get('roll_no', ''),
                        'maths': int(row.get('maths', 0)),
                        'science': int(row.get('science', 0)),
                        'english': int(row.get('english', 0)),
                        'total': int(row.get('total', 0)),
                        'attendance': int(row.get('attendance', 0)),
                        'activities': activities,
                        'image_url': row.get('image_url', 'https://i.pravatar.cc/150?img=default')
                    }
    except Exception as e:
        print(f"Error loading CSV: {e}")
    
    return students

def calculate_rank(email, all_students):
    """Calculate rank based on total marks"""
    student_email = email.lower()
    if student_email not in all_students:
        return None
    
    student_total = all_students[student_email]['total']
    rank = 1
    
    for email_key, student in all_students.items():
        if student['total'] > student_total:
            rank += 1
    
    return rank

def generate_ai_feedback(total_marks):
    """Generate AI-based feedback based on total marks"""
    if total_marks >= 240:
        return {
            'message': 'Excellent! Keep it up 🚀',
            'color': '#28a745',
            'level': 'Excellent'
        }
    elif total_marks >= 180:
        return {
            'message': 'Good work, but you can do even better 💪',
            'color': '#ffc107',
            'level': 'Good'
        }
    else:
        return {
            'message': 'Needs improvement — focus on your weak areas 📘',
            'color': '#dc3545',
            'level': 'Needs Improvement'
        }

def login_required(f):
    """Decorator to check if user is logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ==================== Routes ====================

@app.route('/')
def index():
    """Home page - redirect to dashboard if logged in, else to login"""
    if 'user_email' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page and authentication"""
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email', '').lower()
        password = data.get('password', '')
        
        if not email or not password:
            return jsonify({'success': False, 'message': 'Email and password required'}), 400
        
        students = load_students_data()
        
        # Check if student exists (email-based login)
        if email in students:
            # For demo purposes, we accept any password
            # In production, implement proper password hashing and storage
            session['user_email'] = email
            session['user_name'] = students[email]['name']
            return jsonify({'success': True, 'message': 'Login successful'}), 200
        else:
            return jsonify({'success': False, 'message': 'Student not found. Please sign up first.'}), 401
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Signup page and registration"""
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email', '').lower()
        password = data.get('password', '')
        confirm_password = data.get('confirm_password', '')
        
        if not email or not password or not confirm_password:
            return jsonify({'success': False, 'message': 'All fields required'}), 400
        
        if password != confirm_password:
            return jsonify({'success': False, 'message': 'Passwords do not match'}), 400
        
        if len(password) < 6:
            return jsonify({'success': False, 'message': 'Password must be at least 6 characters'}), 400
        
        students = load_students_data()
        
        if email in students:
            return jsonify({'success': False, 'message': 'Email already registered'}), 400
        
        # For demo: auto-login after signup
        session['user_email'] = email
        session['user_name'] = email.split('@')[0]
        
        return jsonify({'success': True, 'message': 'Signup successful! Redirecting...'}), 200
    
    return render_template('signup.html')

@app.route('/dashboard')
@login_required
def dashboard():
    """Student dashboard"""
    return render_template('dashboard.html')

@app.route('/api/student-data')
@login_required
def get_student_data():
    """API endpoint to get student performance data"""
    email = session.get('user_email', '').lower()
    students = load_students_data()
    
    if email not in students:
        return jsonify({'success': False, 'message': 'Student data not found'}), 404
    
    student = students[email]
    rank = calculate_rank(email, students)
    feedback = generate_ai_feedback(student['total'])
    
    return jsonify({
        'success': True,
        'data': {
            'name': student['name'],
            'email': student['email'],
            'branch': student['branch'],
            'roll_no': student['roll_no'],
            'image_url': student['image_url'],
            'maths': student['maths'],
            'science': student['science'],
            'english': student['english'],
            'total': student['total'],
            'attendance': student['attendance'],
            'activities': student['activities'],
            'rank': rank,
            'total_students': len(students),
            'feedback': feedback
        }
    }), 200

@app.route('/admin')
def admin():
    """Admin page for CSV upload"""
    return render_template('admin.html')

@app.route('/api/upload-csv', methods=['POST'])
def upload_csv():
    """Handle CSV file upload for updating student data"""
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No file selected'}), 400
    
    if not file.filename.endswith('.csv'):
        return jsonify({'success': False, 'message': 'Only CSV files allowed'}), 400
    
    try:
        # Read and validate CSV
        stream = file.stream.read().decode('utf-8')
        lines = stream.split('\n')
        
        # Validate CSV structure
        if not lines or not lines[0]:
            return jsonify({'success': False, 'message': 'Empty CSV file'}), 400
        
        # Write to students.csv
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            f.write(stream)
        
        return jsonify({
            'success': True,
            'message': 'CSV uploaded successfully! Student data updated.'
        }), 200
    
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error processing file: {str(e)}'}), 500

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    return redirect(url_for('login'))

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'}), 200

@app.route('/api/session-check')
def session_check():
    """Check if user is logged in"""
    if 'user_email' in session:
        return jsonify({
            'logged_in': True,
            'email': session.get('user_email'),
            'name': session.get('user_name')
        }), 200
    else:
        return jsonify({'logged_in': False}), 401

# ==================== Error Handlers ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

# ==================== Main ====================

if __name__ == '__main__':
    print("=" * 60)
    print("AI-Driven Assessment of Student Performance Trends")
    print("=" * 60)
    print("Starting Flask server...")
    print("Visit: http://localhost:5000")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
