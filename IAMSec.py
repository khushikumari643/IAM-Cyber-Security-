"""
IAM Cybersecurity Automation Project
Technologies:
- SailPoint IdentityIQ/IdentityNow (IGA)
- Microsoft Entra ID (IDaaS)
- SCIM Protocol for SaaS connectors (Salesforce, Jira)
"""

import requests
import json
from typing import Dict

# -------------------------------
# CONFIGURATION
# -------------------------------
SAILPOINT_BASE_URL = "https://your-sailpoint-instance/api"
SAILPOINT_API_KEY = "your_sailpoint_api_key"

ENTRA_BASE_URL = "https://graph.microsoft.com/v1.0"
ENTRA_TOKEN = "your_ms_graph_token"

SCIM_SALESFORCE_URL = "https://your-salesforce-instance/scim/v2"
SCIM_JIRA_URL = "https://your-jira-instance/scim/v2"
SCIM_TOKEN = "your_scim_token"

# -------------------------------
# IGA FUNCTIONS (SailPoint)
# -------------------------------
def sailpoint_get_identities() -> Dict:
    """Fetch identities from SailPoint IGA."""
    headers = {"Authorization": f"Bearer {SAILPOINT_API_KEY}"}
    response = requests.get(f"{SAILPOINT_BASE_URL}/identities", headers=headers)
    return response.json()

def sailpoint_provision_user(user_data: Dict) -> Dict:
    """Provision a new user in SailPoint."""
    headers = {"Authorization": f"Bearer {SAILPOINT_API_KEY}", "Content-Type": "application/json"}
    response = requests.post(f"{SAILPOINT_BASE_URL}/identities", headers=headers, data=json.dumps(user_data))
    return response.json()

# -------------------------------
# IDaaS FUNCTIONS (Microsoft Entra ID)
# -------------------------------
def entra_get_users() -> Dict:
    """Fetch users from Microsoft Entra ID (Azure AD)."""
    headers = {"Authorization": f"Bearer {ENTRA_TOKEN}"}
    response = requests.get(f"{ENTRA_BASE_URL}/users", headers=headers)
    return response.json()

def entra_enable_mfa(user_id: str) -> Dict:
    """Enable MFA for a given user in Entra ID."""
    headers = {"Authorization": f"Bearer {ENTRA_TOKEN}", "Content-Type": "application/json"}
    mfa_policy = {
        "strongAuthenticationMethods": [
            {"method": "phone", "isDefault": True}
        ]
    }
    response = requests.patch(f"{ENTRA_BASE_URL}/users/{user_id}", headers=headers, data=json.dumps(mfa_policy))
    return response.json()

# -------------------------------
# SCIM FUNCTIONS (Salesforce / Jira)
# -------------------------------
def scim_provision_user(scim_url: str, user_data: Dict) -> Dict:
    """Provision user to downstream SaaS via SCIM."""
    headers = {"Authorization": f"Bearer {SCIM_TOKEN}", "Content-Type": "application/json"}
    response = requests.post(f"{scim_url}/Users", headers=headers, data=json.dumps(user_data))
    return response.json()

def scim_deprovision_user(scim_url: str, user_id: str) -> Dict:
    """De-provision user from downstream SaaS via SCIM."""
    headers = {"Authorization": f"Bearer {SCIM_TOKEN}"}
    response = requests.delete(f"{scim_url}/Users/{user_id}", headers=headers)
    return {"status": response.status_code}

# -------------------------------
# MAIN WORKFLOW
# -------------------------------
if __name__ == "__main__":
    print("🔐 IAM Cybersecurity Automation Starting...")

    # Example: Fetch identities from SailPoint
    identities = sailpoint_get_identities()
    print(f"Fetched {len(identities)} identities from SailPoint")

    # Example: Fetch users from Entra ID
    users = entra_get_users()
    print(f"Fetched {len(users['value'])} users from Entra ID")

    # Example: Provision user to Salesforce via SCIM
    new_user = {
        "userName": "jane.doe@example.com",
        "name": {"givenName": "Jane", "familyName": "Doe"},
        "emails": [{"value": "jane.doe@example.com", "primary": True}]
    }
    scim_response = scim_provision_user(SCIM_SALESFORCE_URL, new_user)
    print(f"Provisioned user to Salesforce: {scim_response}")
