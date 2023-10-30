# FlaskMart: A Custom E-Commerce Platform

Welcome to FlaskMart, a basic yet functional implementation of an e-commerce platform built using Flask, a micro web framework written in Python. This application allows users to register, browse through a catalog of products, and proceed to checkout using Stripe for secure payment processing.

## Technologies Used

- **Python**: The main programming language for backend development.
- **Flask**: A micro web framework for Python used to build the web application.
- **SQLite**: A lightweight, file-based database used for storing user and product data.
- **Stripe**: A third-party service for handling secure credit card transactions.

## Project Structure

- **app.py**: The main file that runs the Flask application. It includes routes for user registration, product listing, and the checkout process.
- **models.py**: This file defines the SQLAlchemy data models, including `User`, `Product`, and `Order`.
- **forms.py**: This file contains WTForms classes for user registration and product checkout.
- **templates/**: A directory housing HTML templates for rendering views.

## Setup and Installation

1. Clone the repository 
2. Install the required packages
3. Run the application
4. Open a web browser and navigate to `http://127.0.0.1:5000/` to access FlaskMart.

## Future Work and Enhancements

- **User Authentication**: Enhance the user authentication system, incorporating password hashing and validation.
- **Product Management**: Implement an admin panel for product lifecycle management (addition, update, and removal).
- **Order Management**: Integrate an order system to track user purchases and manage order statuses.
- **Responsive Design**: Refine the front-end templates for a seamless user experience across devices.
- **Testing**: Establish a suite of unit and integration tests to ensure reliable functionality.

## Contributing

We welcome contributions to FlaskMart! If you have suggestions or enhancements, feel free to fork the repository, make your changes, and submit a pull request. Alternatively, you can open an issue to discuss potential improvements.

## License

FlaskMart is released under the MIT License. For more details, see the [LICENSE](LICENSE) file included in the repository.



