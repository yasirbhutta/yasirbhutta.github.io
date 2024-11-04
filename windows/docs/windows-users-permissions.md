# Windows:Managing User Accounts and File Permissions on Windows

Connect with me: [Youtube](https://www.youtube.com/yasirbhutta) \| [LinkedIn](https://www.linkedin.com/in/yasirbhutta/) \| [WhatsApp Channel](https://whatsapp.com/channel/0029VaeGV0517En4iyZGWn2P) \| [Web](https://yasirbhutta.github.io/) \| [Facebook](https://www.facebook.com/yasirbhutta786) \| [Twitter](https://twitter.com/yasirbhutta)

- [Download PDF](https://yasirbhutta.github.io/windows/docs/windows-users-permissions.pdf)
- To access the updated handouts, please click on the following link:
[https://yasirbhutta.github.io/windows/docs/windows-users-permissions.html](https://yasirbhutta.github.io/sna/docs/windows-users-permissions.html)

### Lab Task #1: Create a New User with Limited Permissions on Windows
**Objective:**  Create a new user account on a Windows system with restricted access (limited permissions).

1. **Step 1: Open Control Panel**
   - Open the Start menu and type "Control Panel" in the search bar. Click on it.
   
2. **Step 2: Navigate to User Accounts**
   - In the Control Panel, go to **User Accounts**.
   - Click on **Manage another account**.

3. **Step 3: Add a New User**
   - Select **Add a new user in PC settings**.
   - In the settings, go to **Family & other users**.
   - Under **Other users**, click **Add someone else to this PC**.
   - Choose **I don’t have this person’s sign-in information** if you want to create a local account.
   - Then click on **Add a user without a Microsoft account**.

4. **Step 4: Set Up User Details**
   - Enter the desired **username** and **password** for the new account.
   - Click **Next** to create the account.

5. **Step 5: Change Account Type to Standard User**
   - After creating the account, select it from the **Other users** section.
   - Click **Change account type** and set it to **Standard User** (this ensures limited permissions).
   
6. **Step 6: Log in with the New Account**
   - Log out of the Admin account and log in with the newly created account to verify that the permissions are limited.

### Lab Task 2: Create a Folder on D Drive with Restricted Access
**Objective:** Students will create a folder on the D drive from the Admin account and restrict access to the newly created user.

1. **Step 1: Switch to Admin Account**
   - Ensure you are logged in with an **Admin** account.

2. **Step 2: Create a Folder on D Drive**
   - Navigate to the **D: drive** in **File Explorer**.
   - Right-click on an empty area, select **New**, and then **Folder**.
   - Name the folder (e.g., **RestrictedFolder**).

3. **Step 3: Set Folder Permissions**
   - Right-click on the newly created folder and select **Properties**.
   - Go to the **Security** tab.
   - Click on **Edit** under the group or user names section.

4. **Step 4: Add the Newly Created User**
   - Click on **Add**, then type in the username of the new user account you created.
   - Click **Check Names** to verify the user, then click **OK**.

5. **Step 5: Deny Access to the Folder**
   - Once the user is added, select the user in the list.
   - Under **Permissions for [user]**, check the **Deny** box for **Full control** (or any other permissions you want to restrict).
   - Click **Apply** and then **OK** to confirm the changes.

6. **Step 6: Test Access**
   - Log out of the Admin account and log in with the newly created user.
   - Navigate to the **D: drive** and try to access the restricted folder. You should receive an error message indicating that access is denied.

### Lab Summary:
- Students should now understand how to create a user with limited permissions on Windows and how to use folder permissions to restrict access to specific files or directories.

### Task #: Changing Password for a User Account
**Objective:** Change the password for an existing user account using the Admin account.

1. Log in with the Admin account.
2. Open **Control Panel** > **User Accounts** > **Manage another account**.
3. Select the user whose password you want to change.
4. Click **Change the password**, enter the new password, and confirm.
5. Log out and verify that the password change is successful.

### Task #: Apply Read-Only Permissions to a Folder for a User
**Objective:** Set up a folder that a standard user can access but only with read-only permissions.

1. Log in with the Admin account.
2. Create a folder in **D: drive** (e.g., **ReadOnlyFolder**).
3. Right-click the folder and select **Properties** > **Security**.
4. Add the standard user account and set **Read & Execute** and **Read** permissions while denying **Write**.
5. Log in with the standard user account and verify that the user can only read the files but cannot modify them.

### Task #: Create a Shared Folder with Specific Permissions for Multiple Users
**Objective:** Create a shared folder on the network with different permission levels for different users.

1. Log in with the Admin account.
2. Create a folder on the **D: drive** (e.g., **SharedFolder**).
3. Right-click the folder and select **Properties** > **Sharing** > **Advanced Sharing**.
4. Enable sharing and click **Permissions**.
5. Add multiple users and set different permissions (e.g., full control for one user, read-only for another).
6. Test by logging in as different users to verify permission levels.

### Task : Auditing File Access Attempts
**Objective:** Set up auditing to track file access attempts for specific users.

1. Log in with the Admin account.
2. Right-click the folder (e.g., **SensitiveData**) and go to **Properties** > **Security** > **Advanced**.
3. Go to the **Auditing** tab and click **Add**.
4. Select the users whose access attempts you want to audit and choose which actions (e.g., read, write) should trigger an audit log.
5. Review the audit logs in **Event Viewer** to monitor access attempts.

## Create new user using computer management

## Access Shared folders in Computer management

## Install Office 365
[Download and install or reinstall Microsoft 365 (for students)](https://gudgk.github.io/gu-userguides/microsoft365/install-microsoft365.html)
