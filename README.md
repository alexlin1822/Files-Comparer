# Files-Comparer

Comparing all files in two folder.

Crypto  
Based on Chapter 2 of Information Security (2nd Edition) by Mark Stamp

1. Decrypt the following message that was encrypted using a simple substitution cipher. The plaintext has no spaces or punctuation. (warning: there may be the odd transmission error) Submit the plaintext answer and key, along with an explanation on how you solved the problem and all source code that you developed (use Java, C, or Python) to help you arrive at your answer. The cyphertext is as follows:

PBFPVYFBQXZTYFPBFEQJHDXXQVAPTPQJKTOYQWIPBVWLXTOXBTFXQWAXBVCXQWAXFQJVWLEQNTOZQGGQLFXQWAKVWLXQWAEBIPBFXQVXGTVJVWLBTPQWAEBFPBFHCVLXBQUFEVWLXGDPEQVPQGVPPBFTIXPFHXZHVFAGFOTHFEFBQUFTDHZBQPOTHXTYFTODXQHFTDPTOGHFQPBQWAQJJTODXQHFOQPWTBDHHIXQVAPBFZQHCFWPFHPBFIPBQWKFABVYYDZBOTHPBQPQJTQOTOGHFQAPBFEQJHDXXQVAVXEBQPEFZBVFOJIWFFACFCCFHQWAUVWFLQHGFXVAFXQHFUFHILTTAVWAFFAWTEVOITDHFHFQAITIXPFHXAFQHEFZQWGFLVWPTOFFA

Note, that you will need to write your own code to decrypt the message. Using code or websites available on the Internet or other places to decrypt the message is not allowed. Instead, you should use a large English text corpus from, for example, Wikipedia and do a character frequency analysis on the data as was described in class. Your code should remove spaces, punctuation, and non-alphabetic characters and convert the remaining characters to upper case. Then, your code should do a character frequency analysis on the ciphertext. Explain what you did to recover the plaintext after the two frequency analyses. Submit your data and code along with the key and the recovered plaintext.






1. Roles and Responsibilities
Role/Team	Responsibilities
Vendor (COTS Package & Mobile App)	- Maintaining the DDL COTS package.- Having an agreement with MST to share new versions of the COTS package.- Managing the mobile version of the application.- Providing new mobile packages to Artifactory.
API Platform Team	- Generating API keys for the Mobile platform (for proxy integration).- Rotating API keys every three months.- Sharing new API keys with the Support team (and then ultimately ECCT).
Support Team (Likely your team based on context)	- Receiving rotated API keys from the API Platform team.- Forwarding the API keys to the ECCCD team.- Updating OAuth client ID and secret in AWS Secrets Manager for webapp.- Sending release notes to relevant teams (OA, client-side, etc.).
ECCCD Team	- Republishing the mobile application package with new API keys embedded.
CIAM Team	- Rotating and providing OAuth client ID and secret for webapp.- Rotating and providing OAuth client ID for mobile app.
Mobile Platform Team	- Receiving mobile artifact/package from the vendor.- Deploying the mobile application (presumably to production).- Sharing requirements with GO single point of contact (indirectly implied).
IHD Team	- (To be checked/confirmed) -  Potentially responsible for ECF backup.
GO Single Point of Contact	-  Point of contact for understanding requirements (likely business requirements).
AWS Team/Admin (Implied)	- Managing AWS infrastructure, including ECS, Secret Manager, etc. (Implicitly responsible for ensuring the AWS environment is functioning for these procedures).

2. Assumptions, Limitations, and Exclusions

Assumptions:

AWS Knowledge: It is assumed that the personnel performing these procedures have adequate knowledge of AWS services (ECS, Secret Manager, CloudWatch, etc.). (Source: "just saying assumption is that the person has AWs knowledge")
PingOne Connection: It's assumed the system/team is connected to and integrated with PingOne for authentication/SSO. (Source: "team has connected to the Ping one solution")
Team Access to Systems: It's assumed the support team and other relevant teams have the necessary access to AWS accounts, Secret Manager, Artifactory, and other systems mentioned to perform their responsibilities. (Implied by the procedures described)
Vendor Agreement in Place: Assumes a formal agreement with the vendor is in place for COTS package updates and mobile application management, including timely delivery of updates and artifacts. (Source: "vendor is responsible for maintaining the courts package and has a agreement with MST")
CIAM Team Responsiveness: Assumes CIAM team will provide rotated OAuth credentials in a timely manner when needed. (Implied by dependency on CIAM for webapp and mobile app updates)
Limitations and Exclusions:

Ad-hoc Requests: Many actions (like resizing, log review, updates driven by vendor releases or key rotations) are triggered by ad-hoc requests or external events rather than scheduled maintenance. (Source: "But all of it is an ad hoc request so yes because it's based on the IOc request right we can't do it like there's no scheduled maintenance for this.")
GXP Act Compliance (Conditional): Compliance with GXP Act is conditional. If evidence is required, it will be addressed, but if not business-critical, it may be deprioritized. (Source: "GXP Act is conditional evidence is conditional So it's conditional then while you spending time. We are not business critical, for sure... If they want evidence, we can do the evidence, but if it is not critical, then why to spend di weight?")
Disaster Recovery Plan (DRP) Location Uncertainty initially: Initially, there was uncertainty about where the Disaster Recovery Plan is documented (QAR vs. dedicated document). This highlights a potential limitation in document management or clarity. (Source: "Based is a disaster recovery, there was a document for disaster recovery, but it go. I guess I'm not sure I know that's on the change request as well yeah, so yeah it is right that's only documents so DRP right by find there here now. Maybe disaster, yes, all right, so so one of you right has to pick up this document")
Database Resizing/Rescaling (Mentioned but less detail): Database resizing and rescaling are mentioned as being possible via Terraform but with less detail than web app task resizing. Further details might be needed on the database procedure. (Source: "Not our or you might have to do this for database also okay, like if the recaling needs to happen for database.")
3. Frequency/Schedule

DDL COTS Package Updates: Frequency is based on vendor releases and is therefore unpredictable but event-driven (release note received). (Source: "Receive release note of new/updated DDL COTS package from vendor")
OAuth Client ID and Secret Rotation (Webapp): Frequency is based on CIAM team's rotation schedule, which is likely periodic but unspecified in this conversation. Triggered by notification from CIAM. (Source: "Get rotated OAuth client id and secret from CIAM team for webapp")
Web App ECS Task Resizing/Rescaling: Ad-hoc, based on performance requirements or observed performance issues (CPU/Memory utilization). (Source: "Resizing & rescaling web app ECS task(s) and/or backend database based on performance requirement", "if they're running into performance problem right where the tasks are not scaling and they want to change it")
API Platform Key Rotation (Mobile App): Every three months. (Source: "every three months, they are going to rotate the keys.")
OAuth Client ID Rotation (Mobile App): Frequency is based on CIAM team's rotation schedule, likely periodic but unspecified. Triggered by notification from CIAM. (Source: "Get rotated Qautb client id from CIAM team for Mobile app")
Mobile Artifact Upload & Sharing: Frequency is driven by vendor mobile application releases and is therefore unpredictable but event-driven (new package from vendor). (Source: "Mobile artifactqr.y upload and sharing with Mobile platform team for production deployment", "the lenderer will provide the new mobile package.")
CloudWatch Log Review: Ad-hoc, performed when monitoring for errors or troubleshooting. (Source: "Review gloudwatgb logs for monitoring errors- COMET send/aGknpwledgement.P.ingQne authentication", implies reactive monitoring)
