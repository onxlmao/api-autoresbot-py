"""Utility functions for the Autoresbot API client."""

import requests
from typing import Dict, Any, Optional


def build_headers(api_key: Optional[str]) -> Dict[str, str]:
    """
    Build request headers.
    
    Args:
        api_key (str, optional): API key for authorization.
        
    Returns:
        dict: Headers dictionary.
    """
    headers = {
        'User-Agent': f'Autoresbot-API-Python/1.0.0',
        'Accept': 'application/json'
    }
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'
    return headers


def build_query_params(params: Dict[str, Any] = None, api_key: Optional[str] = None, 
                       api_key_from_param: bool = False) -> Dict[str, Any]:
    """
    Build query parameters.
    
    Args:
        params (dict, optional): Base parameters.
        api_key (str, optional): API key.
        api_key_from_param (bool, optional): Whether to include API key in params.
        
    Returns:
        dict: Query parameters dictionary.
    """
    if api_key_from_param and api_key:
        return {**(params or {}), 'api_key': api_key}
    return params or {}


def handle_error(error: Exception) -> None:
    """
    Handle API errors with descriptive messages.
    
    Args:
        error (Exception): The error to handle.
        
    Raises:
        requests.HTTPError: Re-raised with descriptive message.
        requests.ConnectionError: Re-raised with descriptive message.
        requests.RequestException: Re-raised with descriptive message.
    """
    if isinstance(error, requests.exceptions.HTTPError):
        response = error.response
        status = response.status_code
        
        try:
            error_data = response.json()
            message = error_data.get('message') or error_data.get('error') or 'Unknown error'
        except ValueError:
            message = 'Unknown error'

        error_messages = {
            400: f"Bad Request: {message}",
            401: f"Unauthorized: {message} - Please check your API key",
            403: 'Forbidden: Access denied. Check your API key or permissions.',
            404: 'Not Found: The requested endpoint was not found.',
            429: f"Too Many Requests: {message}",
            500: 'Internal Server Error: The server encountered an error.',
            502: 'Bad Gateway: Invalid response from upstream server.',
            503: 'Service Unavailable: The server is temporarily unavailable.'
        }
        
        error_msg = error_messages.get(status, f"Unexpected error: {status} - {message}")
        raise Exception(error_msg) from error
            
    elif isinstance(error, requests.exceptions.ConnectionError):
        raise Exception('No response received from the server. Please check your internet connection.') from error
    elif isinstance(error, requests.exceptions.Timeout):
        raise Exception('Request timed out. Please try again.') from error
    elif isinstance(error, requests.exceptions.RequestException):
        raise Exception(f"Request failed: {str(error)}") from error
    else:
        raise error
