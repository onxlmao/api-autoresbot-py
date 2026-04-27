"""Main API client module."""

import requests
import os
from typing import Optional, Dict, Any, Union
from .utils import build_headers, build_query_params, handle_error

BASE_URL = 'https://api.autoresbot.com'
BASE_UPLOADER = 'https://autoresbot.com'


class ApiAutoresbot:
    """
    Autoresbot API Client.
    
    A client for interacting with the Autoresbot API services.
    
    Args:
        api_key (str, optional): Your Autoresbot API key. Defaults to None.
    
    Example:
        >>> from autoresbot import ApiAutoresbot
        >>> api = ApiAutoresbot('your_api_key')
        >>> response = api.get('/api/game/family100')
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.session = requests.Session()

    def get(self, endpoint: str, params: Dict[str, Any] = None, 
            api_key_from_param: bool = False) -> Dict[str, Any]:
        """
        Send a GET request to the API.
        
        Args:
            endpoint (str): API endpoint path.
            params (dict, optional): Query parameters. Defaults to None.
            api_key_from_param (bool, optional): Include API key in query params. Defaults to False.
            
        Returns:
            dict: JSON response from the API.
            
        Raises:
            Exception: If the request fails.
        """
        try:
            headers = build_headers(self.api_key)
            query_params = build_query_params(params or {}, self.api_key, api_key_from_param)

            response = self.session.get(
                f"{BASE_URL}{endpoint}",
                headers=headers,
                params=query_params
            )
            response.raise_for_status()
            return response.json()
        except Exception as error:
            handle_error(error)

    def post(self, endpoint: str, data: Dict[str, Any] = None, 
             api_key_from_param: bool = False) -> Dict[str, Any]:
        """
        Send a POST request to the API.
        
        Args:
            endpoint (str): API endpoint path.
            data (dict, optional): Request body data. Defaults to None.
            api_key_from_param (bool, optional): Include API key in query params. Defaults to False.
            
        Returns:
            dict: JSON response from the API.
            
        Raises:
            Exception: If the request fails.
        """
        try:
            headers = build_headers(self.api_key)
            query_params = build_query_params({}, self.api_key, api_key_from_param)

            response = self.session.post(
                f"{BASE_URL}{endpoint}",
                json=data or {},
                headers=headers,
                params=query_params
            )
            response.raise_for_status()
            return response.json()
        except Exception as error:
            handle_error(error)

    def get_json(self, endpoint: str, params: Dict[str, Any] = None, 
                 api_key_from_param: bool = False) -> Dict[str, Any]:
        """
        Get JSON response from the API.
        
        Args:
            endpoint (str): API endpoint path.
            params (dict, optional): Query parameters. Defaults to None.
            api_key_from_param (bool, optional): Include API key in query params. Defaults to False.
            
        Returns:
            dict: JSON response from the API.
            
        Raises:
            Exception: If the request fails.
        """
        return self.get(endpoint, params, api_key_from_param)

    def get_buffer(self, endpoint: str, params: Dict[str, Any] = None, 
                   api_key_from_param: bool = False) -> bytes:
        """
        Get binary buffer from the API (for files, images, etc).
        
        Args:
            endpoint (str): API endpoint path.
            params (dict, optional): Query parameters. Defaults to None.
            api_key_from_param (bool, optional): Include API key in query params. Defaults to False.
            
        Returns:
            bytes: Binary content from the response.
            
        Raises:
            Exception: If the request fails.
        """
        try:
            headers = build_headers(self.api_key)
            query_params = build_query_params(params or {}, self.api_key, api_key_from_param)

            response = self.session.get(
                f"{BASE_URL}{endpoint}",
                headers=headers,
                params=query_params
            )
            response.raise_for_status()
            return response.content
        except Exception as error:
            handle_error(error)

    def tmp_upload(self, file_path: str) -> Dict[str, Any]:
        """
        Upload a temporary file to Autoresbot.
        
        Files uploaded will expire after 1 week, but the expiry is renewed 
        each time the file is accessed.
        
        Args:
            file_path (str): Path to the file to upload.
            
        Returns:
            dict: Response containing file information.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            Exception: If the upload fails.
        """
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            with open(file_path, 'rb') as file:
                files = {'file': (os.path.basename(file_path), file)}
                response = self.session.post(
                    f"{BASE_UPLOADER}/tmp-files/upload",
                    files=files
                )
                response.raise_for_status()
                return response.json()
        except Exception as error:
            print(f"Upload error: {error}")
            handle_error(error)

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - closes the session."""
        self.session.close()

    def __repr__(self):
        return f"ApiAutoresbot(api_key={'***' if self.api_key else None})"
