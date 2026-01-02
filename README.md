# Frappe Dev Environment

This repository contains a Frappe Bench environment configured with modern specifications and customized for development.

## 🚀 Environment Specifications

- **Python:** 3.14.x
- **Frappe Framework:** v16.0.0-beta
- **Package Manager:** uv / pip / yarn
- **Database:** MariaDB (v12+)

## 🛠 Setup & Installation

To replicate this environment locally, ensure you have Python 3.14 and Node.js installed.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cangir/frappe-dev.git
   cd frappe-dev
   ```

2. **Setup Environment:**
   ```bash
   bench setup env --python /path/to/python3.14
   bench setup requirements
   ```

3. **Install Apps:**
   ```bash
   bench get-app frappe --branch version-16-beta
   ```

4. **Create a New Site:**
   ```bash
   bench new-site cng.localhost
   ```

## 💻 Working with the Bench

- **Start Development Server:**
  ```bash
  bench start
  ```

- **Update Dependencies:**
  ```bash
  bench setup requirements
  bench build
  ```

## 📂 Project Structure

- `apps/`: Contains the Frappe framework and custom applications.
- `sites/`: Contains site configurations and public/private files.
- `config/`: Configuration files for Redis, Nginx, etc.

## 📝 License

This project is for development purposes. Refer to Frappe Framework license for core usage.
