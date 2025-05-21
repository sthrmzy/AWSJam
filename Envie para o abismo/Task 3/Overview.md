# 🌐 Understanding Egress-VPC Routing to the Internet

---

## 📘 **Background**

Now that you know how the traffic reached the **Transit Gateway** and exited it,  
you'll want to understand **what happens beyond that**.

---

## 🎯 **Your Task**

So far, we have traced the traffic up to the **Egress VPC**.

🔍 Your task is to **find out how the Egress VPC helps the traffic (from VPC-1) reach the Internet**.

- The traffic from **VPC-1** was routed to the **Egress VPC** via the **Transit Gateway**.
- **What happens next?**
- Your goal is to identify the **AWS Resource** to which this traffic is routed **from the Egress VPC**.

✍️ **Enter the ID of this AWS Resource** (the next routing hop) in the **answer field**.

---

## 🏗️ **Architecture**

📌 *Refer to the provided architecture diagram (not included here) for visual assistance.*

---

## 🛠️ **Services You Should Use**

- **Amazon VPC**

---

## ✅ **Task Validation**

Enter the **Resource ID** of the **next routing hop** into the answer field for validation.

This is typically the **Internet Gateway ID (igw-xxxxxxxx)** or a **NAT Gateway ID (nat-xxxxxxxx)**, depending on the setup of the **Egress VPC**.

---
