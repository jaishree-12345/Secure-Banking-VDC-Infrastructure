# Secure-Banking-VDC-Infrastructure
A multi-tier Secure Virtual Data Center for Banking with pfSense Firewall and Snort IDS detection.
# Design and Implementation of a Secure Virtual Data Center (VDC) for Banking
**Internship Domain:** AI in Cybersecurity (Rooman Technologies)

## 📌 Project Overview
This project demonstrates the design of a virtualized banking infrastructure focused on high security and network isolation. The VDC is built using **Oracle VM VirtualBox** and features a three-tier architecture to protect sensitive financial data from unauthorized access.

## 🛡️ Security Architecture
![VDC Architecture](./VDC-Architecture.png)
The infrastructure is segmented into three logical nodes:
1. **Firewall Gateway (pfSense):** Acts as the perimeter defense, managing traffic flow between the internet and the internal secure network.
2. **Bank Vault Server (Ubuntu 22.04 LTS):** Hosts the banking microservices and an SQLite database.
3. **Security Audit Node (Kali Linux):** Used for vulnerability assessment and simulated penetration testing.

## 🚀 Key Features
- **Network Segmentation:** Isolated `vdc-secure` internal network prevents direct host-to-server communication.
- **Intrusion Detection:** Real-time monitoring using **Snort IDS** with custom signatures for SQL Injection detection.
- **Enterprise Portal:** A multi-page Flask-based banking application including Login, Dashboard, and Transaction modules.

## 🧪 Security Simulation (SQL Injection)
The system's defense was validated by simulating a SQL Injection bypass:
- **Payload:** `' OR 1=1 --`
- **Result:** While the logic was bypassed at the app layer, the **Snort IDS** successfully captured the malicious packet and logged a high-priority alert.

## 🛠️ Technology Stack
- **Virtualization:** Oracle VM VirtualBox
- **Firewall:** pfSense
- **Server:** Ubuntu Server
- **IDS:** Snort
- **Backend:** Python (Flask), SQLite
- **Frontend:** HTML5, CSS3

## 🔮 Future Scope (AI Integration)
As an AI in Cybersecurity intern, the next phase involves replacing signature-based detection with **Machine Learning Anomaly Detection** models to identify zero-day threats in bank traffic patterns.
