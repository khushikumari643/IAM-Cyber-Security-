"""
IAM Cybersecurity Automation Demo
This version avoids real API calls and uses mock data (dict + json).
Safe to run locally without network errors.
"""

import json
from typing import Dict

# -------------------------------
# MOCK FUNCTIONS
# -------------------------------

def sailpoint_get_identities() -> Dict:
    """Simulate fetching identities from SailPoint IGA."""
    mock_identities = [
        {"id": "101", "name": "Priya", "role": "Admin"},
        {"id": "102", "name": "Ravi", "role": "User"},
    ]
    return {"identities": mock_identities}

def sailpoint_provision_user(user_data: Dict) -> Dict:
    """Simulate provisioning a new user in SailPoint."""
    return {"status": "success", "provisioned_user": user_data}

def entra_get_users() -> Dict:
    """Simulate fetching users from Microsoft Entra ID."""
    mock_users = [
        {"id": "201", "name": "TechCorpUser1", "mfa_enabled": True},
        {"id": "202", "name": "TechCorpUser2", "mfa_enabled": False},
    ]
    return {"users": mock_users}

def entra_enable_mfa(user_id: str) -> Dict:
    """Simulate enabling MFA for a given user."""
    return {"status": "success", "user_id": user_id, "mfa_enabled": True}

def scim_provision_user(system: str, user_data: Dict) -> Dict:
    """Simulate provisioning user to downstream SaaS via SCIM."""
    return {"status": "success", "system": system, "user": user_data}

def scim_deprovision_user(system: str, user_id: str) -> Dict:
    """Simulate de-provisioning user from downstream SaaS via SCIM."""
    return {"status": "success", "system": system, "user_id": user_id}

# -------------------------------
# MAIN WORKFLOW
# -------------------------------

if __name__ == "__main__":
    print("🔐 IAM Cybersecurity Automation Demo Starting...\n")

    # Example: Fetch identities from SailPoint
    identities = sailpoint_get_identities()
    print("SailPoint identities:", json.dumps(identities, indent=2))

    # Example: Provision new user in SailPoint
    new_user = {"id": "103", "name": "Jane Doe", "role": "Manager"}
    provision_result = sailpoint_provision_user(new_user)
    print("\nProvision result:", json.dumps(provision_result, indent=2))

    # Example: Fetch users from Entra ID
    users = entra_get_users()
    print("\nEntra ID users:", json.dumps(users, indent=2))

    # Example: Enable MFA for a user
    mfa_result = entra_enable_mfa("202")
    print("\nMFA enable result:", json.dumps(mfa_result, indent=2))

    # Example: Provision user to Salesforce via SCIM
    scim_result = scim_provision_user("Salesforce", new_user)
    print("\nSCIM provision result:", json.dumps(scim_result, indent=2))

    # Example: De-provision user from Jira via SCIM
    scim_deprov_result = scim_deprovision_user("Jira", "103")
    print("\nSCIM de-provision result:", json.dumps(scim_deprov_result, indent=2))
