# __Access Key Manager__
## Project Description
Access Key Manager is a web application designed to facilitate the management and purchase of access keys for schools using Micro-Focus Inc.'s (a hypothetical organization) school management platform. The platform operates on a multi-tenant system, allowing multiple schools to set up accounts as if the platform was tailored specifically for them. Instead of integrating payment features directly into the school software, the decision was made to implement an access key-based monetization approach.

## Customer Requirements
School IT Personnel
Authentication: Users can sign up and log in using their email and password, with account verification. A reset password feature is available to recover lost passwords.
View Access Keys: Users can see a list of all access keys, including active, expired, or revoked keys.
Access Key Details: For each access key, personnel can view its status, date of procurement, and expiry date.
Single Active Key: Users cannot obtain a new key if an active key is already assigned to them. Only one key can be active at a time.

## Micro-Focus Admin
Authentication: Admins can log in using their email and password.
Key Management: Admins have the ability to manually revoke access keys.
Access Key Overview: Admins can view all keys generated on the platform, including their status, procurement date, and expiry date.
Integration Endpoint: An endpoint is available for integration purposes, allowing administrators to check the status of active keys by providing the school email. The endpoint returns a status code of 200 along with key details if an active key is found, or 404 if not.

## Deliverables
Web Application Source Code: The source code is available on GitHub.
ER Diagram: An Entity-Relationship (ER) diagram illustrating the database design is included.
Deployed Link: The web application is deployed and accessible online.