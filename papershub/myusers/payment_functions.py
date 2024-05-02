import requests

def azampay_mno_checkout(base_url, token, api_key, account_number, amount, currency, external_id, provider, additional_properties=None):
  """
  This function sends a POST request to Azampay MNO Checkout.

  Args:
      base_url (str): The base URL of the API endpoint.
      token (str): The authorization token (Bearer token).
      api_key (str): The X-API-Key for authentication.
      account_number (str): The account number for the mobile money transaction.
      amount (float): The transaction amount.
      currency (str): The currency code (e.g., TZS).
      external_id (str): An identifier for the transaction.
      additional_properties (dict, optional): Additional properties for the request. Defaults to None.

  Returns:
      dict: The response data as a dictionary (on success) or None (on error).
  """

  # Prepare data dictionary
  data = {
      'accountNumber': account_number,
      'amount': amount,
      'currency': currency,
      'externalId': external_id,
      'provider':provider
  }
  if additional_properties:
    data.update(additional_properties)

  # Prepare headers with authorization and API key
  headers = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {token}',
      'X-API-Key': api_key,
  }

  try:
    response = requests.post(f"{base_url}/azampay/mno/checkout", headers=headers, json=data)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    # Return response data
    return response.json()

  except requests.exceptions.RequestException as err:
    # Handle errors (e.g., network issues, server errors)
    print("Error:", err)
    return None

# # Example usage (replace placeholders with your values)
# base_url = "your_base_url"
# token = "your_authorization_token"
# api_key = "your_api_key"
# account_number = "1292-123"
# amount = 2000.0
# currency = "TZS"
# external_id = "123"
# provider:'Tigo'
# additional_properties = {"property1": None, "property2": None}  # Optional

# response_data = azampay_mno_checkout(base_url, token, api_key, account_number, amount, currency, external_id, additional_properties)

# if response_data:
#   print("Success! Response:", response_data)
# else:
#   print("Failed to process checkout.")




def generate_token(base_url, app_name, client_id, client_secret):
  """
  This function sends a POST request to generate a token.

  Args:
      base_url (str): The base URL of the API endpoint.
      app_name (str): The application name.
      client_id (str): The client ID.
      client_secret (str): The client secret.

  Returns:
      dict: The response data as a dictionary (on success) or None (on error).
  """

  # Data for the request
  data = {
     'clientId': client_id,
     'appName': app_name,
     'clientSecret': client_secret,   
  }

  try:
    response = requests.post(f"{base_url}/AppRegistration/GenerateToken", json=data)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    # Return response data
    return response.json()

  except requests.exceptions.RequestException as err:
    # Handle errors (e.g., network issues, server errors)
    print("Error:", err)
    return None

# Example usage