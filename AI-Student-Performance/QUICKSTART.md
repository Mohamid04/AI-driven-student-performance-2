# ⚡ Quick Start Guide

Get the AI Student Performance application running in 3 minutes!

## 🚀 Quick Setup

### 1. Install Dependencies (1 minute)
```bash
pip install -r requirements.txt
```

### 2. Run the Application (30 seconds)
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

### 3. Open in Browser (30 seconds)
Visit: **http://localhost:5000**

## 🎯 Try It Out

### Login with Demo Account
1. Click on the login page
2. Enter email: **arjun@gmail.com**
3. Enter password: **any password**
4. Click "Login"

### View Dashboard
You'll see:
- ✅ Student name and email
- ✅ Subject-wise marks (Maths, Science, English)
- ✅ Total marks and rank
- ✅ AI-generated feedback (color-coded)
- ✅ Percentile ranking

### Try Other Demo Accounts
- meena@gmail.com
- ravi@gmail.com
- priya@gmail.com
- vikram@gmail.com
- aditya@gmail.com

## 📤 Upload New Student Data

1. Click "Admin Panel" from dashboard
2. Download the CSV template
3. Fill in your student data
4. Upload the CSV file
5. Student data will be updated instantly

## 📱 Responsive Design

The app works perfectly on:
- 🖥️ Desktop (1920px+)
- 📱 Tablet (768px-1919px)
- 📱 Mobile (below 768px)

Try resizing your browser to see the responsive layout!

## 🔑 Demo Credentials

| Email | Password | Marks | Rank |
|-------|----------|-------|------|
| arjun@gmail.com | any | 250 | 2 |
| meena@gmail.com | any | 210 | 6 |
| ravi@gmail.com | any | 150 | 10 |
| priya@gmail.com | any | 275 | 1 |
| vikram@gmail.com | any | 235 | 4 |
| anjali@gmail.com | any | 190 | 8 |
| rohan@gmail.com | any | 260 | 3 |
| neha@gmail.com | any | 215 | 7 |
| aditya@gmail.com | any | 277 | 1 |
| divya@gmail.com | any | 175 | 9 |

## 🎨 Features to Explore

### Student Dashboard
- View your performance metrics
- See subject-wise breakdown
- Get AI-generated feedback
- Check your rank and percentile

### Admin Panel
- Upload CSV files with student data
- Download CSV template
- Update student records in bulk

### Responsive Design
- Try on mobile, tablet, and desktop
- All features work on all screen sizes
- Smooth animations and transitions

## 🛑 Stop the Server

Press `Ctrl+C` in the terminal to stop the Flask server.

## 📚 Next Steps

1. **Explore the Code**: Check `app.py` for backend logic
2. **Customize**: Edit templates in `templates/` folder
3. **Add Features**: Extend the application with new features
4. **Deploy**: Follow deployment guide in README.md

## ❓ Troubleshooting

### Port 5000 already in use?
```bash
# Use a different port
# Edit app.py and change port=5000 to port=5001
python app.py
```

### Module not found?
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### CSV upload not working?
- Ensure file is in CSV format
- Check all required columns are present
- File size should be less than 10MB

## 📖 Full Documentation

See `README.md` for complete documentation including:
- Detailed feature list
- API endpoints
- CSV format specification
- Production deployment guide
- Security recommendations

---

**Enjoy exploring the AI Student Performance application! 🎓**
