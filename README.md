# IAM Lab – Least Privilege User

## 🔍 Objective
Demonstrate how to create a secure IAM user with limited permissions and enable MFA.

## 🛠️ Tools & Services Used
- AWS IAM
- AWS Console

## 📝 What I Did
1. Created a new IAM user named `readonly-analyst`
2. Attached a custom policy granting `ec2:Describe*` and `s3:List*` only
3. Enabled MFA
4. Tested login with IAM user to verify limited access

## 📁 Files Included
| File | Description |
|------|-------------|
| `iam-readonly-policy.json` | Custom IAM policy file used in this lab |

## 💡 What I Learned
- How to define and apply least-privilege IAM policies
- How MFA protects root accounts and users
- IAM policies are written in JSON and can be customized by service/action
- IAM user password can only be reset by the root user or users with admin privledges

## 🔒 Security Concepts Covered
- IAM
- Least Privilege
- Multi-Factor Authentication (MFA)

## 📷 Screenshots
![Dashboard Users Image](./users.png)
![Dashboard Users Image](./console-access.png)
![Dashboard Users Image](./password.png)
![Dashboard Users Image](./password-reset.png)
![Dashboard Users Image](./limited-access.png)