# Smart Cart Master (SCM)

**Smart Cart Master** (SCM) is an advanced application designed to manage grocery shopping, culinary recipes, and refrigerator items. The app allows users to create shopping lists, manage fridge contents, track nutritional values of products 
and organize recipes. Future plans include expanding functionality with a mobile app and a web version.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Future Plans](#future-plans)
- [System Requirements](#system-requirements)
- [Author](#author)

## Features

- Create and manage shopping lists.
- Manage grocery items in the refrigerator.
- Organize culinary recipes.
- Calculate nutritional values (macro and micronutrients).
- Track purchase and expiration dates of products.
- Support for various units of measurement (pieces, kilograms, liters, etc.).
- Planned expansion for a mobile app and web version.

## Project Structure

```plaintext
    smart_cart_master/
    │
    ├── core/
    │   ├── __init__.py
    │   ├── food.py           # Manage grocery items (product descriptions)
    │   ├── fridge.py         # Manage refrigerator items
    │   ├── shopping_list.py  # Manage shopping lists
    │   ├── recipe_list.py    # Manage list of cooking ingredients
    │   ├── recipes.py        # Manage recipes
    │   ├── nutrition.py      # Calculate caloric and nutritional values
    │   └── utils.py          # Helper functions
    │   └── manager.py        # Main management module
    │
    ├── database/
    │   ├── __init__.py
    │   ├── models.py         # SQLAlchemy model definitions (including FoodModel)
    │   ├── database.py       # Database and session configuration, data operations
    │   ├── food.db           # SQLite database file
    │   └── migrations/       # Potential database migrations
    │
    ├── gui/
    │   ├── __init__.py
    │   ├── main_window.py    # Main user interface (GUI)
    │   ├── shopping_list.py  # Shopping list view
    │   ├── fridge_view.py    # Refrigerator view
    │   ├── recipe_view.py    # Recipe view
    │   └── widgets.py        # Custom GUI widgets
    │
    ├── web/                  # (Future development)
    │   ├── __init__.py
    │   ├── forms.py          # Forms (if using Django)
    │   └── static/           # Static files (CSS, JS, images)
    │   ├── settings.py       # Django configuration
    │   ├── urls.py           # URL routing for the web app
    │   ├── views.py          # Web views
    │   └── models.py         # Django database models
    │
    ├── docs/                # Project documentation
    │   ├── architecture.md  # Project architecture documentation
    │   ├── classes.md       # Description of key classes and methods
    │   └── usage.md         # Application usage instructions
    │
    ├── main.py               # Main file to launch the desktop application
    ├── requirements.txt      # List of Python dependencies
    └── README.md             # Project description

```
## Installation

   1. **Clone the repository**:

      ```bash
      git clone https://github.com/BartoszSzyca/SCM.git
      cd SCM
      ```
   2. **Install required dependencies**:

      Use pip to install all dependencies from the requirements.txt file:

      ```bash 
      pip install -r requirements.txt
      ```
   3. **Database setup**:

      After installing the dependencies, ensure that the food.db file is in the correct location within the database/ folder. If the database requires migration, run the necessary migration commands.

   4. **Run the application**:

      In the main project folder, run the application using:

      ```bash
      python main.py
      ```
      
      This should start the desktop application. You can now use the app's features such as managing shopping lists, fridge contents, and recipes.

## Usage

   1. Creating and managing shopping lists:

      In the user interface, go to the "Shopping List" tab to add, edit, and remove products. You can also see a cost summary.

   2. Managing products in the fridge:

      Go to the "Fridge" tab to track products, their expiration dates, and storage conditions. You can edit product information directly from this view.

   3. Organizing recipes:

      In the "Recipes" tab, you can add, edit, and delete recipes. You can also browse recipes and add ingredients to the shopping list with one click.

   4. Calculating nutritional values:

      In the "Calculations" section, you can enter nutritional data such as calories, macro, and micronutrients. The app automatically calculates values based on the entered data.

## Future Plans

   * Development of a mobile and web app.
   * Integration with delivery services such as UberEats and Glovo.
   * Expansion of diet analysis and meal planning features.

## System Requirements

   * Python 3.x
   * SQLite (for database)
   * Operating System: Windows, macOS, or Linux

## Author

   * Bartosz Szyca

## License

  The project is available under the MIT License.
