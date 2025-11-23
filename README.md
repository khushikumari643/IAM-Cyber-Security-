# IAM-Cyber-Security-
outlines the proposed Identity and Access Management (IAM) solution  focusing on  : User Lifecycle Management (ULM) and Access Control Mechanisms (ACM). The design advocates for a modern, cloud-centric approach leveraging Identity Governance and Administration (IGA) and Zero Trust Architecture (ZTA) principles. 

**Foundational IAM Design Principles**
•	Least Privilege Principle: This mandates that all users (human and non-human) are granted the minimum access required to perform their specific job functions and nothing more. This principle is implemented across our design using Just-in-Time (JIT) Access and fine-grained entitlement policies .
•	Role-Based Access Control (RBAC): Permissions are assigned based on clearly defined, formal user roles. Implementing RBAC streamlines the provisioning process, particularly during bulk onboarding and role changes, significantly reducing administrative overhead.
•	User Lifecycle Management (ULM): Robust, automated processes are required to govern identity access from the moment a user joins the organisation until they leave (Joiner, Mover, Leaver). Our HR-driven approach ensures access is always aligned with a user's current status and responsibilities.
•	Strong Authentication: Security is fundamentally enhanced by requiring multiple factors of verification before granting access. Our design uses Multi-Factor Authentication (MFA) and leverages password less technology (FIDO2) to provide a phishing-resistant, low-friction user experience.
•	Audit and Monitoring: Continuous logging and reporting of all user activities and access events are essential for compliance and proactive threat detection. The chosen Identity Governance and Administration (IGA) and Privileged Access Management (PAM) platforms provide immutable audit trails for tracking anomalies and unauthorised access.

**. Technologies Utilised**
•	Identity Governance and Administration (IGA) Platform (e.g., SailPoint IdentityIQ/IdentityNow): The central orchestration layer for all identity and access requests, reviews, and automation.
•	Identity as a Service (IDaaS) / Central Directory (e.g., Microsoft Entra ID): Acts as the primary identity store and identity provider (IdP) for Single Sign-On (SSO) and Multi-Factor Authentication (MFA).
•	SCIM Protocol and Connectors: Standardised protocol used by the IGA platform to communicate with HRIS, Entra ID, and downstream SaaS applications (e.g., Salesforce, Jira).
