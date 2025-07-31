# Roommate_Dekho

**Find. Match. Thrive.**  
Roommate_Dekho is your one-stop Flask application that helps you discover and connect with ideal roommates based on **location**, **budget**, **lifestyle**, and **interests**—all powered by MongoDB, geospatial lookup, FAISS similarity, and TF-IDF matching.

---

## 🚀 Key Features

- **📍 Location-Aware Matching**  
  Uses `KDTree` to instantly find all potential roommates within a configurable radius (default 10 km).

- **💰 Budget Normalization**  
  Standardizes budgets via `StandardScaler` so you compare apples-to-apples.

- **🎯 Interest & Lifestyle Matching**  
  - **Hobbies**: TF-IDF on user-entered hobbies  
  - **Diet**: Vegetarian flag  
  - **Overall Similarity**: Combined into a FAISS L2 index for lightning-fast neighbor search

- **🗺️ Geo-Lookup**  
  Reverse-geocoding via **Geopy/Nominatim** to show real addresses, not just lat/long.

- **📷 Image Upload & Display**  
  Securely upload profile pics (PNG/JPG/GIF) and display them in results.

- **☁️ MongoDB Atlas Backend**  
  Scalable storage with a simple `inserter.py` wrapper.

- **⚡️ Lightning Fast**  
  All heavy lifting (KDTree + FAISS) runs in-memory—searches return in milliseconds.

---

## 🛠️ Tech Stack

- **Backend Framework**: Flask  
- **Database**: MongoDB Atlas (via `pymongo`)  
- **Geo & Distance**: Geopy, SciPy KDTree  
- **ML & Similarity**: scikit-learn, FAISS, NumPy, pandas  
- **Templates**: Jinja2 (`templates/form.html`, `templates/return.html`)  
- **Static Assets**: `images/` for profile uploads  
- **Utilities**: `werkzeug.utils.secure_filename` for safe file handling

---

## 📁 Project Structure

Roommate_Dekho/
├─ images/ # Uploaded profile images
├─ templates/
│ ├─ form.html # Input form for new user
│ └─ return.html # Results page
├─ pycache/ # Auto-generated
├─ example.py # Geo-helper: distance + reverse lookup
├─ inserter.py # MongoDB connection & collection setup
├─ nearloc.py # KDTree location-based neighbor finder
├─ matching.py # FAISS + TF-IDF + scaler matching logic
├─ mainfile.py # Flask app: endpoints & flow
├─ requirements.txt # pip install -r
└─ .gitignore


---

## ⚙️ Prerequisites

- **Python 3.8+**  
- **pip** (or `pipenv`/`poetry`)  
- **MongoDB Atlas** account & URI

---

## 🔧 Installation & Setup

1. **Clone & Enter Directory**  
   ```bash
   git clone https://github.com/Aryan556gaur/Roommate_Dekho.git
   cd Roommate_Dekho

---

Create & Activate Virtual Env

python3 -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate.bat     # Windows

Install Dependencies
pip install -r requirements.txt

Configure Your MongoDB URI
Edit the uri in inserter.py (or better—use environment variables!).

Create Upload Folder
mkdir images

🚀 Running the App
python mainfile.py

---

- Home: GET / → “welcome to roomy”
- Form: GET /predict → fill your profile (name, lat/long, budget, hobbies, veg-flag, mobile, photo)
- Match: POST /predict → returns a ranked list of 3 best roommate matches, complete with:

🏠 Distance
💬 Matching score (%)
📍 Full address
☎️ Contact info
🖼️ Profile image

---

## 📊 How It Works

**User Insertion**
New user data is saved to MongoDB, including profile image path.

**Nearby Filter**
nearloc.find_nearest_by_location() uses KDTree to filter everyone within 10 km.

**Cosine-Style Similarity**

**Budget is scaled.**

**Hobbies → TF-IDF vectors.**

**All features + veg-flag → FAISS L2 index.**

**Final Ranking**

**matching.model.find_nearest_neighbors() returns top 4 (drops the query itself), applies a max-distance threshold, reverse-geocodes their lat/long, and builds the final result set.**

---

# 🛣️ Roadmap & Future Enhancements

🔄 Real-time Chat between matched roommates
🌐 Dockerization for one-click deploy
📱 React/Vue Frontend for an interactive single-page experience
🔔 Push Notifications for new matches
🧪 Unit & Integration Tests for rock-solid reliability

---

🤝 Contributing
Fork

Branch: git checkout -b feature/YourFeature

Commit: git commit -m "✨ Add Your Feature"

Push: git push origin feature/YourFeature

PR: Open a Pull Request & let’s collaborate!

---

📄 License
Distributed under the MIT License. See LICENSE for details.

Enjoy happy, harmonious living—one perfect roommate at a time! 🏡✨
