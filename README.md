# Dummy JSON API Fetching, Application, and Manipulation in Django

## Project Overview
This Django project demonstrates how to fetch, apply, and manipulate dummy JSON data from external sources. It is structured into three different Django applications, each handling a specific JSON file:

1. **Carts** - Handles cart-related JSON data.
2. **Recipes** - Fetches and manipulates recipe data.
3. **Products** - Manages product information.

Each application renders the fetched data in separate HTML templates using Django's context property.

---

## Project Structure
```
DummyJSONProject/
│── carts/
│   ├── templates/
│   │   ├── carts.html
│   ├── views.py
│   ├── urls.py
│
│── recipes/
│   ├── templates/
│   │   ├── recipes.html
│   ├── views.py
│   ├── urls.py
│
│── products/
│   ├── templates/
│   │   ├── products.html
│   ├── views.py
│   ├── urls.py
│
│── DummyJSONProject/
│   ├── settings.py
│   ├── urls.py
│
│── templates/
│   ├── base.html
│
│── static/
│── manage.py
```

---

## Installation & Setup

### 1. Clone the Repository
```sh
$ git clone https://github.com/yourusername/dummy-json-django.git
$ cd dummy-json-django
```

### 2. Create and Activate Virtual Environment
```sh
$ python -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Run the Django Server
```sh
$ python manage.py runserver
```

---

## Fetching and Displaying JSON Data
Each Django app fetches data from a dummy JSON API and displays it using templates.

### Example: Fetching and Displaying Carts JSON
#### `views.py` (Carts App)
```python
import requests
from django.shortcuts import render

def carts_view(request):
    url = "https://dummyjson.com/carts"
    response = requests.get(url)
    carts_data = response.json()
    return render(request, "carts.html", {"carts": carts_data["carts"]})
```

#### `carts.html`
```html
{% extends 'base.html' %}
{% block content %}
    <h2>Carts Data</h2>
    <ul>
        {% for cart in carts %}
            <li>Cart ID: {{ cart.id }} - Total: {{ cart.total }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

### Similarly, Recipes and Products apps follow the same pattern:
- **Recipes:** Fetches data from `https://dummyjson.com/recipes`
- **Products:** Fetches data from `https://dummyjson.com/products`

---

## Features
- Fetches JSON data from an external API.
- Uses Django’s context property to pass data to templates.
- Displays data in separate HTML pages.
- Modular structure with separate Django apps.

---

## Contribution
Feel free to contribute to this project by:
- Adding more API endpoints.
- Enhancing the UI.
- Optimizing the API fetching process.

Fork the repository, make changes, and submit a pull request.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Contact
For any queries, reach out at: your.email@example.com

