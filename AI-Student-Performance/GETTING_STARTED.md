# 🚀 Getting Started Guide

Welcome to the **AI-Driven Assessment of Student Performance Trends** application!

This guide will help you get up and running in minutes.

## ⚡ 30-Second Quick Start

### Windows Users
```bash
# 1. Open Command Prompt in the project folder
# 2. Run:
run.bat
```

### Linux/Mac Users
```bash
# 1. Open Terminal in the project folder
# 2. Run:
chmod +x run.sh
./run.sh
```

### Manual Setup (All Platforms)
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
python app.py

# 3. Open browser
# Visit: http://localhost:5000
```

## 📋 System Requirements

- **Python**: 3.7 or higher
- **pip**: Python package manager
- **Browser**: Any modern browser (Chrome, Firefox, Safari, Edge)
- **RAM**: 512 MB minimum
- **Disk Space**: 100 MB

## ✅ Installation Steps

### Step 1: Verify Python Installation
```bash
python --version
# or
python3 --version
```

You should see: `Python 3.x.x`

If not, download Python from https://www.python.org/

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- Flask 2.3.3
- Flask-CORS 4.0.0
- Werkzeug 2.3.7

### Step 3: Run the Application
```bash
python app.py
```

You should see:
```
============================================================
AI-Driven Assessment of Student Performance Trends
============================================================
Starting Flask server...
Visit: http://localhost:5000
============================================================
```

### Step 4: Open in Browser
Visit: **http://localhost:5000**

## 🎯 First Time Usage

### 1. Login with Demo Account
- **Email**: arjun@gmail.com
- **Password**: any password
- Click "Login"

### 2. Explore the Dashboard
You'll see:
- Your name and email
- Subject-wise marks (Maths: 85, Science: 75, English: 90)
- Total marks: 250
- Your rank: 2 out of 10
- AI feedback: "Good work, but you can do even better 💪" (Yellow)

### 3. Try Other Demo Accounts
- meena@gmail.com
- ravi@gmail.com
- priya@gmail.com
- vikram@gmail.com
- aditya@gmail.com

### 4. Visit Admin Panel
- Click "Admin Panel" from dashboard
- Download CSV template
- Upload a new CSV file with student data

## 📱 Responsive Design

The app works on all devices:

### Desktop (1920px+)
- Full layout with all features
- Multi-column dashboard
- Optimal spacing

### Tablet (768px-1919px)
- Adjusted layout
- Touch-friendly buttons
- Responsive grid

### Mobile (< 768px)
- Single column layout
- Large touch targets
- Optimized for small screens

Try resizing your browser to see the responsive design!

## 🔑 Demo Credentials

| Email | Password | Marks | Rank | Feedback |
|-------|----------|-------|------|----------|
| arjun@gmail.com | any | 250 | 2 | Good 💪 |
| meena@gmail.com | any | 210 | 6 | Good 💪 |
| ravi@gmail.com | any | 150 | 10 | Needs Improvement 📘 |
| priya@gmail.com | any | 275 | 1 | Excellent 🚀 |
| vikram@gmail.com | any | 235 | 4 | Good 💪 |
| anjali@gmail.com | any | 190 | 8 | Good 💪 |
| rohan@gmail.com | any | 260 | 3 | Excellent 🚀 |
| neha@gmail.com | any | 215 | 7 | Good 💪 |
| aditya@gmail.com | any | 277 | 1 | Excellent 🚀 |
| divya@gmail.com | any | 175 | 9 | Needs Improvement 📘 |

## 🎨 Features to Explore

### Student Dashboard
1. **View Performance**
   - Subject-wise marks
   - Total marks
   - Your rank

2. **Get AI Feedback**
   - Color-coded feedback
   - Performance level
   - Percentile ranking

3. **Responsive Design**
   - Try on mobile
   - Try on tablet
   - Try on desktop

### Admin Panel
1. **Upload CSV**
   - Click upload area
   - Select CSV file
   - Click "Upload CSV"

2. **Download Template**
   - Click "Download Template CSV"
   - Fill in your data
   - Upload the file

## 📊 CSV Format

To upload student data, use this format:

```csv
student_id,name,email,maths,science,english,total
1,John Doe,john@example.com,85,75,90,250
2,Jane Smith,jane@example.com,92,88,95,275
```

**Required Columns**:
- student_id (unique number)
- name (student name)
- email (login email)
- maths (0-100)
- science (0-100)
- english (0-100)
- total (0-300)

## 🤖 AI Feedback Levels

The app generates feedback based on total marks:

| Marks | Feedback | Color | Level |
|-------|----------|-------|-------|
| ≥ 240 | Excellent! Keep it up 🚀 | Green | Excellent |
| 180-239 | Good work, but you can do even better 💪 | Yellow | Good |
| < 180 | Needs improvement — focus on your weak areas 📘 | Red | Needs Improvement |

## 🛑 Stopping the Server

Press **Ctrl+C** in the terminal to stop the Flask server.

## ❓ Troubleshooting

### Issue: "Port 5000 already in use"
**Solution**: Use a different port
```bash
# Edit app.py and change:
# app.run(debug=True, host='0.0.0.0', port=5000)
# to:
# app.run(debug=True, host='0.0.0.0', port=5001)
```

### Issue: "Module not found" error
**Solution**: Reinstall dependencies
```bash
pip install -r requirements.txt
```

### Issue: "Python not found"
**Solution**: Install Python from https://www.python.org/

### Issue: Login not working
**Solution**: 
- Ensure students.csv exists
- Check email is in the CSV file
- Verify CSV format is correct

### Issue: CSV upload fails
**Solution**:
- Ensure file is CSV format
- Check all required columns are present
- Verify file size < 10MB

## 📚 Documentation

- **README.md** - Complete documentation
- **QUICKSTART.md** - 3-minute setup
- **PROJECT_SUMMARY.md** - Project overview
- **INDEX.md** - File navigation
- **SETUP_VERIFICATION.md** - Verification checklist

## 🔐 Security Notes

### Current (Demo Mode)
- No password verification
- Session-based authentication
- CSV-based data storage

### For Production
- Implement password hashing
- Use database instead of CSV
- Add HTTPS/SSL
- Implement rate limiting
- Add audit logging

## 🚀 Next Steps

### 1. Explore the Code
- Open `app.py` to see backend logic
- Open `templates/` to see frontend code
- Read inline comments

### 2. Customize
- Change colors in CSS
- Add new features
- Modify feedback messages
- Add more subjects

### 3. Deploy
- Follow deployment guide in README.md
- Deploy to Heroku, AWS, or other platforms
- Set up custom domain

### 4. Extend
- Add database integration
- Add more analytics
- Add email notifications
- Add progress tracking

## 📞 Getting Help

### Documentation
1. Check README.md for detailed docs
2. Check QUICKSTART.md for quick setup
3. Check code comments for implementation details

### Common Issues
1. Check Troubleshooting section above
2. Check README.md Troubleshooting section
3. Check Flask documentation

### External Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Documentation](https://docs.python.org/)
- [MDN Web Docs](https://developer.mozilla.org/)

## 🎓 Learning Resources

This project teaches:
- Full-stack web development
- Backend API design
- Frontend responsive design
- CSV data handling
- Session management
- RESTful API principles
- Error handling
- User authentication

## 💡 Tips & Tricks

### Tip 1: Use Demo Accounts
Try different demo accounts to see different feedback levels.

### Tip 2: Test Responsive Design
Resize your browser to see how the app adapts to different screen sizes.

### Tip 3: Upload Custom Data
Use the admin panel to upload your own student data.

### Tip 4: Check Browser Console
Open browser developer tools (F12) to see any errors or logs.

### Tip 5: Read the Code
The code is well-commented. Read it to understand how it works.

## 🎉 You're Ready!

You now have a fully functional AI-powered student performance assessment system!

### What You Can Do:
✅ Login with student email
✅ View performance dashboard
✅ See AI-generated feedback
✅ Upload student data via CSV
✅ Check rank and percentile
✅ Use on mobile, tablet, desktop

### What's Next:
1. Explore all features
2. Try different demo accounts
3. Upload custom data
4. Customize the app
5. Deploy to production

---

## 📋 Quick Reference

| Task | Command |
|------|---------|
| Install dependencies | `pip install -r requirements.txt` |
| Run app | `python app.py` |
| Open browser | `http://localhost:5000` |
| Stop server | `Ctrl+C` |
| View logs | Check terminal output |
| Edit code | Open files in text editor |
| Upload CSV | Use admin panel |

## 🎯 Success Checklist

- [x] Python installed
- [x] Dependencies installed
- [x] App running
- [x] Browser opened
- [x] Logged in with demo account
- [x] Viewed dashboard
- [x] Explored features
- [x] Tested responsive design
- [x] Tried admin panel
- [x] Ready to customize

---

**Congratulations! You're all set! 🎓**

Enjoy exploring the AI Student Performance application!

For more information, see:
- **README.md** - Full documentation
- **QUICKSTART.md** - Quick setup
- **PROJECT_SUMMARY.md** - Project overview
