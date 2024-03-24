# URL-Shortener Service

Welcome to our URL-Shortener Service, a RESTful API designed to provide an easy and efficient way to shorten long URLs. This service is built using Python, Flask, and is aimed at developers looking to integrate URL shortening capabilities into their applications or projects.

## Features

- **Shorten URLs:** Convert long URLs into shorter, more manageable versions that are easier to share.
- **RESTful API:** Simple and straightforward API endpoints for shortening URLs and retrieving the original URLs.
- **Easy Integration:** Designed with developers in mind, our API can be easily integrated into any application requiring URL shortening functionality.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or later
- Flask
- Any REST Client (Postman, curl, etc.)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/url-shortener-service.git
   ```

2. Navigate to the project directory:
   ```sh
   cd url-shortener-service
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```sh
   flask run
   ```

Your URL-Shortener service should now be running locally on `http://localhost:5000`.

## Usage

### Shortening a URL

- **Endpoint:** `/shorten`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "url": "https://www.example.com/a-very-long-url-you-want-to-shorten"
  }
  ```

- **Response:**
  ```json
  {
    "shortened_url": "http://localhost:5000/abc123"
  }
  ```

### Retrieving the Original URL

- **Endpoint:** `/<shortened_id>`
- **Method:** `GET`

- **Response:**
  The service will redirect you to the original URL.

## API Reference

Please refer to the `docs` folder for a detailed API reference.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, open issues, or suggest new features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries or feedback, please open an issue on the project's GitHub page.

---
