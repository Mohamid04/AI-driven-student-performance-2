# 🎓 AI-Driven Assessment of Student Performance Trends

A full-stack responsive web application that helps students track their academic performance and receive AI-generated feedback based on their marks.

## 📋 Features

### Student Features
- **Email-based Authentication**: Secure signup and login system
- **Performance Dashboard**: View subject-wise marks (Maths, Science, English)
- **Performance Metrics**:
  - Total marks out of 300
  - Student rank among all students
  - Percentile ranking
- **AI-Generated Feedback**: Color-coded feedback based on performance
  - 🚀 Excellent (≥240 marks)
  - 💪 Good (≥180 marks)
  - 📘 Needs Improvement (<180 marks)

### Admin Features
- **CSV Upload**: Upload student data via CSV file
- **Data Management**: Update student records in bulk
- **Template Download**: Download CSV template for easy data entry

### Design Features
- **Fully Responsive**: Works seamlessly on desktop, tablet, and mobile
- **Modern UI**: Clean, gradient-based design with smooth animations
- **User-Friendly**: Intuitive navigation and clear information hierarchy

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask (Python)
- **CORS**: Flask-CORS for cross-origin requests
- **Data Storage**: CSV-based (easily upgradeable to database)

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Responsive design with flexbox and grid
- **JavaScript**: Vanilla JS for interactivity (no dependencies)

## 📦 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone/Download the Project
```bash
# Navigate to the project directory
cd AI-Student-Performance
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Access the Application
Open your browser and navigate to:
```
http://localhost:5000
```

## 🚀 Usage Guide

### For Students

#### 1. **Login**
- Visit the login page
- Enter your email address
- Enter any password (demo mode)
- Click "Login"

**Demo Credentials:**
```
Email: arjun@gmail.com
Password: any password
```

Other demo accounts:
- meena@gmail.com
- ravi@gmail.com
- priya@gmail.com
- vikram@gmail.com

#### 2. **View Dashboard**
After login, you'll see:
- Your name and email
- Subject-wise marks (Maths, Science, English)
- Total marks and rank
- AI-generated feedback with color coding
- Your percentile ranking

#### 3. **Sign Up**
- Click "Sign up here" on the login page
- Enter your email and password (min 6 characters)
- Confirm your password
- Your account will be created (demo mode - no data stored)

### For Admins

#### 1. **Access Admin Panel**
- From the student dashboard, click "Admin Panel"
- Or navigate to: `http://localhost:5000/admin`

#### 2. **Upload CSV File**
- Click on the upload area or drag and drop a CSV file
- The CSV must follow this format:

```csv
student_id,name,email,maths,science,english,total
1,Arjun,arjun@gmail.com,85,75,90,250
2,Meena,meena@gmail.com,70,60,80,210
3,Ravi,ravi@gmail.com,50,40,60,150
```

#### 3. **Download Template**
- Click "Download Template CSV" to get a pre-formatted CSV file
- Fill in your student data
- Upload the file

## 📊 CSV Format

The CSV file must have the following columns:

| Column | Type | Description |
|--------|------|-------------|
| student_id | Integer | Unique student identifier |
| name | String | Student's full name |
| email | String | Student's email (used for login) |
| maths | Integer | Maths marks (0-100) |
| science | Integer | Science marks (0-100) |
| english | Integer | English marks (0-100) |
| total | Integer | Total marks (0-300) |

### Example CSV:
```csv
student_id,name,email,maths,science,english,total
1,Arjun,arjun@gmail.com,85,75,90,250
2,Meena,meena@gmail.com,70,60,80,210
3,Ravi,ravi@gmail.com,50,40,60,150
4,Priya,priya@gmail.com,92,88,95,275
5,Vikram,vikram@gmail.com,78,72,85,235
```

## 🤖 AI Feedback Logic

The feedback is generated based on total marks:

| Total Marks | Feedback | Color | Level |
|-------------|----------|-------|-------|
| ≥ 240 | Excellent! Keep it up 🚀 | Green (#28a745) | Excellent |
| 180-239 | Good work, but you can do even better 💪 | Yellow (#ffc107) | Good |
| < 180 | Needs improvement — focus on your weak areas 📘 | Red (#dc3545) | Needs Improvement |

## 📁 Project Structure

```
AI-Student-Performance/
├── app.py                 # Flask backend application
├── students.csv           # Student data (CSV format)
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    ├── login.html        # Login page
    ├── signup.html       # Signup page
    ├── dashboard.html    # Student dashboard
    └── admin.html        # Admin panel
```

## 🔐 Security Notes

### Current Implementation (Demo)
- Session-based authentication
- Email-based login (no password verification in demo)
- CORS enabled for development

### Production Recommendations
1. **Password Security**:
   - Implement proper password hashing (bcrypt, argon2)
   - Store hashed passwords in database
   - Add password strength validation

2. **Database**:
   - Replace CSV with proper database (PostgreSQL, MySQL)
   - Implement proper data validation and sanitization

3. **Authentication**:
   - Implement JWT tokens
   - Add refresh token mechanism
   - Implement rate limiting

4. **HTTPS**:
   - Use SSL/TLS certificates
   - Redirect HTTP to HTTPS

5. **Environment Variables**:
   - Store secret keys in environment variables
   - Use `.env` file for configuration

## 🎨 Responsive Design

The application is fully responsive and works on:
- **Desktop**: 1920px and above
- **Tablet**: 768px to 1919px
- **Mobile**: Below 768px

All components automatically adjust to screen size using CSS Grid and Flexbox.

## 🐛 Troubleshooting

### Issue: "Port 5000 already in use"
**Solution**: Change the port in `app.py`
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use 5001 instead
```

### Issue: "Module not found" error
**Solution**: Ensure all dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: CSV file not uploading
**Solution**: 
- Ensure the file is in CSV format
- Check that all required columns are present
- Verify file size is less than 10MB

### Issue: Login not working
**Solution**:
- Ensure `students.csv` exists in the project root
- Check that the email exists in the CSV file
- Verify the CSV format is correct

## 📝 API Endpoints

### Authentication
- `GET /` - Home page (redirects to login or dashboard)
- `GET /login` - Login page
- `POST /login` - Login API
- `GET /signup` - Signup page
- `POST /signup` - Signup API
- `GET /logout` - Logout

### Student
- `GET /dashboard` - Student dashboard
- `GET /api/student-data` - Get student performance data

### Admin
- `GET /admin` - Admin panel
- `POST /api/upload-csv` - Upload CSV file

### Health
- `GET /api/health` - Health check endpoint

## 🚀 Deployment

### Deploy to Heroku
1. Create a `Procfile`:
```
web: python app.py
```

2. Create a `runtime.txt`:
```
python-3.9.16
```

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Deploy to PythonAnywhere
1. Upload files to PythonAnywhere
2. Create a web app with Flask
3. Configure the WSGI file
4. Reload the web app

## 📚 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [HTML/CSS/JavaScript MDN Docs](https://developer.mozilla.org/)
- [CSV Format Specification](https://tools.ietf.org/html/rfc4180)

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a full-stack web development project demonstrating:
- Backend API development with Flask
- Frontend responsive design
- CSV data handling
- Session management
- RESTful API design

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the code comments
3. Check Flask documentation

## 🎯 Future Enhancements

- [ ] Database integration (PostgreSQL/MySQL)
- [ ] Advanced analytics and charts
- [ ] Email notifications
- [ ] Student progress tracking over time
- [ ] Teacher dashboard with class management
- [ ] Mobile app (React Native/Flutter)
- [ ] Advanced AI feedback with personalized recommendations
- [ ] Parent portal
- [ ] Attendance tracking
- [ ] Assignment management

---

**Happy Learning! 🎓**
