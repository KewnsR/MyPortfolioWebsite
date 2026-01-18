# Lloyd Kenneth Ramos - Portfolio Website 🚀

A modern, minimalist single-page portfolio website built with Flask and Tailwind CSS, featuring elegant design, smooth animations, and clean typography.

![Portfolio Preview](https://img.shields.io/badge/Status-Live-brightgreen) ![Flask](https://img.shields.io/badge/Flask-3.1.0-blue) ![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Latest-38B2AC) ![Python](https://img.shields.io/badge/Python-3.x-yellow)

## ✨ Features

- **Minimalist Design**: Clean, elegant UI with purple gradient accents
- **Single-Page Architecture**: Smooth scrolling between sections with anchor navigation
- **Responsive Layout**: Fully responsive design that works seamlessly on all devices
- **Smooth Animations**: Custom reveal animations using Intersection Observer API
- **Interactive Elements**: Hover effects, smooth transitions, and dynamic navigation
- **Performance Optimized**: Fast loading with efficient code structure
- **Professional Presentation**: Perfect for OJT/Internship applications

## 🛠️ Tech Stack

### Backend
- **Flask 3.1.0** - Python web framework
- **Python 3.x** - Server-side programming

### Frontend
- **HTML5** - Semantic markup structure
- **Tailwind CSS (CDN)** - Utility-first CSS framework
- **Custom CSS** - Minimalist card design, gradient effects, reveal animations
- **Vanilla JavaScript** - Intersection Observer API, smooth scrolling, mobile menu

### Fonts
- **Space Grotesk** - Headings and display text
- **Inter** - Body text and paragraphs

## 📁 Project Structure

```
MyPortfolioWebsite/
│
├── app.py                 # Flask application main file
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment configuration
├── package.json          # Node.js dependencies
├── tailwind.config.js    # Tailwind configuration
│
├── api/
│   └── index.py          # Vercel API endpoint
│
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Custom styles (gradient text, cards, animations)
│   ├── img/
│   │   └── 1v1formal.png # Profile image
│   └── js/
│       └── scroll-animations.js
│
└── templates/            # HTML templates
    └── index.html        # Single-page portfolio
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/KewnsR/MyPortfolioWebsite.git
   cd MyPortfolioWebsite
   ```

2. **Set up Python virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000` to view the website

## 🎨 Portfolio Sections

### Home
- Professional profile image
- Name and title
- Brief introduction
- Call-to-action buttons

### About
- Personal biography (3 paragraphs)
- Statistics cards (Years Coding, Projects Built, Technologies, GPA)

### Education
- Taguig City University
- Bachelor of Science in Computer Science
- 2022 - Expected July 2026

### Skills & Expertise
- **Frontend Development**: HTML/CSS, JavaScript, React, Tailwind CSS
- **Backend Development**: Python, Django, Flask, SQL, PostgreSQL
- **Tools & Technologies**: Git, VS Code, Figma, Docker, AI/ML

### Projects
- **AI Scholarship Evaluation System (TCU-CEAA)**: AI-driven scholarship evaluation with OCR, NLP, and document verification
- **Graduate Survey Responses**: Interactive dashboard for alumni tracer data visualization

### Contact
- OJT/Internship opportunity section
- Email: ramoslloydkenneth1@gmail.com
- Location: Taguig City, Philippines
- Social links: GitHub, LinkedIn
- Contact form

## 🌟 Key Features Explained

### Animation System
- **Reveal Animations**: Intersection Observer triggers fade-in effects on scroll
- **Gradient Text**: Purple gradient accent on name
- **Card Hover Effects**: Smooth transitions and subtle elevation
- **Smooth Scrolling**: Native CSS smooth scrolling for anchor navigation

### Interactive Elements
- **Mobile Navigation**: Responsive hamburger menu with overlay
- **Active Section Highlighting**: Navigation links highlight based on scroll position
- **Smooth Transitions**: All interactive elements have fluid animations

### Design Principles
- **Minimalism**: Clean black background (#0a0a0a) with white text
- **Typography Hierarchy**: Clear heading sizes (6xl, 4xl, 3xl hierarchy)
- **Consistent Spacing**: Reduced spacing between sections (py-16, py-12)
- **Subtle Accents**: Purple gradient (#667eea to #764ba2) for emphasis
- **Rounded Corners**: Modern rounded-2xl and rounded-3xl borders

## 📱 Browser Support

- ✅ Chrome (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)
- ✅ Edge (Latest)
- ✅ Mobile browsers

## 🔧 Customization

### Updating Content

1. **Personal Information**: Edit `templates/index.html`
   - Update name, title, and description in Hero section
   - Modify About section biography
   - Update statistics cards with accurate numbers

2. **Projects**: Modify project cards in Projects section
   - Change project titles and descriptions
   - Update GitHub repository links
   - Swap technology tags

3. **Skills**: Edit Skills section
   - Add/remove technology tags
   - Update skill categories

4. **Contact Info**: Update Contact section
   - Change email address
   - Update location
   - Modify social media links

### Styling Customization

- **Colors**: Edit gradient colors in `static/css/style.css`
- **Fonts**: Change font families in `index.html` Google Fonts import
- **Spacing**: Adjust padding/margin using Tailwind utility classes
- **Image**: Replace `static/img/1v1formal.png` with your profile photo

## 🚀 Deployment

### Vercel (Recommended)
The project includes `vercel.json` configuration:
```bash
vercel --prod
```

### Local Development
```bash
python app.py
```

### Traditional Hosting
1. Use WSGI server like Gunicorn
2. Configure web server (Nginx/Apache)
3. Set up SSL certificate

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📞 Contact

- **Email**: ramoslloydkenneth1@gmail.com
- **LinkedIn**: [Lloyd Kenneth Ramos](https://www.linkedin.com/in/lloyd-kenneth-ramos-047a30379/)
- **GitHub**: [@KewnsR](https://github.com/KewnsR)
- **Location**: Taguig City, Philippines

## 🎓 About

Computer Science student at Taguig City University passionate about building digital solutions that blend functionality with clean, minimalist design. Currently seeking internship or OJT opportunities to apply technical skills and contribute through problem-solving and adaptability.

## 🙏 Acknowledgments

- Flask documentation and community
- Tailwind CSS for the utility-first framework
- Google Fonts (Space Grotesk & Inter)
- Intersection Observer API for scroll animations

---

**Built with ❤️ by Lloyd Kenneth Ramos**

*Last updated: January 2026*
