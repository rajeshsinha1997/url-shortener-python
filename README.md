# URL Shortener REST API

A basic URL shortening service developed as a REST API using Python and Flask. This API allows users to shorten long URLs into shorter versions, making them easier to share and manage.

## Features

- Shorten long URLs into short, unique identifiers
- Redirect users from short URLs to the original long URLs
- Retrieve service health data to monitor the status of the API
- Retrieve the original URL from a given short URL value

## Endpoints

- **GET /health**: Returns the service health data of the application along with the service health of its connected services. Example response:

    ```json
    {
        "response-timestamp": "2024/03/25T00:33:28:570514",
        "response-data": {
            "health-check-timestamp": "2024/03/25T00:33:28:570464",
            "application-name": "URL-SHORTENER-REST-API",
            "application-status": "UP",
            "connected-services-health": []
        }
    }
    ```

- **POST /shorten**: *(To be implemented)* Shorten a long URL into a shorter version. Example request:

    ```json
    {
        "long_url": "https://example.com/very/long/url"
    }
    ```

    Example response:

    ```json
    {
        "response-timestamp": "2024/03/25T00:33:28:570514",
        "response-data": {
            "short_url": "http://localhost:5000/abcd1234"
        }
    }
    ```

- **GET /\<short_url>**: *(To be implemented)* Redirect users from a short URL to the original long URL.

- **GET /original**: *(To be implemented)* Retrieve the original URL from the given short URL value. Example request:

    ```
    GET /original?short_url=abcd1234
    ```

    Example response:

    ```json
    {
        "response-timestamp": "2024/03/25T00:33:28:570514",
        "response-data": {
            "original_url": "https://example.com/very/long/url"
        }
    }
    ```

## Getting Started

1. Ensure you have Python 3.10 or later installed.
2. Clone this repository.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the Flask application:
   - For local or development environments, use: `flask run --debug`
   - For production or deployment environments, use: `flask run`
5. Access the API endpoints using a tool like cURL, Postman, or a web browser.
6. Explore the API using the included Postman collection, which provides example requests and corresponding example responses for each endpoint.

## Developers

- **[Rajesh Sinha](https://github.com/rajeshsinha1997)**
- **[Sudarshan Sinha](https://github.com/ssinha2103)**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Flask and Python community for providing excellent tools and libraries.
