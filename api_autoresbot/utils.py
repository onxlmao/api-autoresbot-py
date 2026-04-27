import requests
from typing import Dict, Any, Optional


def build_headers(api_key: Optional[str]) -> Dict[str, str]:
    headers = {}
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'
    return headers


def build_query_params(params: Dict[str, Any] = None, api_key: Optional[str] = None, 
                       api_key_from_param: bool = False) -> Dict[str, Any]:
    if api_key_from_param and api_key:
        return {**(params or {}), 'api_key': api_key}
    return params or {}


def handle_error(error: Exception) -> None:
    if isinstance(error, requests.exceptions.HTTPError):
        response = error.response
        status = response.status_code
        
        try:
            error_data = response.json()
            message = error_data.get('message') or error_data.get('error') or 'Unknown error'
        except ValueError:
            message = 'Unknown error'

        if status == 400:
            raise Exception(f"Bad Request: {message}")
        elif status == 401:
            raise Exception(f"Unauthorized: {message}")
        elif status == 403:
            raise Exception('Forbidden: Access denied. Check your API key or permissions.')
        elif status == 404:
            raise Exception('Not Found: Endpoint not found.')
        elif status == 429:
            raise Exception(f"Too Many Requests: {message}")
        elif status == 500:
            raise Exception('Internal Server Error: The server encountered an error.')
        else:
            raise Exception(f"Unexpected error: {status} - {message}")
            
    elif isinstance(error, requests.exceptions.ConnectionError):
        raise Exception('No response received from the server.')
    elif isinstance(error, requests.exceptions.RequestException):
        raise Exception(f"Request failed: {str(error)}")
    else:
        raise error
