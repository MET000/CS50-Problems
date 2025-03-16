---
# BrewCraft Studio: Menu Builder ☕

BrewCraft Studio is a web application designed to empower coffee shop owners to create, customize, and publish professional digital menus. Built with Flask and SQLite, the app offers intuitive tools for menu management, theme customization, and customer engagement while prioritizing security and usability. Whether you're crafting a vibrant “Colorful” menu for a trendy café or a sleek “Minimalistic” design for an upscale espresso bar, BrewCraft Studio streamlines the process of showcasing a coffee shop’s offerings.

---

## Features ✨

1. **User Authentication & Security**
   - **Secure Registration/Login:** Uses [`werkzeug.security`](https://werkzeug.palletsprojects.com/) for password hashing.
   - **Session Management:** Implements [`flask-session`](https://pythonhosted.org/Flask-Session/) for secure, server-side session storage.
   - **Input Validation:** Employs [`email-validator`](https://pypi.org/project/email-validator/) for emails and [`phonenumbers`](https://pypi.org/project/phonenumbers/) for phone numbers.

2. **Dynamic Menu Management**
   - **Add/Remove Items:** Organize menu items into 9 categories (e.g., "Espresso Bar", "Desserts").
   - **Price Management:** Input and display prices with consistent formatting.
   - **Real-Time Editing:** Provides instant updates to the menu during creation.

3. **Theme Customization**
   - **Three Unique Styles:**
     - **Colorful:** Bold colors and playful fonts for a lively vibe.
     - **Illustrational:** Soft pastels and hand-drawn aesthetics.
     - **Minimalistic:** Clean lines and monochromatic tones for modern elegance.
   - **Dynamic Previews:** Renders menus with theme-specific colors, fonts, and background images.

4. **Subscription & Contact Systems**
   - **Newsletter Subscription:** Allows coffee shop owners to subscribe for updates on new features and themes.
   - **Interactive Contact Form:** A dynamic form at `/contact` for inquiries or feedback, with validation ensuring email correctness and message completeness.

5. **Responsive Design**
   - Mobile-friendly templates ensure menus look great on all devices.

## File Structure & Key Components 📂

1. **app.py (Core Application)**
   - **Routes:** Handles all HTTP requests (e.g., `/login`, `/add`, `/menu`, `/contact`).
   - **Session Management:** Uses `flask-session` to track logged-in users.
   - **Database Interactions:** Utilizes SQLite alongside the [CS50 Library](https://cs50.readthedocs.io/libraries/cs50/) to simplify SQL queries.
   - **Security:** Validates inputs, hashes passwords, and sanitizes user data.

2. **helpers.py (Decorators)**
   - **@login_required:** Restricts access to authenticated users only. Redirects unauthorized users to `/login`.

3. **Templates (HTML)**
   - **layout.html:**
     - Serves as the base template inherited by all other pages to ensure consistent styling.
     - Includes a navigation bar, CSS/JS links, and dynamic content blocks (`{% block content %}`).
     - Dynamically displays login/logout links based on the user session.
   - **login.html / register.html:** Manage user authentication with real-time error feedback.
   - **add.html / remove.html:** Provide forms for managing menu items.
   - **menu.html:** Offers a style selection page with theme previews.
   - **display_menu.html:** Dynamically renders the final menu with the chosen styling.
   - **contact.html:** Collects user emails and messages, validates inputs, and submits data to the database.
   - **about.html:** A static page describing the web application.

4. **Static Files (CSS/Images)**
   - **styles.css:** Centralizes styling to maintain consistency across all pages.
   - **Theme Images:** Includes background images (e.g., `img_1.jpg`) tied to specific styles.

5. **Database (coffeeshops.db)**
   - **Tables:**
     - `users`: Stores coffee shop credentials and details.
     - `menu`: Tracks menu items linked to users via `user_id`.
     - `subscribers`/`contact`: Manages newsletter subscriptions and support inquiries.

## Design Choices & Debates 🤔

1. **Template Inheritance with layout.html**
   - **Rationale:** Centralizes shared HTML/CSS (e.g., navigation bars, headers) to avoid redundancy and ensure a consistent UI across all pages.
   - **Debate:** Although separate headers per page were considered, inheritance was chosen to simplify maintenance.

2. **Session Management Over Cookies**
   - **Rationale:** By using `flask-session` with server-side storage, session data remains secure and tamper-proof compared to Flask’s default signed cookies.

3. **Database Choice: SQLite**
   - **Rationale:** SQLite is lightweight, serverless, and ideal for small applications. It offers simplicity and ease of setup without the overhead of a full-fledged database server.

4. **Theme Implementation**
   - **Debate:** Full customization of colors/fonts was initially considered. Limiting choices to three cohesive themes ensures professional results and reduces decision fatigue.
   - **Compromise:** Themes include predefined fonts (e.g., `shrikhand-regular`) and color palettes, with plans for future expansion via CSS variables.

## Installation & Usage 🚀

1. **Prerequisites**
   - Python 3.8+
   - pip
   - SQLite

2. **Setup**
   ```bash
   # Clone the repository
   git clone https://github.com/MET000/brewcraft_studio.git
   cd brewcraft_studio

   # Install dependencies
   pip install -r requirements.txt

   # Set up the database
   sqlite3 coffeeshops.db < schema.sql

   # Run the application
   flask run
   ```

## Tech Stack 💻

| **Component** | **Tools Used**                                                |
|---------------|---------------------------------------------------------------|
| **Backend**   | Flask ([Documentation](https://flask.palletsprojects.com/))    |
| **Database**  | SQLite + [CS50 Library](https://cs50.readthedocs.io/libraries/cs50/) |
| **Security**  | Werkzeug Password Hashing ([Documentation](https://werkzeug.palletsprojects.com/)) |
| **Validation**| [email-validator](https://pypi.org/project/email-validator/), [phonenumbers](https://pypi.org/project/phonenumbers/) |
| **Frontend**  | HTML, CSS                                                     |

## Future Enhancements 🔮

- **User Uploads:** Allow custom theme images and fonts.
- **Menu Sharing:** Generate public URLs for published menus.
- **Analytics:** Track menu views and identify popular items.

## License 📄

BrewCraft Studio is open-source and available under the [MIT License](LICENSE).

---

## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Werkzeug Documentation](https://werkzeug.palletsprojects.com/)
- [Flask-Session Documentation](https://pythonhosted.org/Flask-Session/)
- [SQLite Official Documentation](https://www.sqlite.org/index.html)
- [CS50 Library Documentation](https://cs50.readthedocs.io/libraries/cs50/)
- [email-validator on PyPI](https://pypi.org/project/email-validator/)
- [phonenumbers on PyPI](https://pypi.org/project/phonenumbers/)

---

**Brew Your Brand:** Create a menu that reflects your coffee shop’s unique personality with BrewCraft Studio!

---
