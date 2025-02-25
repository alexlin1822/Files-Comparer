# Files-Comparer

Comparing all files in two folder.

Crypto  
Based on Chapter 2 of Information Security (2nd Edition) by Mark Stamp

1. Decrypt the following message that was encrypted using a simple substitution cipher. The plaintext has no spaces or punctuation. (warning: there may be the odd transmission error) Submit the plaintext answer and key, along with an explanation on how you solved the problem and all source code that you developed (use Java, C, or Python) to help you arrive at your answer. The cyphertext is as follows:

PBFPVYFBQXZTYFPBFEQJHDXXQVAPTPQJKTOYQWIPBVWLXTOXBTFXQWAXBVCXQWAXFQJVWLEQNTOZQGGQLFXQWAKVWLXQWAEBIPBFXQVXGTVJVWLBTPQWAEBFPBFHCVLXBQUFEVWLXGDPEQVPQGVPPBFTIXPFHXZHVFAGFOTHFEFBQUFTDHZBQPOTHXTYFTODXQHFTDPTOGHFQPBQWAQJJTODXQHFOQPWTBDHHIXQVAPBFZQHCFWPFHPBFIPBQWKFABVYYDZBOTHPBQPQJTQOTOGHFQAPBFEQJHDXXQVAVXEBQPEFZBVFOJIWFFACFCCFHQWAUVWFLQHGFXVAFXQHFUFHILTTAVWAFFAWTEVOITDHFHFQAITIXPFHXAFQHEFZQWGFLVWPTOFFA

Note, that you will need to write your own code to decrypt the message. Using code or websites available on the Internet or other places to decrypt the message is not allowed. Instead, you should use a large English text corpus from, for example, Wikipedia and do a character frequency analysis on the data as was described in class. Your code should remove spaces, punctuation, and non-alphabetic characters and convert the remaining characters to upper case. Then, your code should do a character frequency analysis on the ciphertext. Explain what you did to recover the plaintext after the two frequency analyses. Submit your data and code along with the key and the recovered plaintext.






Roles and R
1. Documentation Team (You, Dn, Christian, Imina, Lead):
* Develop and document Operational Procedures (SOPs).
* Develop and document Disaster Recovery Plan (DRP).
* Assist Digital Team with STLC documents.
* Incorporate AWS and Security best practices in documentation.
* Document Resizing & Rescaling procedures.
* Document Mobile Artifact Handling.
* Document API Key Rotation procedures.
* Document Log Monitoring.
* Maintain and update documentation.

2. Vendor (COTS Package & Mobile App Provider):
* Provide DDL COTS package updates with release notes.
* Maintain COTS package and Mobile App version.
* Share new Web and Mobile App versions with MST.
* Provide updated credentials/API keys.

3. CIAM Team (PingOne Team / Sand Team):
* Manage PingOne Keys (SignM and Sand Keys).
* Rotate OAuth Client ID and Secret (Webapp).
* Rotate Qauth Client ID (Mobile App).
* Share rotated keys with EMS Team.

4. EMS Team (Enterprise Monitoring & Support Team / Support Team):
* Receive rotated keys from CIAM Team.
* Update Webapp secrets in AWS Secret Manager.
* Provide Mobile App keys to ECCCD (or relevant team - clarify).
* Inform ECCCD to republish Webapp.
* Handle key rotation communication.

5. ECCCD (Engineering Continuous Integration Continuous Delivery Team):
* Update Webapp package with new keys.
* Run CI/CD pipeline for Webapp updates.
* Potentially involved in Mobile App deployment (clarify).

6. API Platform Team:
* Generate API Platform Keys (Mobile Platform).
* Rotate API Platform Keys.
* Share new API keys with EMS Team.
* Manage API Proxy (A Platform).

7. Mobile Platform Team:
* Receive Mobile Artifact uploads.
* Deploy Mobile Application to Production.
* Report performance issues.
* Utilize API Platform Proxy & API Keys.

8. IHD (Infrastructure Hosting Department - Assumption):
* To be Confirmed: ECF (ECS) Backup Procedures.

9. GO Single Point of Contact (SPOC):
* Clarify requirements for documentation.
* Potentially: Project oversight for documentation.

* 
