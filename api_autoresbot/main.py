import requests
import os
from typing import Optional, Dict, Any, BinaryIO, Union
from utils import build_headers, build_query_params, handle_error

BASE_URL = 'https://api.autoresbot.com'  # http://localhost:3000 https://api.autoresbot.com
BASE_UPLOADER = 'https://autoresbot.com'  # https://autoresbot.com


class ApiAutoresbot:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def get(self, endpoint: str, params: Dict[str, Any] = None, api_key_from_param: bool = False) -> Dict[str, Any]:
        try:
            headers = build_headers(self.api_key)
            query_params = build_query_params(params or {}, self.api_key, api_key_from_param)

            response = requests.get(
                f"{BASE_URL}{endpoint}",
                headers=headers,
                params=query_params
            )
            response.raise_for_status()
            return response.json()
        except Exception as error:
            handle_error(error)

    def post(self, endpoint: str, data: Dict[str, Any] = None, api_key_from_param: bool = False) -> Dict[str, Any]:
        try:
            headers = build_headers(self.api_key)
            query_params = build_query_params({}, self.api_key, api_key_from_param)

            response = requests.post(
                f"{BASE_URL}{endpoint}",
                json=data or {},
                headers=headers,
                params=query_params
            )
            response.raise_for_status()
            return response.json()
        except Exception as error:
            handle_error(error)

    def get_json(self, endpoint: str, params: Dict[str, Any] = None, api_key_from_param: bool = False) -> Dict[str, Any]:
        try:
            headers = build_headers(self.api_key)
            query_params = build_query_params(params or {}, self.api_key, api_key_from_param)

            response = requests.get(
                f"{BASE_URL}{endpoint}",
                headers=headers,
                params=query_params
            )
            response.raise_for_status()
            return response.json()
        except Exception as error:
            handle_error(error)

    def get_buffer(self, endpoint: str, params: Dict[str, Any] = None, api_key_from_param: bool = False) -> bytes:
        try:
            headers = build_headers(self.api_key)
            query_params = build_query_params(params or {}, self.api_key, api_key_from_param)

            response = requests.get(
                f"{BASE_URL}{endpoint}",
                headers=headers,
                params=query_params
            )
            response.raise_for_status()
            return response.content
        except Exception as error:
            handle_error(error)

    def tmp_upload(self, file_path: str) -> Dict[str, Any]:
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            with open(file_path, 'rb') as file:
                files = {'file': (os.path.basename(file_path), file)}
                response = requests.post(
                    f"{BASE_UPLOADER}/tmp-files/upload",
                    files=files
                )
                response.raise_for_status()
                return response.json()
        except Exception as error:
            print(error)
            handle_error(error)
