# Ken Ramos - Portfolio Website 🚀

A modern, responsive portfolio website built with Flask and Tailwind CSS, featuring stunning animations and a cyberpunk-inspired design aesthetic.

![Portfolio Preview](https://img.shields.io/badge/Status-Live-brightgreen) ![Flask](https://img.shields.io/badge/Flask-3.1.0-blue) ![TailwindCSS](https://img.shields.io/badge/TailwindCSS-4.1.11-38B2AC) ![Python](https://img.shields.io/badge/Python-3.x-yellow)

## ✨ Features

- **Modern Design**: Cyberpunk-inspired UI with neon accents and glass morphism effects
- **Responsive Layout**: Fully responsive design that works on all devices
- **Smooth Animations**: Custom CSS animations including floating elements, morphing shapes, and gradient effects
- **Interactive Elements**: Hover effects, smooth scrolling, and dynamic navigation
- **Performance Optimized**: Fast loading with efficient code structure
- **SEO Friendly**: Proper meta tags and semantic HTML structure

## 🛠️ Tech Stack

### Backend
- **Flask 3.1.0** - Python web framework
- **Python** - Server-side programming

### Frontend
- **HTML5** - Markup structure
- **Tailwind CSS 4.1.11** - Utility-first CSS framework
- **Vanilla JavaScript** - Interactive functionality
- **Custom CSS** - Advanced animations and effects

### Fonts & Icons
- **JetBrains Mono** - Monospace font for code snippets
- **Inter** - Modern sans-serif font
- **Emoji Icons** - For visual elements and tech stack representation

## 📁 Project Structure

```
MyPortfolioWebsite/
│
├── app.py                 # Flask application main file
├── requirements.txt       # Python dependencies
├── package.json          # Node.js dependencies (Tailwind CSS)
├── tailwind.config.js    # Tailwind configuration
│
├── static/               # Static assets
│   ├── css/
│   │   ├── output.css    # Compiled Tailwind CSS
│   │   └── tailwind.css  # Tailwind source file
│   ├── img/
│   │   └── profile.jpg.placeholder
│   └── js/
│       └── particles.min.js
│
└── templates/            # HTML templates
    ├── base.html         # Base template
    ├── index.html        # Homepage
    ├── about.html        # About page
    ├── projects.html     # Projects showcase
    └── contact.html      # Contact page
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Node.js (for Tailwind CSS)
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

4. **Install Node.js dependencies**
   ```bash
   npm install
   ```

5. **Initialize Tailwind CSS (if needed)**
   ```bash
   npx tailwindcss init
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser**
   Navigate to `http://localhost:5000` to view the website

## 🎨 Customization

### Updating Personal Information

1. **Homepage Content**: Edit `templates/index.html` to update:
   - Name and title
   - Profile description
   - Skills and interests
   - Social links

2. **About Page**: Modify `templates/about.html` for:
   - Detailed biography
   - Education background
   - Work experience

3. **Projects**: Update `templates/projects.html` to showcase:
   - Portfolio projects
   - Technical achievements
   - GitHub repositories

4. **Contact Info**: Edit `templates/contact.html` for:
   - Contact form
   - Social media links
   - Professional information

### Styling Customization

- **Colors**: Modify the color scheme in the Tailwind config section of `index.html`
- **Animations**: Adjust CSS animations in the `<style>` section
- **Layout**: Update the grid system and spacing using Tailwind classes

## 🌟 Key Features Explained

### Animation System
- **Float Animation**: Smooth floating elements with rotation
- **Gradient Effects**: Dynamic gradient text and backgrounds
- **Morphing Shapes**: CSS-based shape morphing animations
- **Typing Effect**: Simulated typing animation for text

### Interactive Elements
- **Mobile Navigation**: Responsive hamburger menu
- **Smooth Scrolling**: Seamless navigation between sections
- **Hover Effects**: 3D transforms and glow effects
- **Intersection Observer**: Scroll-triggered animations

### Design Principles
- **Glass Morphism**: Translucent cards with backdrop blur
- **Neon Aesthetics**: Cyberpunk-inspired color palette
- **Typography**: Careful font pairing for readability
- **Responsive Design**: Mobile-first approach

## 📱 Browser Support

- ✅ Chrome (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)
- ✅ Edge (Latest)
- ✅ Mobile browsers

## 🔧 Development

### Adding New Pages

1. Create a new HTML template in `templates/`
2. Add a new route in `app.py`:
   ```python
   @app.route("/newpage")
   def newpage():
       return render_template("newpage.html")
   ```
3. Update navigation in all templates

### CSS Compilation

If you modify Tailwind styles:
```bash
npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --watch
```

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment Options

1. **Heroku**
   - Add `Procfile`: `web: python app.py`
   - Deploy via Git

2. **Vercel**
   - Install Vercel CLI
   - Run `vercel --prod`

3. **Traditional Hosting**
   - Use WSGI server like Gunicorn
   - Configure web server (Nginx/Apache)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📞 Contact

- **Portfolio**: [Your Website URL]
- **Email**: [your.email@example.com]
- **LinkedIn**: [Your LinkedIn Profile]
- **GitHub**: [@KewnsR](https://github.com/KewnsR)

## 🙏 Acknowledgments

- Flask documentation and community
- Tailwind CSS for the utility-first framework
- Google Fonts for typography
- Inspiration from modern web design trends

---

**Built with ❤️ by Ken Ramos**

*Last updated: August 2025*
