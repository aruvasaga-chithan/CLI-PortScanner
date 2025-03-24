# 🔍 Simple TCP Port Scanner

## 🚀 About the Project
A fast and efficient **TCP Port Scanner** written in Python using `socket`. This tool allows you to scan **single or multiple ports** on a target IP to check if they are **open or closed**.

## 🛠 Features
- 🎨 **Colored Output** for better readability
- 🔢 **Single & Range Port Scanning** (e.g., `-p 80` or `-p 20-25`)
- ⚡ **Fast Scanning** with timeout handling
- ✅ **Validates Target IP Address** before scanning

## 📦 Requirements
Ensure you have Python installed, then install dependencies using:
```bash
pip install -r requirements.txt
```

### 📜 Dependencies
- `socket`
- `argparse`
- `pyfiglet`
- `colorama`

## 🔧 Usage
Run the tool with the following command:
```bash
python port_scanner.py -H <IP_ADDRESS> -p <PORTS>
```

### 📌 Examples
- Scan a **single port** (e.g., 80):
  ```bash
  python port_scanner.py -H 192.168.1.1 -p 80
  ```
- Scan a **range of ports** (e.g., 20 to 25):
  ```bash
  python port_scanner.py -H 192.168.1.1 -p 20-25
  ```

## 🖥 Sample Output
```bash
🔥 SIMPLE TCP PORT SCANNER 🔥

PORT SCANNER

========================================
🔥 Port 22 is OPEN
⚠️ Port 23 is CLOSED
⚠️ Port 24 is CLOSED

✅ Scan completed!
🔹 Total Ports Scanned: 3
🔹 Open Ports: 1
🔹 Closed Ports: 2
```

## 📜 License
This project is open-source and available under the **Apache License 2.0**.

---

👨‍💻 **Author:** A. Aruvasaga Chithan 🚀

🔗 **GitHub:** [Aruvasaga Chithan](https://github.com/aruvasaga-chithan)  
🔗 **LinkedIn:** [Aruvasaga Chithan](https://www.linkedin.com/in/aruvasaga-chithan/)

